import psycopg2, psycopg2.extras

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
port=port_id)

open_connection = connection_to_database.cursor(cursor_factory=psycopg2.extras.DictCursor)

sql_insert_script = "insert into dataMemory (address,  string_data) values(%s, %s);"
sql_select_script = "select * from dataMemory;"
insert_value = (2, '87654321')
#open_connection.execute(sql_insert_script, insert_value)
sql_update_script = "update dataMemory set string_data = %s where address = %s"
update_value = ('00000000', 1)
open_connection.execute(sql_update_script, update_value)

#open_connection.execute(sql_select_script)
#result = open_connection.fetchall()

# for record in result:
#     address = record['address']
#     string_data = record['string_data']
#     print(address, string_data)


connection_to_database.commit()


open_connection.close()
    
def Memory(address ,data, read , write , Type) :
    
    # host_name = "185.105.239.28"
    # database_name = "camputerArchitecture"
    # root_user = "aliiiw"
    # root_password = "qazwsx"
    # port_id = 5432
    
    # connection_to_database = psycopg2.connect(
    # host=host_name,
    # dbname=database_name,
    # user=root_user,
    # password=root_password,
    # port=port_id)

    # open_connection = connection_to_database.cursor()

    # sql_insert_script = "insert into dataMemory values(default, %s, %s);"
    # sql_select_script = "insert into dataMemory values(default, %s, %s);"
    # insert_value = ('default', 1, '12345678')
    # open_connection.execute(sql_insert_script, insert_value)
    # connection_to_database.commit()

    #open_connection.close()
    
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
    
    if write == '1':
        for i in range(size) :
            DB [address + i ] = data [i*8:i*8+8]
        for i in range(size-1,-1,-1) :
            DB [address + i ] = data [-(i+1)*8 :- (i)*8]