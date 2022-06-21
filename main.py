import numpy
import InstructionMemory
import PC

address = []
a = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
i = 0
ClockCycle = 0
file = open("instructions.txt", "r")
for each in file: 
    if(each!='\n'):
        address.append(each)
file.close()

pc = "00000000000000000000000000000000"
while(True):

    i = int(pc,2)
    i = i // 4

    ins="00000000000000000000000000000000"
    instruction = InstructionMemory.InstructionMemory(ins, a, ClockCycle, pc).fetch()
    ClockCycle += 1
    for j in range(5):
        print(a[j][0],a[j][1])
    print(ClockCycle)
    print('\n\n')
    if (instruction == "Undefined opcode"):
        print("Undefined opcode")
        break
    elif(instruction == "J"):
        pc = a[0][5]
    elif(instruction != "Nope"):
        pc = PC.PC(pc).PC_Add_By_four()