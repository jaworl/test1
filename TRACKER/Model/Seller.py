class seller :
    def __init__ (self , personID : int, name : str , lastname : str , nationalID : int , phone_number : int ) :
        self.personID = personID
        self.name = name
        self.lastName = lastname
        self.nationalID = nationalID
        self.phone_number = phone_number

    def get_personID (self) :
        return self.personID
    
    def set_personID (self,personID) :
        self.personID = personID 

    def get_name (self) :
        return self.name
    
    def set_name (self,name) :
        self.name = name

    def get_lastname (self) :
        return self.lastname
    
    def set_lastname (self,lastname) :
        self.lastname = lastname

    def get_nationalID (self) :
        return self.nationalID
    
    def set_nationalID (self,nationalID) :
        self.nationalID = nationalID

    def get_phone_number (self) :
        return self.phone_number
    
    def set_phone_number (self,phone_number) :
        self.phone_number = phone_number