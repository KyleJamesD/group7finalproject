class Appointment:
    def __init__(self, day_of_week, start_time_hour): # This is called a constructor it is used to assign values to Private attributes
        self.__c_n = ""
        self.__c_num = ""
        self.__a_t = 0
        self.__d_o_w = day_of_week
        self.__s_t_h = start_time_hour

    #Getters, these are also called accesssors
    def get_client_name(self):
        return self.__c_n
    
    def get_client_phone(self):
        return self.__c_num

    def get_appt_type(self):
        return self.__a_t

    def get_day_of_week(self):
        return self.__d_o_w

    def get_start_time_hour(self):
        return self.__s_t_h
    

    def get_appt_type_desc(self): 

            if self.__a_t == 0:
                self.a_t_string = ("Availible")
                return self.a_t_string
            if self.__a_t == 1:
                self.a_t_string = ("Mens Cut")
                return self.a_t_string
            if self.__a_t == 2:
                self.a_t_string = ("Ladies Cut")
                return self.a_t_string
            if self.__a_t == 3:
                self.a_t_string = ("Mens Colouring")
                return self.a_t_string
            if self.__a_t == 4:
                self.a_t_string = ("Ladies Colouring")
                return self.a_t_string

    def get_end_time_hour(self):
        return self.__s_t_h + 1
    
    # Setters, these are also called mutators
    def set_client_name(self,new_c_n): 
        self.__c_n = new_c_n
    
    def set_client_phone(self,new_c_num): 
        self.__c_num = new_c_num

    def set_appt_type(self,new_a_t):  
        self.__a_t = new_a_t

    def schedule(self,client_name, client_phone, appt_type):
        self.__c_n = client_name
        self.__c_num = client_phone
        self.__a_t = appt_type

    def set_client_day(self,new_d_o_w): 
        self.__d_o_w = new_d_o_w

    def set_client_start(self,new_s_t_h):
        self.__s_t_h = new_s_t_h

    def cancel (self):
        self.__c_n = ""
        self.__c_num = ""
        self.__a_t = 0

    def format_record (self):
        return f"{self.__c_n},{self.__c_num},{self.__a_t},{self.__d_o_w},{self.__s_t_h}\n"
    
    def __str__(self):
            zeros = ":00"
            return (f'{str(self.__c_n):<20}{str(self.__c_num):<15}{str(self.__d_o_w.capitalize()):<10}{str(self.__s_t_h):>2}:00  -  {self.__s_t_h + 1}{zeros:<8}{str(self.get_appt_type_desc()):<15}') 






    




        





        
