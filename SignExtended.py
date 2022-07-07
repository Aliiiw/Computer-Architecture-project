class SignExtend:
    #-------------------------------------------------------------------------------------------------------------------

    def __init__(self, constant_address_Itype):
        self.constant_address_Itype = constant_address_Itype

    #-------------------------------------------------------------------------------------------------------------------
    # Extending an immediate to 32 bits
    def extending(self):
        toBeExtended= self.constant_address_Itype[0]
        while (len(self.constant_address_Itype) != 32):
            self.constant_address_Itype = toBeExtended + self.constant_address_Itype
        return self.constant_address_Itype



