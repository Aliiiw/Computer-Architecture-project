import psycopg2

host_name = "185.105.239.28"
database_name = "camputerArchitecture"
root_user = "aliiiw"
root_password = "qazwsx"
port_id = 5432


connection_to_database = psycopg2.connect(
    host=host_name,
    dbname=database_name,
    user=root_user,
    password=root_password,
    port=port_id
)

open_connection = connection_to_database.cursor()

sql_script = ""

open_connection.close()



def Memory(address ,data, read , write , Type) :
    
    signed = bool(int(Type[2]))
    
    size = [4 , 4 , 2 , 1][int(Type[:2])]
    address = int(address[:-size])
    
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