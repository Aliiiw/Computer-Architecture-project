import RegisterFile
import PC
import ControlUnit
import time

class InstructionMemory:
    def __init__(self, instruction, array, counter, PCcounter):
        self.array = array
        self.counter = counter
        self.instruction = instruction
        self.PCcounter = PCcounter
        
    def fetch(self):

        opcode = ""
        rs = ""
        rt = ""
        rd = ""

        constant_address_Itype = ""
        constant_address_Jtype = ""
        opcode = self.instruction [0:6]
        rs     = self.instruction [6:11]
        rt     = self.instuction  [11:16]
        rd     = self.instuction  [16:21]
        constant_address_Itype = self.instuction [16 :32]
        constant_address_Jtype = self.instuction [ 6 :32]

        controlKey = ControlUnit.ControlUnit(opcode).instruction()
        
        if(controlKey == "N/A"):
            return "Undefined opcode"
        
        rs = (32-len(rs))*'0' + rs
        rt = (32-len(rs))*'0' + rt
        rd = (32-len(rs))*'0' + rd
        
        if(controlKey == "J"):
            
            constant_address_Jtype  = self.PCcounter[31]
            constant_address_Jtype += self.PCcounter[30]
            constant_address_Jtype += self.PCcounter[29]
            constant_address_Jtype += self.PCcounter[28]
            constant_address_Jtype += constant_address_Jtype + "00"

            self.array[0][0] = controlKey
            self.array[0][1] = "InstructionMemory"
            self.array[0][2] = "00000000000000000000000000000000"
            self.array[0][3] = "00000000000000000000000000000000"
            self.array[0][4] = "00000000000000000000000000000000"
            self.array[0][5] = constant_address_Jtype
            return "J"
            
        self.array[0][0] = controlKey
        self.array[0][1] = "InstructionMemory"
        self.array[0][2] = rs
        self.array[0][3] = rt
        self.array[0][4] = rd
        self.array[0][5] = constant_address_Itype