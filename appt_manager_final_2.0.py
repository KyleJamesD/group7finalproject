from appointment import Appointment

calender= []

def create_weekly_calender():  
    working_days = ["monday","tuesday","wednesday","thursday","friday","saturday"]
    working_hours = [9,10,11,12,13,14,15,16]
    for day in working_days: # for each day make an object with each hour from the hour list
        for hour in working_hours: # for each hour make an object with appintment class pass day and hour as Arguments
            obj = Appointment(day, hour)
            calender.append(obj) # append each object to one big list. Makes 48 Objects

def find_appointment_by_time(day,time):
    target_day = day
    target_time = time
    matching_object = None
    # Search for a matching object
    for obj in calender: # if object day attribute and time attribute are true - return that object
        if obj.get_day_of_week() == target_day and obj.get_start_time_hour() == target_time:
            matching_object = obj
            return matching_object
    else:
        return None # If a match is not found return None
    
def show_appointment_by_name (name):
    target_name = name.lower() # makes string lower case 
    found_appointments = False
    for obj in calender:
        if  target_name in obj.get_client_name().lower():
            print(obj.__str__())
            found_appointments = True
        
    if not found_appointments:
            print('No appointments found.')


def show_appointments_by_day (day):
    target_day = day
    for obj in calender:
        if obj.get_day_of_week().lower().strip() == target_day: 
            print(obj.__str__())


def print_menu():
    while True:
        print("\n\nJojo's Hair Salon Appointment Manager")
        print("=" * 37,)
        print(" 1) Schedule an appointment")
        print(" 2) Find appointment by name")
        print(' 3) Print Calendar for a specific day')
        print(' 4) Cancel an appointment ')
        print(' 9) Exit the system')
        menu_option = (input("Enter your selection:"))
        print ('')
        if menu_option == "1":
            schedule_appointments()
        elif menu_option == '2':
            print('** Find appointment by name **')
            name_option = input('Enter Client Name:')
            print(f'Appointments for {name_option}')
            print ("Client Name         Phone          Day       Start     End       Type")# top menu bar for Calender will display on any day
            print ("-------------------------------------------------------------------------------------")
            show_appointment_by_name(name_option)
        elif menu_option == '3':
            print('**Print calender for a specific day **')
            day = input('Enter Day of the week:')
            print(f'Appointments for {day.capitalize()}\n')
            print ("Client Name         Phone          Day       Start     End       Type")# top menu bar for Calender will display on any day 
            print ("-------------------------------------------------------------------------------------")
            show_appointments_by_day(day.lower())
        elif menu_option == '4':
            print('**Cancel an appointment **')
            canceled_day = input("What day:")
            canceled_hour = int(input('Enter start hour (24 hour clock):'))
            obj = find_appointment_by_time(canceled_day.lower(),canceled_hour)
            if obj == None:
                print('Sorry that time slot is not in the weekly Calender!')
            elif obj.get_client_name() != "":
                print (f'Appointment: {obj.get_day_of_week()} {obj.get_start_time_hour()}:00 - {obj.get_start_time_hour() + 1}:00 for {obj.get_client_name()} has been cancelled!\n')
                obj.cancel()
            else:
                print ('That time slot isnt booked and doesnt need to be cancelled!')
        elif menu_option == '9':
            save_scheduled_appointments()
        else:
            print ("Invalid input")


def load_scheduled_appointments():
        c = 1
        csv_filename=input('Enter Appointment filename:')
        apointments_loaded = 0
        while c > 0 :
            try:
            # Attempt to open and read the contents of the file
                with open(csv_filename, 'r') as file:
                    for line in file:
                        item = line.strip().split(',') # strips trailing white space uses comma as a delimeter and adds items in the line to a list called item
                        client_name = item[0] # takes index 0 item and assigns to variable
                        client_number = item[1] # takes index 1 item and assigns to variable
                        client_Atype = item[2] # takes index 2 item and assigns to variable
                        client_day = item[3] # takes index 3 item and assigns to variable
                        client_starthour = item[4] # takes index 4 item and assigns to variable
                        obj = find_appointment_by_time(client_day.lower(),int(client_starthour)) # calls the find appointment by day function and passes arguements day and start time. start time converted to int 
                        obj.schedule(client_name,(client_number),int(client_Atype)) # calls the schedule method and passes arguments to change objects attributes in calender list
                        apointments_loaded += 1
                        c=0
            except FileNotFoundError: # if file name is mispelled or file is not their will raise an error and execute following code block
                csv_filename=input(f"File not found. Re-enter appointment filename:")
        print(f'{apointments_loaded} previously scheduled apointments have been loaded')


