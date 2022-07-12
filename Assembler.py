commandsOpCodes = {

    "add" : "000000",
    "sub" : "000000",
    "addi": "001000",
    "lw"  : "100011",
    "sw"  : "101011",
    "lh"  : "100001",
    "lhu" : "100101",
    "sh"  : "101001",
    "lb"  : "100000",
    "lbu" : "100100",
    "sb"  : "101000",
    "and" : "000000",
    "or"  : "000000",
    "nor" : "000000",
    "andi": "001100",
    "ori" : "001101",
    "sll" : "000000",
    "srl" : "000000",
    "beq" : "000100",
    "bne" : "000101",
    "slt" : "000000",
    "sltu": "000000",
    "slti": "001010",
    "j"   : "000010",
    "jr"  : "000000",
    "jal" : "000011",
  
}

registersValue = {

   "zero": "00000",
    "at" : "00001" ,
    "v0" : "00010",
    "v1" : "00011",
    "a0" : "00100",
    "a1" : "00101",
    "a2" : "00110",
    "a3" : "00111",
    "t0" : "01000",
    "t1" : "01001",
    "t2" : "01010",
    "t3" : "01011",
    "t4" : "01100",
    "t5" : "01101",
    "t6" : "01110",
    "t7" : "01111",
    "s0" : "10000",
    "s1" : "10001",
    "s2" : "10010",
    "s3" : "10011",
    "s4" : "10100",
    "s5" : "10101",
    "s6" : "10110",
    "s7" : "10111",
    "t8" : "11000",
    "t9" : "11001",
    "k0" : "11010",
    "k1" : "11011",
    "gp" : "11100",
    "sp" : "11101",
    "s8" : "11110",
    "ra" : "11111",

}


