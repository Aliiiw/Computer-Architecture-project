# import ControlUnit
# data=[]
# file = open("dataMemory.txt", "r")
# for each in file: 
#     if(each!='\n'):
#         data.append(each[:32])
# file.close()
# class DataMemory:
#     def __init__(self,result,registerRd,controlKey,array,counter):
#         self.result=result
#         self.registerRd=registerRd
#         self.controlKey=controlKey
#         self.array=array
#         self.counter=counter
    
#     def hazard(self):
#         MEMWB.MEMWB(self.array,self.counter).call()
#         return 0
    
#     def DataMemory(self):
#         if(self.controlKey=="Sw"):
#             data[int(self.result,2)]=self.registerRd
#             F=open("dataMemory.txt","w")
#             for i in range(0,len(data)):
#                 F.write(str(data[i]))
#                 F.write('\n')
#             F.close()
#             self.array[3][0]=self.controlKey
#             self.array[3][1]="DataMemory"
#             return
        
#         if(self.controlKey=="Lw"):
#             self.array[3][0]=self.controlKey
#             self.array[3][1]="DataMemory"
#             self.array[3][2]=data[int(self.result,2)]
#             self.array[3][3]="00000000000000000000000000000000"
#             self.array[3][4]=self.registerRd
#             self.array[3][5]="00000000000000000000000000000000"
#             return
        
#         #if self.controlKey in ["None" , "Nope" , "Beq" , "Bne" ,"j" ] :
#             #self.array[3][0]=self.controlKey
#             #self.array[3][1]="DataMemory"
#             #return 
            
        
#         self.array[3][0]=self.controlKey
#         self.array[3][1]="DataMemory"
#         self.array[3][2]=self.result
#         self.array[3][3]="00000000000000000000000000000000"
#         self.array[3][4]=self.registerRd
#         self.array[3][5]="00000000000000000000000000000000"

