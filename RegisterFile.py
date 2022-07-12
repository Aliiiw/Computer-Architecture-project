
Registers = 32 * [ 32 * '0' ]

def read ( a , b ) :
    print("Read from Regs :" , a,b)
    print("Value: ",Registers[int(a,2)] + Registers [int(b,2)])
    return Registers [int(a,2)] + Registers [int(b,2)]

def write(write_control,RegisterWrite,Registerin) :
    if write_control == '1' and RegisterWrite != 5*'0':
        print("Write in " ,RegisterWrite,Registerin)
        Registers[int(RegisterWrite,2)] = Registerin
