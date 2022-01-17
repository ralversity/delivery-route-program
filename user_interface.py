import datetime
from packages import get_package_map
from delivery import total_miles_traveled


# User Interface function. Allows user to check packages at given times and exit the program.
def user_interface():
    # This is the display message that is shown when the user runs the program.
    print(f'A total of {int(total_miles_traveled())} miles was taken for deliveries.')

    # takes user input for a choice on what to do
    user_input = int(input(
        """Enter the corresponding number to choose what to do:
       1. Track a single package at a certain time 
       2. Track all packages at a certain time
       3. Quit program
       Enter Choice(1-3): """))

    # Checks for user to input 3 for quit
    while user_input != 3:

        # When user input is 1
        # Output info for a single package given package ID and Time
        # Space-Time Complexity: O(N)
        if user_input == 1:
            single_package()

        # When user input is 2
        # Output all package info for a user-given time
        # Space-Time Complexity: O(N)
        elif user_input == 2:
            all_packages()

        # when user inputs an invalid value
        # Restarts UI function
        else:
            print('Incorrect input. Please try again (1-3)')
            user_interface()
            break

    # Ends program when input is 3
    else:
        exit()


# Output info for a single package given package ID and Time
# Time Complexity: O(N)
def single_package():
    try:
        # Takes user-input for a package ID.
        # Re-prompts if user enters an invalid ID
        package_id = int(input(f'Enter a valid package ID (1-40): '))
        while package_id > 40 or package_id < 1:
            package_id = int(input('Invalid package id please enter a new package id (1-40): '))

        # Take user input for time wanting to be checked
        # set times equal to the times for the associated package id given
        departure_time = get_package_map().get_package_info(str(package_id))[9]
        arrival_time = get_package_map().get_package_info(str(package_id))[10]
        time = input('Enter a time (HH:MM:SS): ')

        if departure_time == '8:00:00':
            truck_number = '1'
        elif departure_time == '9:05:00':
            truck_number = '2'
        else:
            truck_number = '3'

        # Converts times using timedelta into HH:MM:SS format
        # to use for comparison operations
        (hours, minutes, seconds) = time.split(':')
        converted_time = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))
        (hours, minutes, seconds) = departure_time.split(':')
        converted_departure_time = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))
        (hours, minutes, seconds) = arrival_time.split(':')
        converted_arrival_time = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))

        # Checks if package is still at hub by comparing departure time
        # to the time given by user. If it is still at hub then it
        # sets delivery status to at hub and sets when it will leave
        # then prints package info for given ID
        if converted_departure_time >= converted_time:
            get_package_map().get_package_info(str(package_id))[10] = 'Package is at hub'
            get_package_map().get_package_info(str(package_id))[9] = 'Leaves hub at ' + departure_time
            print(
                f'\n\nPackage is on truck {truck_number}\n'
                f'Package ID: {get_package_map().get_package_info(str(package_id))[0]}\n'
                f'Address: {get_package_map().get_package_info(str(package_id))[2]}\n'
                f'City: {get_package_map().get_package_info(str(package_id))[3]}\n'
                f'State: {get_package_map().get_package_info(str(package_id))[4]}\n'
                f'Zip: {get_package_map().get_package_info(str(package_id))[5]}\n'
                f'Must be delivered by: {get_package_map().get_package_info(str(package_id))[6]}\n'
                f'Package weight: {get_package_map().get_package_info(str(package_id))[7]} lbs\n'
                f'Truck status: {get_package_map().get_package_info(str(package_id))[9]}\n'
                f'Delivery status: {get_package_map().get_package_info(str(package_id))[10]}\n'
            )

        # checks if package has left hub and check if package is not delivered
        # sets delivery status to out for delivery and sets when it left hub
        # then prints package info for given ID
        elif converted_departure_time <= converted_time:
            if converted_time < converted_arrival_time:
                get_package_map().get_package_info(str(package_id))[10] = 'Package is out for delivery'
                get_package_map().get_package_info(str(package_id))[9] = 'Left hub at ' + departure_time

                print(
                    f'\n\nPackage is on truck {truck_number}\n'
                    f'Package ID: {get_package_map().get_package_info(str(package_id))[0]}\n'
                    f'Address: {get_package_map().get_package_info(str(package_id))[2]}\n'
                    f'City: {get_package_map().get_package_info(str(package_id))[3]}\n'
                    f'State: {get_package_map().get_package_info(str(package_id))[4]}\n'
                    f'Zip: {get_package_map().get_package_info(str(package_id))[5]}\n'
                    f'Must be delivered by: {get_package_map().get_package_info(str(package_id))[6]}\n'
                    f'Package weight: {get_package_map().get_package_info(str(package_id))[7]} lbs\n'
                    f'Truck status: {get_package_map().get_package_info(str(package_id))[9]}\n'
                    f'Delivery status: {get_package_map().get_package_info(str(package_id))[10]}\n'
                )

            # Else case - Package has been delivered
            # sets delivery status to delivered with time of delivery
            # then prints package info for given ID
            else:
                get_package_map().get_package_info(str(package_id))[10] = 'Package was delivered at ' + arrival_time
                get_package_map().get_package_info(str(package_id))[9] = 'Left hub at ' + departure_time

                print(
                    f'\n\nPackage is on truck {truck_number}\n'
                    f'Package ID: {get_package_map().get_package_info(str(package_id))[0]}\n'
                    f'Address: {get_package_map().get_package_info(str(package_id))[2]}\n'
                    f'City: {get_package_map().get_package_info(str(package_id))[3]}\n'
                    f'State: {get_package_map().get_package_info(str(package_id))[4]}\n'
                    f'Zip: {get_package_map().get_package_info(str(package_id))[5]}\n'
                    f'Must be delivered by: {get_package_map().get_package_info(str(package_id))[6]}\n'
                    f'Package weight: {get_package_map().get_package_info(str(package_id))[7]} lbs\n'
                    f'Truck status: {get_package_map().get_package_info(str(package_id))[9]}\n'
                    f'Delivery status: {get_package_map().get_package_info(str(package_id))[10]}\n'
                )

    except ValueError:
        print('Invalid entry. Try again.')
        single_package()
        pass
    exit()


