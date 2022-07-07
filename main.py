import Assembler
import ALU
import RegisterFile
import Memory
import CU 



def select ( select_line , wire_a , wire_b ) :
    if bool(int(select_line)) == False :
        return wire_a
    if bool(int(select_line)) == True :
        return wire_b
    print("EROR INVALID SELECT_LINE")

def update_PC (PC,jtype,btype,ALU_OUT , instruction ,regdata) :
    PC += 4
    
    
    beq_bne = bool ( int (btype[1] ) )
    is_eq = (ALU_OUT == 32*'0')
    
    control_bt =  (beq_bne and not(is_eq)) or (not(beq_bne) and is_eq)  # XOR
    
    PC_b = select (control_bt,PC , PC + int ( instruction [-16 :]+'00', 2) )
    
    
    PC_j = select (jtype[1],int(instruction[-26:],2) , int(regdata,2))
    
    
    PC = select (btype[0] , PC,PC_b )
    PC = select (jtype[0] ,PC , PC_j)

    return PC


inputs = Assembler.FinalResults

PC = 0
while ( PC // 4 < len( inputs ) ) :
    print(PC)
    instruction = inputs[PC//4]

    regdata = RegisterFile.read(instruction [1][6:11] , instruction[1][11:16])
    
    controlLine = CU.CU (instruction)
    
    ALU_out = ALU.ALU( controlLine["ALU"] , regdata[:32] , select(controlLine['i_type'],regdata[32:], 16*'0' + instruction[1][16:]))

    Memory_out = Memory.Memory(ALU_out , regdata[32:] ,  controlLine["Memread"] , controlLine["Memwrite"] , controlLine["Memtype"])
    
    Registerin = select ( controlLine["Memtoreg"] , ALU_out , Memory_out)
    Registerin = select ( controlLine["Jandlink"] , Registerin , PC+4 )
    
    RegisterWrite = select (controlLine["register_select"] , instruction[1][16:21] , instruction [1][11 : 16 ] )
    RegisterWrite = select (controlLine["Jandlink" ] , RegisterWrite , "11111" )
    
    RegisterFile.write(controlLine["Regwrite"],RegisterWrite,Registerin)
    
    PC = update_PC(PC,controlLine["j_type"] , controlLine ["b_type"] , ALU_out , instruction[1] , regdata[:32])