def save_scheduled_appointments():
        print('** Exit the system **')
        save_appointments = input('Would you like to save all scheduled appointments to a file (Y/N)?')
        if save_appointments.lower() == "y":
            csv_filename=input('Enter Appointment filename:')
            appointments_saved = 0
            try: #Try to open the file name specified if file does not exist python will raise an error and our except block will execute
                open(csv_filename, 'r') # Open the file
                csvfile = open(csv_filename, 'r') # open the file but assign it to a variable (cannot not close file by file name?)
                csvfile.close() # Close the file because it already exists
                overwrite_file =  input('This file already exists. Do you want to overwrite it (Y/N)?') # Gives user the option to overwrite the existing File
                if overwrite_file.lower() == "y":
                    open(csv_filename, 'w').close()
                    csvfile = open(csv_filename, 'a')
                    for obj in calender:
                        if obj.get_client_name() != "":
                            write_string = obj.format_record()
                            csvfile.write(write_string)
                            appointments_saved += 1
                    csvfile.close() 
                    print(f'{appointments_saved} scheduled appointments have been successfully saved') 
                elif overwrite_file.lower() == "n":
                    csv_filename=input('Enter Appointment filename:')
                    open(csv_filename, 'w').close()
                    csvfile = open(csv_filename, 'a')
                    for obj in calender:
                        if obj.get_client_name() != "":
                            write_string = obj.format_record()
                            csvfile.write(write_string)
                            appointments_saved += 1
                csvfile.close()
                print(f'{appointments_saved} scheduled appointments have been successfully saved')
                print ('Good Bye!')
                quit()

                        # for line in file:
            except FileNotFoundError: #If file does not exists create a new file and append all saved apponintments by iterating through calender list and checking if Client name variable is not empty then append to csv file in the format suplied by the format_record() method in appointment class
                open(csv_filename, 'w').close()
                csvfile = open(csv_filename, 'a')
                for obj in calender:
                    if obj.get_client_name() != "":
                        write_string = obj.format_record()
                        csvfile.write(write_string)
                        appointments_saved += 1
            csvfile.close()
            print(f'{appointments_saved} scheduled appointments have been successfully saved')
            print ('Good Bye!')
            quit()
        
        else:
            print ('Good Bye!')
            quit()


def schedule_appointments():
    print('** Schedule an appointment**')
    day = input("What Day:")
    hour = int(input('Enter start hour(24 hour clock):'))
    obj = find_appointment_by_time(day.lower(),hour)
    if obj == None:
        print('Sorry that time slot is not in the weekly Calender!')
    elif obj.get_client_name() != "":
        print ('Sorry that time slot is booked already!')
    else:
        client_name_schedule = input('Client name:')
        client_phone_schedule = input('Client Phone:')
        print('Appointment Types \n1:Mens Cut 50$, 2:ladies Cut $80, 3:Mens Colouring $50, 4:Ladies Colouring $120')
        apointment_type_schedule = int(input('Type of Appointment:'))
        if apointment_type_schedule == 0: 
            obj.schedule(client_name_schedule,client_phone_schedule,apointment_type_schedule) # If statment is to ensure proper appointment type is selected, and integer value is input.
            print(f'OK, {client_name_schedule}\'s appointment is scheduled!')
        elif apointment_type_schedule == 1:
            obj.schedule(client_name_schedule,client_phone_schedule,apointment_type_schedule)
            print(f'OK, {client_name_schedule}\'s appointment is scheduled!')
        elif apointment_type_schedule == 2:
            obj.schedule(client_name_schedule,client_phone_schedule,apointment_type_schedule)
            print(f'OK, {client_name_schedule}\'s appointment is scheduled!')
        elif apointment_type_schedule == 3:
            obj.schedule(client_name_schedule,client_phone_schedule,apointment_type_schedule)
            print(f'OK, {client_name_schedule}\'s appointment is scheduled!')
        elif apointment_type_schedule == 4:
            obj.schedule(client_name_schedule,client_phone_schedule,apointment_type_schedule)
            print(f'OK, {client_name_schedule}\'s appointment is scheduled!')
        else:
            print ("Sorry that is not a valid appointment Type!")
    print_menu()


def main ():
    print('Starting the Appointment Manager System')
    create_weekly_calender()
    print('Weekly calendar created')
    menu_load_CSV = input('Would you like to load previouly scheduled appointments from a file (Y/N)?').lower()
    if menu_load_CSV == "y":
        load_scheduled_appointments()

    print_menu()

if __name__ == "__main__":#starts the program
    main()
