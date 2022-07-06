def CU ( instruction) :
    controlLine = {}
    controlLine ["opcode"          ] = '0000'
    controlLine ["i_type"          ] = '0'
    controlLine ["Memread"         ] = '0'
    controlLine ["Memwrite"        ] = '0'
    controlLine ["memtype"         ] = '000'
    controlLine ["MemToReg"        ] = '0'
    controlLine ["Jandlink"        ] = '0'
    controlLine ["register_select" ] = '0'
    controlLine ["Jandlink"        ] = '0'
    controlLine ["Regwrite"        ] = '0'
    controlLine ["j-type"          ] = '00'
    controlLine ["b_type"          ] = '00'
    
    
     
    controlLine
    command = instruction [0]
    do[command]()