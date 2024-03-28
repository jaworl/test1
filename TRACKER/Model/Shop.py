class shop :
    def __init__ (self , product_type : str , num_purchases : int , plate : str , floor : str , hall : str , window_visit_time : int , window_visit_person : int , name : str , sellerID : int , num_enterance : int , open_time : int , pick_time : int  ) :
        self.product_type = product_type
        self.num_purchases = num_purchases
        self.plate = plate
        self.floor = floor
        self.hall = hall
        self.window_visit_time = window_visit_time
        self.window_visit_person = window_visit_person
        self.name = name
        self.sellerID = sellerID
        self.num_enterance = num_enterance
        self.open_time = open_time
        self.pick_time = pick_time

    def get_product_type (self) :
        return self.product_type
    
    def set_product_type (self,product_type) :
        self.product_type = product_type

    def get_num_purchases (self) :
        return self.num_purchases
    
    def set_num_purchases (self,num_purchases) :
        self.num_purchases = num_purchases

    def get_plate (self) :
        return self.plate
    
    def set_plate (self,plate) :
        self.plate = plate

    def get_floor (self) :
        return self.floor
    
    def set_floor (self,floor) :
        self.floor = floor

    def get_hall (self) :
        return self.hall
    
    def set_hall (self,hall) :
        self.hall = hall

    def get_window_visit_time (self) :
        return self.window_visit_time
    
    def set_window_visit_time (self,window_visit_time) :
        self.window_visit_time = window_visit_time

    def get_window_visit_person (self) :
        return self.window_visit_person
    
    def set_window_visit_person (self,window_visit_person) :
        self.window_visit_person = window_visit_person

    def get_name (self) :
        return self.name
    
    def set_name (self,name) :
        self.name = name

    def get_sellerID (self) :
        return self.sellerID
    
    def set_sellerID (self,sellerID) :
        self.sellerID = sellerID

    def get_num_enterance (self) :
        return self.num_enterance
    
    def set_num_enterance (self,num_enterance) :
        self.num_enterance = num_enterance

    def get_open_time (self) :
        return self.open_time
    
    def set_open_time (self,open_time) :
        self.open_time = open_time

    def get_pick_time (self) :
        return self. pick_time
    
    def set_open_time (self, pick_time) :
        self. pick_time =  pick_time
