# import DecimalToBinary
# #-----------------------------------------------------------------------------------------------------------------------
# class PC:
#     def __init__(self, PCcounter):
#         self.PCcounter = PCcounter

#     # ------------------------------------------------------------------------------------------------------------------
#     def pcAdds4(self):
#         result = ""
#         binaryFour = DecimalToBinary.DecimalToBinary(4).DecimalToBinary("")
#         carry = 0
#         for counter32Bits in range(32):
#             if (self.PCcounter[32 - counter32Bits - 1] == '0' and binaryFour[32 - counter32Bits - 1] == '0' and carry == 0):
#                 result = '0' + result
#                 carry = 0
#             elif (self.PCcounter[32 - counter32Bits - 1] == '0' and binaryFour[32 - counter32Bits - 1] == '0' and carry == 1):
#                 result = '1' + result
#                 carry = 0
#             elif (self.PCcounter[32 - counter32Bits - 1] == '1' and binaryFour[32 - counter32Bits - 1] == '0' and carry == 0):
#                 result = '1' + result
#                 carry = 0
#             elif (self.PCcounter[32 - counter32Bits - 1] == '1' and binaryFour[32 - counter32Bits - 1] == '0' and carry == 1):
#                 result = '0' + result
#                 carry = 1
#             elif (self.PCcounter[32 - counter32Bits - 1] == '0' and binaryFour[32 - counter32Bits - 1] == '1' and carry == 0):
#                 result = '1' + result
#                 carry = 0
#             elif (self.PCcounter[32 - counter32Bits - 1] == '0' and binaryFour[32 - counter32Bits - 1] == '1' and carry == 1):
#                 result = '0' + result
#                 carry = 1
#             elif (self.PCcounter[32 - counter32Bits - 1] == '1' and binaryFour[32 - counter32Bits - 1] == '1' and carry == 0):
#                 result = '0' + result
#                 carry = 1
#             elif (self.PCcounter[32 - counter32Bits - 1] == '1' and binaryFour[32 - counter32Bits - 1] == '1' and carry == 1):
#                 result = '1' + result
#                 carry = 1
#         return result



