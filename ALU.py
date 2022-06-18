
import MEMWB
import BinaryToDecimal
import DecimalToBinary

#-----------------------------------------------------------------------------------------------------------------------

class ALU:
    def __init__(self,firstInput,secondInput,destination,ALUopKey,array,counter):
        self.firstInput=firstInput
        self.secondInput=secondInput
        self.destination=destination
        self.ALUopKey=ALUopKey
        self.array=array
        self.counter=counter

    # -----------------------------------------------------------------------------------------------------------------------

    def operating(self):
        # ALU Operation Key : Add - Lw - Sw
        if(self.ALUopKey=="Add" or self.ALUopKey=="Lw" or self.ALUopKey=="Sw"):
            result=""
            carry=0
            for counter32Bits in range(32):
                if(self.firstInput[32-counter32Bits-1]=='0' and self.secondInput[32-counter32Bits-1]=='0' and carry==0):
                    result='0'+result
                    carry=0
                elif(self.firstInput[32-counter32Bits-1]=='0' and self.secondInput[32-counter32Bits-1]=='0' and carry==1):
                    result='1'+result
                    carry=0
                elif(self.firstInput[32-counter32Bits-1]=='1' and self.secondInput[32-counter32Bits-1]=='0' and carry==0):
                    result='1'+result
                    carry=0
                elif(self.firstInput[32-counter32Bits-1]=='1' and self.secondInput[32-counter32Bits-1]=='0' and carry==1):
                    result='0'+result
                    carry=1
                elif(self.firstInput[32-counter32Bits-1]=='0' and self.secondInput[32-counter32Bits-1]=='1' and carry==0):
                    result='1'+result
                    carry=0
                elif(self.firstInput[32-counter32Bits-1]=='0' and self.secondInput[32-counter32Bits-1]=='1' and carry==1):
                    result='0'+result
                    carry=1
                elif(self.firstInput[32-counter32Bits-1]=='1' and self.secondInput[32-counter32Bits-1]=='1' and carry==0):
                    result='0'+result
                    carry=1
                elif(self.firstInput[32-counter32Bits-1]=='1' and self.secondInput[32-counter32Bits-1]=='1' and carry==1):
                    result='1'+result
                    carry=1
            self.array[2][0]=self.ALUopKey
            self.array[2][1]="ALU"
            self.array[2][2]="00000000000000000000000000000000"
            self.array[2][3]=result
            self.array[2][4]=self.destination
            self.array[2][5]="00000000000000000000000000000000"

        # -----------------------------------------------------------------------------------------------------------------------
        # ALU Operation Key : Sub
        if(self.ALUopKey=="Sub"):
            result=""
            for counter32Bits in range(32):
                if(self.secondInput[32-counter32Bits-1]=='1'):
                    result=self.secondInput[32-counter32Bits-1]+result
                    for j in range(32-counter32Bits-1):
                        if(self.secondInput[32-counter32Bits-j-2]=='0'):
                            result='1'+result
                        else:
                            result='0'+result
                    break
                else:
                    result=self.secondInput[32-counter32Bits-1]+result
            result_sub=""
            carry=0
            for counter32Bits in range(32):
                if(self.firstInput[32-counter32Bits-1]=='0' and result[32-counter32Bits-1]=='0' and carry==0):
                    result_sub='0'+result_sub
                    carry=0
                elif(self.firstInput[32-counter32Bits-1]=='0' and result[32-counter32Bits-1]=='0' and carry==1):
                    result_sub='1'+result_sub
                    carry=0
                elif(self.firstInput[32-counter32Bits-1]=='1' and result[32-counter32Bits-1]=='0' and carry==0):
                    result_sub='1'+result_sub
                    carry=0
                elif(self.firstInput[32-counter32Bits-1]=='1' and result[32-counter32Bits-1]=='0' and carry==1):
                    result_sub='0'+result_sub
                    carry=1
                elif(self.firstInput[32-counter32Bits-1]=='0' and result[32-counter32Bits-1]=='1' and carry==0):
                    result_sub='1'+result_sub
                    carry=0
                elif(self.firstInput[32-counter32Bits-1]=='0' and result[32-counter32Bits-1]=='1' and carry==1):
                    result_sub='0'+result_sub
                    carry=1
                elif(self.firstInput[32-counter32Bits-1]=='1' and result[32-counter32Bits-1]=='1' and carry==0):
                    result_sub='0'+result_sub
                    carry=1
                elif(self.firstInput[32-counter32Bits-1]=='1' and result[32-counter32Bits-1]=='1' and carry==1):
                    result_sub='1'+result_sub
                    carry=1
            self.array[2][0]=self.ALUopKey
            self.array[2][1]="ALU"
            self.array[2][2]="00000000000000000000000000000000"
            self.array[2][3]=result_sub
            self.array[2][4]=self.destination
            self.array[2][5]="00000000000000000000000000000000"

        # -----------------------------------------------------------------------------------------------------------------------
        # ALU Operation Key : And
        if(self.ALUopKey=="And"):
            result_And=""
            for counter32Bits in range (32):
                if(self.firstInput[32-counter32Bits-1]=='1' and self.secondInput[32-counter32Bits-1]=='1'):
                    result_And='1'+result_And
                else:
                    result_And='0'+result_And
            self.array[2][0]=self.ALUopKey
            self.array[2][1]="ALU"
            self.array[2][2]="00000000000000000000000000000000"
            self.array[2][3]=result_And
            self.array[2][4]=self.destination
            self.array[2][5]="00000000000000000000000000000000"

        # -----------------------------------------------------------------------------------------------------------------------
        # ALU Operation Key : Or
        if(self.ALUopKey=="Or"):
            result_Or=""
            for counter32Bits in range(32):
                if(self.firstInput[32-counter32Bits-1]=='0' and self.secondInput[32-counter32Bits-1]=='0'):
                    result_Or='0'+result_Or
                else:
                    result_Or='1'+result_Or
            self.array[2][0]=self.ALUopKey
            self.array[2][1]="ALU"
            self.array[2][2]="00000000000000000000000000000000"
            self.array[2][3]=result_Or
            self.array[2][4]=self.destination
            self.array[2][5]="00000000000000000000000000000000"

        # -----------------------------------------------------------------------------------------------------------------------
        # ALU Operation Key : Nor
        if(self.ALUopKey=="Nor"):
            result_Nor=""
            for counter32Bits in range(32):
                if(self.firstInput[32-counter32Bits-1]=='0' and self.secondInput[32-counter32Bits-1]=='0'):
                    result_Nor='1'+result_Nor
                else:
                    result_Nor='0'+result_Nor
            self.array[2][0]=self.ALUopKey
            self.array[2][1]="ALU"
            self.array[2][2]="00000000000000000000000000000000"
            self.array[2][3]=result_Nor
            self.array[2][4]=self.destination
            self.array[2][5]="00000000000000000000000000000000"

        # -----------------------------------------------------------------------------------------------------------------------
        # ALU Operation Key : XOR
        if(self.ALUopKey=="Xor"):
            result_Xor=""
            for counter32Bits in range(32):
                if ((self.firstInput[32-counter32Bits-1]=='0' and self.secondInput[32-counter32Bits-1]=='0') or (self.firstInput[32-counter32Bits-1]=='1' and self.secondInput[32-counter32Bits-1]=='1')):
                    result_Xor='0'+result_Xor
                else:
                    result_Xor='1'+result_Xor
            self.array[2][0]=self.ALUopKey
            self.array[2][1]="ALU"
            self.array[2][2]="00000000000000000000000000000000"
            self.array[2][3]=result_Xor
            self.array[2][4]=self.destination
            self.array[2][5]="00000000000000000000000000000000"

        # -----------------------------------------------------------------------------------------------------------------------
        # ALU Operation Key : Slt
        if(self.ALUopKey=="Slt"):
            result_Slt=""
            if(BinaryToDecimal.BinaryToDecimal(self.firstInput).BinaryToDecimal()<BinaryToDecimal.BinaryToDecimal(self.secondInput).BinaryToDecimal()):
                result_Slt="00000000000000000000000000000001"
            else:
                result_Slt="00000000000000000000000000000000"
            self.array[2][0]=self.ALUopKey
            self.array[2][1]="ALU"
            self.array[2][2]="00000000000000000000000000000000"
            self.array[2][3]=result_Slt
            self.array[2][4]=self.destination
            self.array[2][5]="00000000000000000000000000000000"

        # -----------------------------------------------------------------------------------------------------------------------
        # ALU Operation Key : Nop
        if(self.ALUopKey=="None" or self.ALUopKey=="Nope" or self.ALUopKey=="Beq" or self.ALUopKey=="Bne" or self.ALUopKey=="J"):
            self.array[2][0]=self.ALUopKey
            self.array[2][1]="ALU"
            self.array[2][2]="00000000000000000000000000000000"
            self.array[2][3]="00000000000000000000000000000000"
            self.array[2][4]="00000000000000000000000000000000"
            self.array[2][5]="00000000000000000000000000000000"

