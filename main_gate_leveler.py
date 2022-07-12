import Assembler
import ALU
import RegisterFile
import Memory
import CU 



def select ( select_line , wire_a , wire_b ) :
    select = bool(int(select_line))
    wire_a = [x=='1' for x in wire_a]
    wire_b = [x=='1' for x in wire_b]
    return   [str(int((not(select) and wire_a[i]) or (select and wire_b[i]))) for i in range(min(len(wire_a),len(wire_b)))]
    
#    if bool(int(select_line)) == False :
#        return wire_a
#    if bool(int(select_line)) == True :
#        return wire_b
#    print("EROR INVALID SELECT_LINE")

def update_PC (PC,jtype,btype,ALU_OUT , instruction ,regdata) :
    bin (int(PC,2) + 4 )[2:]
    
    
    beq_bne = bool ( int (btype[1] ) )
    is_eq = (ALU_OUT == 32*'0')
    
    control_bt =  (beq_bne and not(is_eq)) or (not(beq_bne) and is_eq)  # XOR
    
    
    if (instruction[16] == '1' ) :
        PC_b = select (control_bt,PC ,bool(int( PC[:-2],2) + (int ( instruction [-16 :] ,2 ) - 2**16)*4)[2:])
    else:
        PC_b = select (control_bt,PC ,bool( int(PC,2) + int ( instruction [-16 :]+'00', 2))[2:] )
    
    if (jtype[1]=='1' and jtype[0] =='1'):
        print("regdata: " , regdata)
    PC_j = select (jtype[1],instruction[-26:],2 , regdata)
    if jtype[1] == '0' :
        print("jump palce : "  ,int(instruction[-26:],2))
        
    
    PC = select (btype[0] , PC,PC_b )
    PC = select (jtype[0] ,PC , PC_j)
    if PC 
    return PC


inputs = Assembler.FinalResults

PC = 32*'0'
while ( int(PC[:-2]) < len( inputs ) ) :
    PC_line = bin(int(PC,2)+4)[2:]
    PC_line = (32- len(PC_line))*'0' + PC_line
    
    instruction = inputs[int(PC,2)]
    print("PC: ",PC,"instruction: ", instruction[0])
    regdata = RegisterFile.read(instruction [1][6:11] , instruction[1][11:16])
    
    controlLine = CU.CU (instruction)
    
    ALU_out = ALU.ALU( controlLine["ALU"] , regdata[:32] , select(controlLine['i_type'],regdata[32:], 16*'0' + instruction[1][16:]))
    print("ALU_OUT : " , ALU_out)
    Memory_out = Memory.Memory(ALU_out , regdata[32:] ,  controlLine["Memread"] , controlLine["Memwrite"] , controlLine["Memtype"])
    
    Registerin = select ( controlLine["Memtoreg"] , ALU_out , Memory_out)
    Registerin = select ( controlLine["Jandlink"] , Registerin , PC_line )
    #if (controlLine["Jandlink"]=='1' ):
    #    print("Registerin: ",Registerin)
    RegisterWrite = select (controlLine["register_select"] , instruction[1][16:21] , instruction [1][11 : 16 ] )
    RegisterWrite = select (controlLine["Jandlink" ] , RegisterWrite , "11111" )
    
    RegisterFile.write(controlLine["Regwrite"],RegisterWrite,Registerin)
    #print("Regwrite: ", controlLine["Regwrite"])
    PC = update_PC(PC,controlLine["j_type"] , controlLine ["b_type"] , ALU_out , instruction[1] , regdata[:32])
