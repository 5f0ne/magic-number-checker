class FileParser():
    def __init__(self) -> None:
        pass

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

        return hexstring

    
    def printHexTable(self, hexstring, bytes, heading):
        print("")
        print(f"------------------------- File Hex - {heading} {str(bytes)} Bytes --------------------------")
        i = 0
        j = 0
        v = ""
        hexTable= ""
        for h in hexstring:
            if(j == 48):
                hexTable += "\n"
                j = 0
            if(i < 3):
                v+=h
            elif(i == 3):
                hexTable += (v + h)[:2] + "" + (v+h)[2:] + " "
                i = 0
                v = ""
                continue
            i += 1
            j += 1

        print(hexTable)