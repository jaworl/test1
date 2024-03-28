class time :
    def __init__(self, personID : int , shop_name : str , time_spent : int ,enter : int ):
        self.personID = personID
        self.shop_name = shop_name
        self.time_spent = time_spent
        self.enter = enter

    def get_personID (self) :
        return self.personID
    
    def set_personID (self,personID) :
        self.personID = personID 
    
    def get_shop_name (self) :
        return self.shop_name
    
    def set_shop_name (self,shop_name) :
        self.shop_name = shop_name 

    def get_time_spent (self) :
        return self.time_spent
    
    def set_time_spent(self,time_spent) :
        self.time_spent = time_spent 

    def get_enter (self) :
        return self.enter
    
    def set_enter(self,enter) :
        self.enter = enter 
