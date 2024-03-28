class floor :
    def __init__ (self , floorID : int , name :str , num_of_people : int ,  hall_name : str , shop_plate : str ) :
        self.floorID = floorID 
        self.name = name
        self.num_of_people = num_of_people
        self.hall_name = hall_name
        self.shop_plate = shop_plate

    def get_floorID (self) :
        return self.floorID
    
    def set_floorID (self,floorID) :
        self.floorID = floorID 

    def get_name (self) :
        return self.name
    
    def set_name (self,name) :
        self.name = name

    def get_num_of_people (self) :
        return self.num_of_people
    
    def set_num_of_people(self,num_of_people) :
        self.num_of_people = num_of_people

    def get_hall_name (self) :
        return self.hall_name
    
    def set_hall_name (self,hall_name) :
        self.hall_name = hall_name

    def get_shop_plate (self) :
        return self.shop_plate
    
    def set_shop_plate (self,shop_plate) :
        self.shop_plate = shop_plate