# Outputs all package info for a user-given time
# Space-Time Complexity: O(N)
def all_packages():
    departure_time = ''
    converted_departure_time = ''
    converted_arrival_time = ''
    arrival_time = ''

    try:
        print("If you would like to return to main menu please type: back")

        # takes user input for time
        time = input("Enter a time (HH:MM:SS):")

        # Allows user to go back if they did not mean to run this function
        if time.lower() == 'back':
            user_interface()
            exit()
        # splits time into hours, min and seconds
        # for comparisons using datetime.timedelta function
        (hours, minutes, seconds) = time.split(':')
        converted_time = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))

        # Finds start and end times of packages with [9] and [10] being delivery times
        # Uses timedelta function in order to compare times to determine delivery status
        # based off the user given time
        # Time Complexity O(N^2)
        for ID in range(1, 41):
            try:
                # get departure and arrival time for package
                departure_time = get_package_map().get_package_info(str(ID))[9]
                arrival_time = get_package_map().get_package_info(str(ID))[10]

                # splits departure and arrival times into hours minutes and seconds
                # then converts them into datetime.timedelta objects to be compared
                (hours, minutes, seconds) = departure_time.split(':')
                converted_departure_time = datetime.timedelta(hours=int(hours), minutes=int(minutes),
                                                              seconds=int(seconds))

                (hours, minutes, seconds) = arrival_time.split(':')
                converted_arrival_time = datetime.timedelta(hours=int(hours), minutes=int(minutes),
                                                            seconds=int(seconds))
            except ValueError:
                pass

            # Checks if package is still at hub by comparing departure time to user time
            # Prints out Package ID and delivery status for packages
            # that still remain at the hub
            if converted_departure_time >= converted_time:
                get_package_map().get_package_info(str(ID))[10] = 'Package is at hub'
                get_package_map().get_package_info(str(ID))[9] = 'Package Leaves hub at ' + departure_time

                print(
                    f'Package ID: {get_package_map().get_package_info(str(ID))[0]}, '
                    f'Delivery status: {get_package_map().get_package_info(str(ID))[10]}'
                )

            # Checks if package is out for delivery by comparing departure time to user time
            # Prints out Package ID and delivery status for packages that
            # are out for delivery
            elif converted_departure_time <= converted_time:
                if converted_time < converted_arrival_time:
                    get_package_map().get_package_info(str(ID))[10] = 'Package is out for delivery'
                    get_package_map().get_package_info(str(ID))[9] = 'Left hub at ' + departure_time

                    print(
                        f'Package ID: {get_package_map().get_package_info(str(ID))[0]}, '
                        f'Delivery status: {get_package_map().get_package_info(str(ID))[10]}'
                    )

                # Else case, package was delivered
                # Prints out Package Id and delivery status for packages that have been delivered
                # at given time
                else:
                    get_package_map().get_package_info(str(ID))[10] = 'Package was delivered at ' + arrival_time
                    get_package_map().get_package_info(str(ID))[9] = 'Left hub at ' + departure_time

                    print(
                        f'Package ID: {get_package_map().get_package_info(str(ID))[0]}, '
                        f'Delivery status: {get_package_map().get_package_info(str(ID))[10]}'
                    )

    # Checks for value error by user and restarts all_packages() function to try again
    except ValueError:
        print('Invalid input. Try again')
        all_packages()
    exit()
