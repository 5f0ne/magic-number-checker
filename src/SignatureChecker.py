import json 

class SignatureChecker():
    def __init__(self) -> None:
        f = open("data/signatures.json", encoding="utf8")
        self.signatureTable = json.load(f)      
        # The signatures need to be sorted starting form the longest to the shortest one
        self.signatureTable["signatures"] = sorted(self.signatureTable["signatures"], key=lambda d: len(d['Header (hex)']), reverse=True)        


    def check(self, hexStringHeader, hexStringTrailer):
        sigHeaderFound = False

        print("")
        print("")
        print("--> Matches: ")

        for signature in self.signatureTable["signatures"]:
            headerSignature = self.__formatSignature(signature["Header (hex)"])
    
            lenSigHeader = len(headerSignature)
            headerOffset = int(signature["Header offset"])

            trimmedHeader = hexStringHeader[headerOffset:(headerOffset+lenSigHeader)]

            # self.__debug(lenSigHeader, headerOffset, headerSignature, trimmedHeader)

            if (headerSignature == trimmedHeader):
                sigHeaderFound = True
                        
                print("")
                print(" Description: " + signature["File description"]) 
                print("Header Offet: " + signature["Header offset"]) 
                print("      Header: " + signature["Header (hex)"]) 
                print("     Trailer: " + signature["Trailer (hex)"]) 
                print("   Extension: " + signature["File extension"]) 
                print("  File Class: " + signature["FileClass"]) 
                print("")
            
        if(not sigHeaderFound):
            print("")
            print(f"--> The filetype could not be determined")
            print("")

        print("########################################################################################################")

    def __formatSignature(self, s):
        return s.lower().replace(" ", "")
    
    def __debug(self, a, b, c, d):
        print(" Signature Length: " + str(a))
        print("    Header Offset: " + str(b))
        print("Current Signature: " + c)
        print("   Trimmed Header: " + d)
        print("----------------------------------------------------------------------------")