import BinaryToDecimal
#-----------------------------------------------------------------------------------------------------------------------
registersArray=[]
file = open("registersArray.txt", "r")
for each in file:
    if(each!='\n'):
        registersArray.append(each[:32])
file.close()
#-----------------------------------------------------------------------------------------------------------------------
class WriteBack:
    def __init__(self,result1,controlKey,array,counter):
        self.result1=result1
        self.controlKey=controlKey
        self.array=array
        self.counter=counter
        # --------------------------------------------------------------------------------------------------------------
    def making_decition(self):
        if(self.array[4][0]=="None" or self.array[4][0]=="Sw" or self.array[4][0]=="Bne" or self.array[4][0]=="Beq" or self.array[4][0]=="J" or self.controlKey=="Nope"):
            self.array[4][1]="WriteBack"
            return
        else:
            registersArray[BinaryToDecimal.BinaryToDecimal(self.array[4][4]).BinaryToDecimal()]=self.result1
            self.array[4][1]="WriteBack"
            # ----------------------------------------------------------------------------------------------------------
            # Writing new values to registersArray
            F=open("registersArray.txt","w")
            for i in range(0, len(registersArray)):
                F.write(str(registersArray[i]))
                F.write('\n')
            F.close()
            return
