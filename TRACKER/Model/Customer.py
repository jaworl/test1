class customer :
    def __init__ (self , personID : int , number_of_visit : int , window_watching_shops : str , window_watching_time : int , last_visit : int , visited_shops : str , total_time_spent : int ) :
        self.personID = personID 
        self.number_of_visit = number_of_visit
        self.window_watching_shops = window_watching_shops
        self.window_watching_time = window_watching_time
        self.last_visit = last_visit
        self.visited_shops = visited_shops
        self.total_time_spent = total_time_spent

    def get_personID (self) :
        return self.personID
    
    def set_personID (self,personID) :
        self.personID = personID

    def get_number_of_visit (self) :
        return self.number_of_visit
    
    def set_number_of_visit (self,number_of_visit) :
        self.number_of_visit = number_of_visit

    def get_window_watching_shops (self) :
        return self.window_watching_shops
    
    def set_window_watching_shops (self,window_watching_shops) :
        self.window_watching_shops = window_watching_shops

    def get_window_watching_time (self) :
        return self.window_watching_time
    
    def set_window_watching_time (self,window_watching_time) :
        self.window_watching_time = window_watching_time

    def get_last_visit(self) :
        return self.last_visit
    
    def get_last_visit (self,last_visit) :
        self.last_visit = last_visit

    def get_visited_shops(self) :
        return self.visited_shops
    
    def get_visited_shops (self,visited_shops) :
        self.visited_shops = visited_shops

    def get_total_time_spent(self) :
        return self.total_time_spent
    
    def get_total_time_spent (self,total_time_spent) :
        self.total_time_spent = total_time_spent

    