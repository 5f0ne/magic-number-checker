import os
import argparse
import time
from datetime import datetime

from src.FileParser import FileParser
from src.SignatureChecker import SignatureChecker

parser = argparse.ArgumentParser()
parser.add_argument("--path", "-p", type=str, required=True, help="Path to the directory containing the files")
parser.add_argument("--headerBytes", "-e", type=int, default=512, help="Number of first bytes to read")
parser.add_argument("--trailerBytes", "-t", type=int, default=32, help="Number of last bytes to read")
args = parser.parse_args()

dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

print("################################################################################")
print("")
print("Magic Number Checker by 5f0")
print("Indicates the type of the file based on their magic number")
print("")
print("Current working directory: " + os.getcwd())
print("Investigate files in: " + args.path)
print("")
print("Current Datetime: " + dt_string)
print("")
print("################################################################################")

parser = FileParser()
checker = SignatureChecker()

start = time.time()

for path, dirs, files in os.walk(args.path):
    for file in files:
        currentFile = os.path.join(path, file)

        print("")
        print("Investigated File: " + currentFile)
        
        # Read the first x bytes and get the hex string
        firstHexString = parser.getFirstBytesAsHexString(currentFile, args.headerBytes)
        
        # Print the first x bytes of the file
        parser.printHexTable(firstHexString, args.headerBytes, "First")

         # Read the last x bytes
        lastHexString = parser.getLastBytesAsHexString(currentFile, args.trailerBytes)

        # Print the last x bytes of the file
        parser.printHexTable(lastHexString, args.trailerBytes, "Last")

        # Check if a header signature is matching 
        checker.check(firstHexString, lastHexString)

end = time.time()

print("Execution Time: " + str(end-start)[0:8] + " sec")
print("################################################################################")
       