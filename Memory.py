def Memory(address ,data, read , write , Type) :
    
    signed = bool(int(Type[2]))
    
    size = [4 , 4 , 2 , 1][int(type[:2])]
    address = addres//size
    
    if read == '1' :
        
        Memdata = "" 
        for i in range(size) :
            Memdata += DB [address + i ]
        
        if signed :
            Memdata = 32-len(Memdata)*Memdata[0] + Memdata
        else :
            Memdata = 32-len(Memdata)*'0' + Memdata
    
        return Memdata
    
    if write =='1':
        for i in range(size) :
            DB [address + i ] = data [i*8:i*8+8]
        for i in range(size-1,-1,-1) :
            DB [address + i ] = data [-(i+1)*8 :- (i)*8]    