import Assembler
import ALU
import RegisterFile
import Memory
import CU 



def select ( select_line , wire_a , wire_b ) :
    if select_line =='0' :
        return wire_a
    if select_line =='b' :
        return wire b
    print("EROR INVALID SELECT_LINE")

def update_PC (PC,jype,btype,ALU_OUT , instruction ,regdata) :
    PC += 4
    
    
    bne_beq = bool ( int (btype[1] ) )
    is_eq = (ALU_OUT == 32*'0')
    
    control_bt =  (bne_bqe and not(is_eq)) or (not(bne_bqe) and is_eq)  # XOR
    
    PC_b = select (control_bt,PC , PC + int ( instruction [-16 :]+'00', 2) )
    
    
    PC_j = select (jtype[1],int(instruction[-26:]) , int(regdata))
    
    
    PC = select (btype[0] , PC,PC_b )
    PC = select (jtype[0] ,PC , PC_j)









inputs = Assembler.FinalResults

PC = 0
while ( PC // 4 < len( inputs ) ) :
    
    instruction = inputs[PC//4]

    regdata = RegisterFile.read(instruction [1][6:11] , instruction[1][11:16])
    
    controlLine = CU.CU (instruction)
    
    ALU_out = ALU.ALU( controlLine["opcode"] , regdata[:32] , select(controlLine['i_type'],reg[32:],instruction[16:])S)
    

    Memory_out = Memory.Memory(ALU_out , regdata[32:] ,  controlLine["Memread"] , controlLine["Memwrite"] , controlLine["memtype"])
    
    Registerin = select ( controlLine["MemToReg"] , ALU_out , Memory_out)
    Registerin = select ( controlLine["Jandlink"] , Registerin , PC+4 )
    
    RegisterWrite = select (controlLine["register_select"] , instruction[1][11:16] , instruction [1][16 : 21 ] )
    RegisterWrite = select (controlLine["Jandlink" ] , RegisterWrite , "11111" )
    
    RegisterFile.write(controlLine["Regwrite"],RegisterWrite,Registerin)
    
    PC = update_PC(PC,controlLine["j-type"] , controlLine ["b_type"] , ALU_out , instruction[1] , regdata[:32])
    
        