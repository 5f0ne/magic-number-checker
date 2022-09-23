from binascii import hexlify
from distutils.util import split_quoted
import hashlib

class FileParser():
    def __init__(self) -> None:
        pass

    def calculateFileHash(self, path):
        hashes = {}
        sha256 = hashlib.sha256()
        md5 = hashlib.md5()

        with open(path, "rb") as f:
            while True:
                data = f.read(65536) 
                if not data:
                    break
                sha256.update(data)
                md5.update(data)

        hashes["sha256"] = sha256.hexdigest()
        hashes["md5"] = md5.hexdigest()
        
        return hashes

    def getFirstBytesAsHexString(self, path, noOfBytes):
        # Open current file 
        binary  = open(path, "rb")
        # Read the current files first bytes
        bytes_ = binary.read(noOfBytes)
        # 
        return self.getHexString(bytes_)

    
    def getLastBytesAsHexString(self, path, noOfBytes):
         # Open current file 
        binary  = open(path, "rb")
        # Read the current files last bytes
        binary.seek(-noOfBytes, 2)
        bytes_ = binary.read(noOfBytes)
        # 
        return self.getHexString(bytes_)


    def getHexString(self, bytes_):
        # Convert the bytes to a list of hex values
        hexlist = [hex(x).split('x')[-1] for x in list(bytes_)]
        l = []
        
        # Convert the list of hex values of the file to a string
        hexstring = ""  
        for hex_ in hexlist:
            # While converting the bytes, the leading zeros gets cut of
            # the following instructions check if there are 2 characters
            # and adds a leading zero if necessary
            val = ""
            if(len(hex_) == 2):
                val = hex_
            elif(len(hex_) == 1):
                val = "0" + hex_
            hexstring += val
            l.append(val.upper())

        return hexstring, l

    def printHexTableHeader(self, heading, bytes_):
        h = "{:4} {:4} {:4} {:4} {:4} {:4} {:4} {:4}   {:4} {:4} {:4} {:4} {:4} {:4} {:4} {:4}      {:5}".format(" 0", " 1", " 2", " 3", " 4", " 5",
                                                                                                                 " 6", " 7", " 8", " 9", " A", " B",
                                                                                                                 " C", " D", " E", " F", "ASCII")
        print("")
        print("")
        print(f"--> {heading} {str(bytes_)} Bytes")
        print("")
        print(h)
        print("-------------------------------------------------------------------------------        ----------------")


    def printHexTable(self, hexList):
        splitted = [hexList[x:x+16] for x in range(0, len(hexList), 16)]
        self.__printHexTable(splitted)

    def __printHexTable(self, lines):
        formatStr = "{:4} {:4} {:4} {:4} {:4} {:4} {:4} {:4}   {:4} {:4} {:4} {:4} {:4} {:4} {:4} {:4}      {:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}"

        for line in lines:
            while True:
                if (len(line) < 16):    # Padding for output
                    line.append("  ")
                else:
                    break
            
            a = [] # Contains the ascii values
            for i in range(0, 16):
                a.append(self.hexToAscii(line[i]))

            h = line

            r = formatStr.format(h[0], h[1], h[2], h[3], h[4], h[5], h[6], h[7],
                                 h[8], h[9], h[10], h[11], h[12], h[13], h[14], h[15],
                                 a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], 
                                 a[8], a[9], a[10], a[11], a[12], a[13], a[14], a[15])
            print(r)


    def hexToAscii(self, hex_):
        result = "."
        if (hex_ != "  "):
            d = int(hex_, 16)
            if (d >= 32 and d <= 126):
                result = chr(d)
        return result
    