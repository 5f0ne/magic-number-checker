import json 

class SignatureChecker():
    def __init__(self) -> None:
        f = open("data/signatures.json", encoding="utf8")
        self.signatureTable = json.load(f)      
        # The signatures need to be sorted starting form the longest to the shortest one
        self.signatureTable["signatures"] = sorted(self.signatureTable["signatures"], key=lambda d: len(d['Header (hex)']), reverse=True)        


    def check(self, hexStringHeader, hexStringTrailer):
        sigHeaderFound = False
        sigTrailerFound = False

        for signature in self.signatureTable["signatures"]:
            headerSignature = self.__formatSignature(signature["Header (hex)"])
    
            lenSigHeader = len(headerSignature)
            headerOffset = int(signature["Header offset"])

            trimmedHeader = hexStringHeader[headerOffset:(headerOffset+lenSigHeader)]

            # self.__debug(lenSigHeader, headerOffset, headerSignature, trimmedHeader)

            if (headerSignature == trimmedHeader):
                sigHeaderFound = True
                hexHeader = self.__formatHex(signature["Header (hex)"])
                hexTrailer = self.__formatHex(signature["Trailer (hex)"])
                
                print("")
                print("--- Description ---> " + signature["File description"]) 
                print("-- Header Offet ---> " + signature["Header offset"]) 
                print("-------- Header ---> " + hexHeader.lower()) 
                print("------- Trailer ---> " + hexTrailer.lower()) 
                print("----- Extension ---> " + signature["File extension"]) 
                print("---- File Class ---> " + signature["FileClass"]) 
                print("")
            
        if(not sigHeaderFound):
            print("")
            print(f"-----------------> The filetype could not be determined")
            print("")

        print("################################################################################")

    def __formatSignature(self, s):
        return s.lower().replace(" ", "")
    
    def __formatHex(self, s):
        r = s.replace(" ", "")
        return " ".join(r[i:i+4] for i in range(0, len(r), 4))

    def __debug(self, a, b, c, d):
        print(" Signature Length: " + str(a))
        print("    Header Offset: " + str(b))
        print("Current Signature: " + c)
        print("   Trimmed Header: " + d)
        print("----------------------------------------------------------------------------")