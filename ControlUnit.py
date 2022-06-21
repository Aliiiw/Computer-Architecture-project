# all_instructions  = ["None" , "Add"  , "Sub"  , "And" , "Or"  , "Slt"  , "Nor"]
# all_instructions += ["Xor " , "LW"   , "Sw"   , "Beq" , "Bnq" , "J"           ]

# #   all_instructions  = ["Add"  , "Sub"  , "Addi" , "Lw"  , "Sw"  , "Lh"   , "Lhu"]
# #   all_instructions += ["Sh"   , "Lb"   , "Lbu"  , "Sb"  , "And" , "Or"   , "Nor"]
# #   all_instructions += ["Andi" , "Ori"  , "Sll"  , "Srl" , "Beq" , "Bne"  , "Slt"]
# #   all_instructions += ["Sltu" , "Slti" , "J"    , "Jr"  , "Jal" , "None"        ]


# instructions = {}
# opcodes = {}

# for i in range(len(all_instructions)):
#     bincode = bin(i)[2:]
#     bincode = (6-len(bincode))*'0' + bincode
#     instructions [bincode] = all_instructions[i]
#     opcodes [all_instructions[i]] = bincode

# #opcodes = {}
# #for x in instructions :
# #    opcodes[instructions[x]] = x
    
    
# class ControlUnit:
    
#     def __init__(self,opcode,inputed_instruction = "N/A"):
#         self.opcode = opcode
#         self.inputed_instruction = inputed_instruction

    
#     def instruction(self):
#         if self.inputed_instruction != "N/A" :
#             return self.inputed_instruction
        
#         if self.opcode in instructions:
#             self.inputed_instruction = instructions [self.opcode]
#             return instructions [self.opcode]
#         else :
#             return "N/A"
        
#     def get_opcode(self):
#         if self.opcode != "N/A" :
#             return self.opcode
        
#         if self.instuction in opcodes:
#             self.opcodes = [self.instruction]
#             return opcodes[self.instuction]
#         else :
#             return "N/A"
        