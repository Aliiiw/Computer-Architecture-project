ALU = {}

ALU["add"] = "0010"
ALU["sub"] = "0110"
ALU["addi"]= "0010"
ALU["lw"] =  "0010"
ALU["sw"] =  "0010"
ALU["lh"] = "0010"
ALU["lhu"]= "0010"
ALU["sh"] = "0010"
ALU["lb"] = "0010"
ALU["lbu"]= "0010"
ALU["sb"] = "0010"
ALU["and"]= "0000"
ALU["or"] = "0001"
ALU["andi"] = "0000"
ALU["ori"] = "0001"
ALU["nor"] = "1100"
ALU["sll"] = "1101"
ALU["srl"] = "1110"
ALU["beq"] = "0110"
ALU["bne"] = "0110"
ALU["slt"] = "0111" 
ALU["sltu"] = "1000"
ALU["slti"] = "0111"
ALU['j'] = '0000'
ALU['jr'] = '0000'
ALU['jal'] = '0000'

d = {}

d["i_type"] = ["addi","andi","ori","slti","srl","sll"]
d["i_type"] += ["lw","sw","lh","sh","lb","sb","lhu","lbu"]
d["Memread"] = ["lw","lh","lb","lhu","lbu"]
d["Memwrite"] = ["sw","sh","sb"]
d["Memtype0"] = ["sh","sb","lh","lb","lhu","lbu"]
d["Memtype1"] = ["sb","lb","lbu"]
d["Memtype2"] = ["lbu" , "lhu"]
d["Memtoreg"] = d["Memread"]
d["Jandlink"] = ["jal"]
d["Regwrite"] = ["add","sub","addi","jal"]
d["Regwrite"]+= ["lw","lh","lhu","lb","lbu"]
d["Regwrite"]+= ["and","or","andi","ori","nor"]
d["Regwrite"]+= ["sll","srl","slt","sltu","slti"]

d["register_select" ] = ["lw","lh","lhu","lb","lbu"]
d["register_select" ] += ["addi","andi","ori","slti"]

d["j_type0"] = ["j","jr","jal"]
d["j_type1"] = ["jr"]
d["b_type0"] = ["beq","bne"]
d["b_type1"] = ["bne"]

Lines  = ["i_type","Memread","Memwrite","Memtoreg","Jandlink"]
Lines += ["register_select","Regwrite"]

def CU ( instruction) :
    
    command = instruction [0]
    controlLine = {}
    controlLine ["i_type"          ] = '0'
    controlLine ["Memread"         ] = '0'
    controlLine ["Memwrite"        ] = '0'
    controlLine ["Memtype"         ] = '000'
    controlLine ["Memtoreg"        ] = '0'
    controlLine ["Jandlink"        ] = '0'
    controlLine ["register_select" ] = '0'
    controlLine ["Regwrite"        ] = '0'
    controlLine ["j_type"          ] = '00'
    controlLine ["b_type"          ] = '00'
    controlLine ["ALU"             ] = ALU[command]
    
    
    for Line in Lines :
        if (command in d[Line]):
            controlLine[Line] = '1'
            
    for Line in ["Memtype","j_type","b_type"]:
        i = 0
        s = ""
        while Line + str(i) in d :
            if command in d[Line+str(i)]:
              s+='1'
            else :
                s+='0'
            i+=1
        controlLine[Line] = s
    
    return controlLine