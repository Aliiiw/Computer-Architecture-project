def flip(c):
    return '1' if (c == '0') else '0'

def OneAndTwosComplement(bin):
    n = len(bin)
    ones = ""
    twos = ""
    for i in range(n):
        ones += flip(bin[i])
    ones = list(ones.strip(""))
    twos = list(ones)
    for i in range(n - 1, -1, -1):
        if (ones[i] == '1'):
            twos[i] = '0'
        else:        
            twos[i] = '1'
            break
    i -= 1   
    if (i == -1):
        twos.insert(0, '1')
    twosComplement = ""
    for i in twos:
         twosComplement += i
    return twosComplement
#---------------------------------------------------------------------------------------------------------------------------

def ALU(controlLine , reg_1 , reg_2):
    shiftAmount = int(reg_2,2) 
    result = ""
    
    if controlLine == "0000":
        result = int(reg_1,2) & int(reg_2,2)
        result = '{:032b}'.format(result)
        return result
    #------------------------------------------------------------------------------
    elif controlLine == "0001":
        result = bin(int(reg_1,2) | int(reg_2,2))
        result = '{:032b}'.format(int(result,2))
        return result
    #------------------------------------------------------------------------------
    elif controlLine == "0010":
        result = bin(int(reg_1,2) + int(reg_2,2))[2:]
        result = '{:032b}'.format(int(result,2))
        return result
    #------------------------------------------------------------------------------
    elif controlLine == "0110":
        reg_2 = OneAndTwosComplement('{:032b}'.format(int(reg_2,2)))
        result = bin(int(reg_1,2) + int(reg_2,2))[2:]
        result = '{:032b}'.format(int(result,2))
        return result
    #------------------------------------------------------------------------------
    elif controlLine == "0111":
        if (reg_1[0] == '1' and reg_2[0] == '0'):
            result = '{:032b}'.format(1)
            return result
        elif reg_2[0] == '1' and reg_1[0] == '0':
            result = '{:032b}'.format(0)
            return result
        elif reg_1 < reg_2:
            result = '{:032b}'.format(1)
            return result
        else:
            result = '{:032b}'.format(0)
            return result
    #------------------------------------------------------------------------------
    elif controlLine == "1100":
        result = bin(int(reg_1,2) | int(reg_2,2))
        result = list('{:032b}'.format(int(result,2)))
        for i in range(len(result)):
            if  result[i]== '0':
                result[i] = '1'
            else:
                result[i] = '0'
        result = ''.join(result)
        return result
#---------------------------------------------------------------------------------------------------------------------------
    elif controlLine == "1101":#sll
         for indexes in range(0,shiftAmount):
             reg_1 = reg_1[indexes+1:]
             reg_1 += '0'
         return reg_1
             
         
# #---------------------------------------------------------------------------------------------------------------------------
    elif controlLine == "1110":#srl
        for indexes in range(0,shiftAmount):
             reg_1 = '0' + reg_1
             reg_1 = reg_1[:len(reg_1) - (indexes+1)]
    
        return reg_1
# #---------------------------------------------------------------------------------------------------------------------------
#print(ALU("1110","1000000000000000000000000000001","01111111111111111111111111111010",5))