def assembler(command, operator1, operator2, operator3):

    machineCode = ""

    if command == "add":
        machineCode += commandsOpCodes[command]
        machineCode += registersValue[operator2]
        machineCode += registersValue[operator3]
        machineCode += registersValue[operator1]
        machineCode += "00000100000"

    elif command == "sub":
        machineCode += commandsOpCodes[command]
        machineCode += registersValue[operator2]
        machineCode += registersValue[operator3]
        machineCode += registersValue[operator1]
        machineCode += "00000100010"
        
    elif command == "addi":
        machineCode += commandsOpCodes[command]
        machineCode += registersValue[operator2]
        machineCode += registersValue[operator1]
        binary =  bin(int(operator3))
        machineCode += (16 - len(binary[2::])) * "0" + binary[2::]

    elif command == "lw":
        machineCode += commandsOpCodes[command]
        machineCode += registersValue[operator3]
        machineCode += registersValue[operator1]
        binary =  bin(int(operator2))
        machineCode += (16 - len(binary[2::])) * "0" + binary[2::]

    elif command == "sw":
        machineCode += commandsOpCodes[command]
        machineCode += registersValue[operator3]
        machineCode += registersValue[operator1]
        binary =  bin(int(operator2))
        machineCode += (16 - len(binary[2::])) * "0" + binary[2::]

    elif command == "lh":
        machineCode += commandsOpCodes[command]
        machineCode += registersValue[operator3]
        machineCode += registersValue[operator1]
        binary =  bin(int(operator2))
        machineCode += (16 - len(binary[2::])) * "0" + binary[2::]

    elif command == "lhu":
        machineCode += commandsOpCodes[command]
        machineCode += registersValue[operator3]
        machineCode += registersValue[operator1]
        binary =  bin(int(operator2))
        machineCode += (16 - len(binary[2::])) * "0" + binary[2::]

    elif command == "sh":
        machineCode += commandsOpCodes[command]
        machineCode += registersValue[operator3]
        machineCode += registersValue[operator1]
        binary =  bin(int(operator2))
        machineCode += (16 - len(binary[2::])) * "0" + binary[2::]

    elif command == "lb":
        machineCode += commandsOpCodes[command]
        machineCode += registersValue[operator3]
        machineCode += registersValue[operator1]
        binary =  bin(int(operator2))
        machineCode += (16 - len(binary[2::])) * "0" + binary[2::]

    elif command == "lbu":
        machineCode += commandsOpCodes[command]
        machineCode += registersValue[operator3]
        machineCode += registersValue[operator1]
        binary =  bin(int(operator2))
        machineCode += (16 - len(binary[2::])) * "0" + binary[2::]

    elif command == "sb":
        machineCode += commandsOpCodes[command]
        machineCode += registersValue[operator3]
        machineCode += registersValue[operator1]
        binary =  bin(int(operator2))
        machineCode += (16 - len(binary[2::])) * "0" + binary[2::]

    elif command == "and":
        machineCode += commandsOpCodes[command]
        machineCode += registersValue[operator2]
        machineCode += registersValue[operator3]
        machineCode += registersValue[operator1]
        machineCode += "00000100100"
        
    elif command == "or":
        machineCode += commandsOpCodes[command]
        machineCode += registersValue[operator2]
        machineCode += registersValue[operator3]
        machineCode += registersValue[operator1]
        machineCode += "00000100101"

    elif command == "nor":
        machineCode += commandsOpCodes[command]
        machineCode += registersValue[operator2]
        machineCode += registersValue[operator3]
        machineCode += registersValue[operator1]
        machineCode += "00000100111"

    elif command == "andi":
        machineCode += commandsOpCodes[command]
        machineCode += registersValue[operator2]
        machineCode += registersValue[operator1]
        binary =  bin(int(operator3))
        machineCode += (16 - len(binary[2::])) * "0" + binary[2::]

    elif command == "ori":
        machineCode += commandsOpCodes[command]
        machineCode += registersValue[operator2]
        machineCode += registersValue[operator1]
        binary =  bin(int(operator3))
        machineCode += (16 - len(binary[2::])) * "0" + binary[2::]
        
    elif command == "sll":
        machineCode += commandsOpCodes[command]
        machineCode += registersValue[operator2]
        machineCode += registersValue[operator2]
        machineCode += registersValue[operator1]
        binary =  bin(int(operator3))[2::]
        if len(binary) < 5:
            binary = (5 - len(binary)) * "0" + binary
        machineCode += binary
        machineCode += "000000"

    elif command == "srl":
        machineCode += commandsOpCodes[command]
        machineCode += registersValue[operator2]
        machineCode += registersValue[operator2]
        machineCode += registersValue[operator1]
        binary =  bin(int(operator3))[2::]
        if len(binary) < 5:
            binary = (5 - len(binary)) * "0" + binary
        machineCode += binary
        machineCode += "000010"

    elif command == "beq":
        machineCode += commandsOpCodes[command]
        machineCode += registersValue[operator1]
        machineCode += registersValue[operator2]
        binary =  bin(int(operator3))
        machineCode += (16 - len(binary[2::])) * "0" + binary[2::]
        
    elif command == "bne":
        machineCode += commandsOpCodes[command]
        machineCode += registersValue[operator1]
        machineCode += registersValue[operator2]
        binary =  bin(int(operator3))
        machineCode += (16 - len(binary[2::])) * "0" + binary[2::]

    elif command == "slt":
        machineCode += commandsOpCodes[command]
        machineCode += registersValue[operator2]
        machineCode += registersValue[operator3]
        machineCode += registersValue[operator1]
        machineCode += "00000101010"

    elif command == "sltu":
        machineCode += commandsOpCodes[command]
        machineCode += registersValue[operator2]
        machineCode += registersValue[operator3]
        machineCode += registersValue[operator1]
        machineCode += "00000101011"

    elif command == "slti":
        machineCode += commandsOpCodes[command]
        machineCode += registersValue[operator2]
        machineCode += registersValue[operator1]
        binary =  bin(int(operator3))
        machineCode += (16 - len(binary[2::])) * "0" + binary[2::]

    elif command == "j":
        machineCode += commandsOpCodes[command]
        binary =  bin(int(operator1))
        machineCode += (26 - len(binary[2::])) * "0" + binary[2::]

    elif command == "jr":
        machineCode += commandsOpCodes[command]
        machineCode += registersValue[operator1]
        machineCode += "000000000000000001000"
        
    elif command == "jal":
        machineCode += commandsOpCodes[command]
        binary =  bin(int(operator1))
        machineCode += (26 - len(binary[2::])) * "0" + binary[2::]

        
    return machineCode


FinalResults = []

with open('input.txt') as file:  

    allString = file.read()
    updateString = allString.splitlines()
    
    for i in range(len(updateString)): 

        finalResult = []                                        
        instruction = updateString[i].split(" ")
        
        command = instruction[0].lower()                      
        registers = instruction[1].split(",")                                        

        operator1 = registers[0].lower()                                              
        operator2 = registers[1].lower()
        operator3 = registers[2].lower()
        
        if operator3[0] == '-' :
            operator3 = int(operator3)
            operator3 += 2**32
            operator3 = str(operator3)

        machineCode = assembler(command, operator1, operator2, operator3)
        finalResult += [command]
        finalResult += [machineCode]
        #print(finalResult)
        FinalResults += [finalResult]