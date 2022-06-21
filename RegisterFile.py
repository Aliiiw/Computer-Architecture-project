# import CU
# import DecimalToBinary
# import BinaryToDecimal
# import SignExtended
# import ALU
# import PC

# class RegisterFile:
#     def __init__(self, registerRs, registerRt, registerRd, controlKey, constantAddress,
#     array, counter, PCcounter):
#         self.registerRs = registerRs
#         self.registerRt = registerRt
#         self.registerRd = registerRd
#         self.controlKey = controlKey
#         self.constantAddress = constantAddress
#         self.array = array
#         self.counter = counter
#         self.PCcounter = PCcounter

#     def registerInputs(self):

#         registers = []
#         file = open("registers.txt", "r")
#         for each in file: 
#             registers.append(each[:32])
#         file.close()

#         if (self.controlKey == "Add" or 
#         self.controlKey == "Sub" or 
#         self.controlKey == "And" or 
#         self.controlKey == "Or" or 
#         self.controlKey == "Slt" or 
#         self.controlKey == "Nor" or
#         self.controlKey == "Xor"):
#             first_input = registers[BinaryToDecimal.BinaryToDecimal(self.registerRs).BinaryToDecimal()]
#             second_input = registers[BinaryToDecimal.BinaryToDecimal(self.registerRt).BinaryToDecimal()]
#             destination = self.registerRd
#             while(len(destination) != 32):
#                 destination = '0' + destination
#             self.array[1][0] = self.controlKey
#             self.array[1][1] = "RegisterFile"
#             self.array[1][2] = first_input
#             self.array[1][3] = second_input
#             self.array[1][4] = destination
#             self.array[1][5] = self.constantAddress
#         if (self.controlKey == "Beq"):
#             first_input = ""
#             second_input = ""
#             destination_for_pc = ""
#             first_input = registers[BinaryToDecimal.BinaryToDecimal(self.registerRs).BinaryToDecimal()]
#             second_input = registers[BinaryToDecimal.BinaryToDecimal(self.registerRt).BinaryToDecimal()]
#             destination_for_pc = SignExtended.SignExtend(self.constantAddress).extending()
#             if(first_input == second_input):
#                 destinationArray = ""
#                 destinationArray = destination_for_pc + "00"
#                 destination_for_pc = ""
#                 for i in range(2, 34):
#                     destination_for_pc += destinationArray[i]
#                 result = ""
#                 carry = 0
#                 for i in range(32):
#                     if(self.PCcounter[32 - i - 1] == '0' and 
#                     destination_for_pc[32 - i - 1] == '0' and carry == 0):
#                         result = '0' + result
#                         carry = 0
#                     elif(self.PCcounter[32 - i - 1] == '0' and 
#                     destination_for_pc[32 - i - 1] == '0' and carry == 1):
#                         result = '1' + result
#                         carry = 0
#                     elif(self.PCcounter[32 - i - 1] == '1' and 
#                     destination_for_pc[32 - i - 1] == '0' and carry == 0):
#                         result = '1' + result
#                         carry = 0
#                     elif(self.PCcounter[32 - i - 1] == '1' and 
#                     destination_for_pc[32 - i - 1] == '0' and carry == 1):
#                         result = '0' + result
#                         carry = 1
#                     elif(self.PCcounter[32 - i - 1] == '0' and 
#                     destination_for_pc[32 - i - 1] == '1' and carry == 0):
#                         result = '1' + result
#                         carry = 0
#                     elif(self.PCcounter[32 - i - 1] == '0' and 
#                     destination_for_pc[32 - i - 1] == '1' and carry == 1):
#                         result='0'+result
#                         carry=1
#                     elif(self.PCcounter[32 - i - 1] == '1' and 
#                     destination_for_pc[32 - i - 1] == '1' and carry == 0):
#                         result = '0' + result
#                         carry = 1
#                     elif(self.PCcounter[32 - i - 1] == '1' and 
#                     destination_for_pc[32-i-1] == '1' and carry == 1):
#                         result = '1' + result
#                         carry = 1
#                 self.array[0][2] = result
#                 return "NopeBranch"
#             else:
#                 self.array[1][0] = self.controlKey
#                 self.array[1][1] = "RegisterFile"
#                 self.array[1][2] = "00000000000000000000000000000000"
#                 self.array[1][3] = "00000000000000000000000000000000"
#                 self.array[1][4] = "00000000000000000000000000000000"
#                 self.array[1][5] = "00000000000000000000000000000000"
#         if (self.controlKey == "Bne"):
#             first_input = ""
#             second_input = ""
#             destination_for_pc = ""
#             first_input = registers[BinaryToDecimal.BinaryToDecimal(self.registerRs).BinaryToDecimal()]
#             second_input = registers[BinaryToDecimal.BinaryToDecimal(self.registerRt).BinaryToDecimal()]
#             destination_for_pc = SignExtended.SignExtend(self.constantAddress).extending()
#             if(first_input != second_input):
#                 destinationArray = ""
#                 destinationArray = destination_for_pc+"00"
#                 destination_for_pc = ""
#                 for i in range(2, 34):
#                     destination_for_pc += destinationArray[i]
#                 result = ""
#                 carry = 0
#                 for i in range(32):
#                     if(self.PCcounter[32 - i - 1] == '0' and 
#                     destination_for_pc[32 - i - 1 ] == '0' and carry == 0):
#                         result = '0' + result
#                         carry = 0
#                     elif(self.PCcounter[32 - i - 1] == '0' and 
#                     destination_for_pc[32 - i - 1] == '0' and carry == 1):
#                         result = '1' + result
#                         carry = 0
#                     elif(self.PCcounter[32 - i - 1] == '1' and 
#                     destination_for_pc[32 - i - 1] == '0' and carry == 0):
#                         result = '1' + result
#                         carry = 0
#                     elif(self.PCcounter[32 - i - 1] == '1' and 
#                     destination_for_pc[32 - i - 1] == '0' and carry == 1):
#                         result = '0' + result
#                         carry = 1
#                     elif(self.PCcounter[32 - i - 1] == '0' and 
#                     destination_for_pc[32 - i - 1 ] == '1' and carry == 0):
#                         result = '1' + result
#                         carry = 0
#                     elif(self.PCcounter[32 - i - 1] == '0' and 
#                     destination_for_pc[32 - i - 1] == '1' and carry == 1):
#                         result = '0' + result
#                         carry = 1
#                     elif(self.PCcounter[32 - i - 1] == '1' and 
#                     destination_for_pc[32 - i - 1] == '1' and carry == 0):
#                         result = '0' + result
#                         carry = 1
#                     elif(self.PCcounter[32 - i - 1] == '1' and 
#                     destination_for_pc[32 - i - 1] == '1' and carry == 1):
#                         result = '1' + result
#                         carry = 1
#                 self.array[0][2] = result
#                 return "NopeBranch"
#             else:
#                 self.array[1][0] = self.controlKey
#                 self.array[1][1] = "RegisterFile"
#                 self.array[1][2] = "00000000000000000000000000000000"
#                 self.array[1][3] = "00000000000000000000000000000000"
#                 self.array[1][4] = "00000000000000000000000000000000"
#                 self.array[1][5] = "00000000000000000000000000000000"
#         if(self.controlKey == "Lw" or self.controlKey == "Sw"):
#             first_input = ""
#             second_input = ""
#             destination = ""
#             destination = registers[BinaryToDecimal.BinaryToDecimal(self.registerRt).BinaryToDecimal()]
#             first_input = registers[BinaryToDecimal.BinaryToDecimal(self.registerRs).BinaryToDecimal()]
#             second_input = SignExtended.SignExtend(self.constantAddress).extending()
#             self.array[1][0] = self.controlKey
#             self.array[1][1] = "RegisterFile"
#             self.array[1][2] = first_input
#             self.array[1][3] = second_input
#             self.array[1][4] = destination
#             self.array[1][5] = self.registerRt
#         if(self.controlKey == "None" or self.controlKey == "J"):
#             self.array[1][0] = self.controlKey
#             self.array[1][1] = "RegisterFile"
#             self.array[1][2] = "00000000000000000000000000000000"
#             self.array[1][3] = "00000000000000000000000000000000"
#             self.array[1][4] = "00000000000000000000000000000000"
#             self.array[1][5] = "00000000000000000000000000000000"