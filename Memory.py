def Memory(adres ,data, read , write , type) :
    if read == '1' :
        return Mem[adres]
    if write =='1':
        Memm[adres] =data 
    