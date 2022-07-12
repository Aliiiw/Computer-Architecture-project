
Registers = 32 * [ 32 * '0' ]

def read ( a , b ) :
    print("Reg" , a,b , "REG RA")
    return Registers [int(a,2)] + Registers [int(b,2)]

def write(write_control,RegisterWrite,Registerin) :
    if write_control == '1' and RegisterWrite != 5*'0':
        Registers[int(RegisterWrite,2)] = Registerin
    if write_control == '1' and RegisterWrite == 5*'1' :
        print("RA", Registerin)