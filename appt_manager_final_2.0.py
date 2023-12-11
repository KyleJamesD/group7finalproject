










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
            print ("Client Name         Phone          Day       Start     End       Type")# top menu bar for Calender will display on toosday
            print ("-------------------------------------------------------------------------------------")
            show_appointment_by_name(name_option)
        elif menu_option == '3':
            print('**Print calender for a specific day **')
            day = input('Enter Day of the week:')
            print(f'Appointments for {day.capitalize()}\n')
            print ("Client Name         Phone          Day       Start     End       Type")# top menu bar for Calender will display on toosday
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