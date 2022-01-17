import csv
import datetime

# Constant speed trucks travel
MILES_PER_HOUR = 18

# Convert CSV files into lists of miles and address information
# Space-Time O(N) for each conversion
with open('./package_data/miles.csv') as miles_file:
    miles = list(csv.reader(miles_file, delimiter=','))
with open('./package_data/address_file.csv') as address_file:
    address = list(csv.reader(address_file, delimiter=','))


# Calculate the distance from truck to location of delivery
# uses row, col indices given to find the distance
# if the value is "" then inverts to find a value
# This is due to the data in miles being bi-directional
# this way if row, col is blank then col, row will be
# the distance we were looking for
# Space-Time-Complexity: O(1)
def distance_from_location(row, col):
    current_distance = miles[row][col]
    if current_distance == "":
        current_distance = miles[col][row]

    return float(current_distance)


# This function calculates the total distance traveled
# adds the new distance to total given
# the row, col inversion works for the same reason
# as the function above this one
# Space-Time Complexity: O(1)
def calc_total_dist(row, col, total):
    current_distance = miles[row][col]
    if current_distance == "":
        current_distance = miles[col][row]
    total_distance = total + float(current_distance)
    return total_distance


# This function returns a delivery time
# It does so by calculating the time in hours
# then converts this to minutes
# followed by using datetime.timedelta()
# in order to add the times together and then return the total time
# Space-Time Complexity: O(N)
def get_delivery_time(distance_traveled, list_of_times):
    time_in_hours = distance_traveled / MILES_PER_HOUR
    time_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(time_in_hours * 60, 60))
    delivery_time = time_in_minutes + ':00'
    list_of_times.append(delivery_time)
    delivery_time = datetime.timedelta()
    for time in list_of_times:
        (hours, minutes, seconds) = time.split(':')
        delivery_time += datetime.timedelta(hours=int(hours),
                                            minutes=int(minutes), seconds=int(seconds))
    return delivery_time


# Create empty truck lists to fill with optimized
# route in the create_route function below
first_truck = []
second_truck = []
third_truck = []

# lists of location indices for the locations
# each truck travels to on the optimized path
# first element is 0 to indicate starting at hub
first_truck_indices = ['0']
second_truck_indices = ['0']
third_truck_indices = ['0']


# getter functions to return location indices traveled to
# Space-Time Complexity: O(N) for each function
def truck_one_indices():
    return first_truck_indices


def truck_two_indices():
    return second_truck_indices


def truck_three_indices():
    return third_truck_indices


# getter functions to return optimized truck package lists
# Space-Time Complexity: O(N) for each function
def truck_one_shortest():
    return first_truck


def truck_two_shortest():
    return second_truck


def truck_three_shortest():
    return third_truck


# This function is the Greedy algorithm that uses the current location and next location
# to optimize and find the shortest path between each package in a truck
# The algorithm determines the shortest distance from the current location
# to its next destination for each package.
# It then appends packages to the appropriate list once it has determined
# that the package is the closest to the current location the truck is at.
#
# It will recursively call itself with the initial list that has the inserted
# packages popped from the list. This recursively calls until the base case is met
# which is when the list is empty
# Space-Time Complexity: O(N^2)

def create_route(package_list, truck_number, curr_location):
    # base case - ends if list is empty
    if len(package_list) < 1:
        return package_list

    # initialize lowest_value to infinite so that first value
    # checked is set as the lowest value for further checks
    lowest_value = float('inf')
    location = 0

    # Loops through packages and compares distances calculated
    # to current lowest value and sets a new lowest value
    # if the distance is lower
    for package in package_list:
        destination = int(package[1])
        if distance_from_location(curr_location, destination) <= lowest_value:
            lowest_value = distance_from_location(curr_location, destination)
            location = destination

    # loops through packages and checks if the distance is equal to the lowest value
    # then takes truck number passed through function to determine which truck to append package to
    # adds package with lowest distance to truck list, adds the index value to indices list
    # pops package from list and sets new current location then calls function with new values
    for package in package_list:
        if distance_from_location(curr_location, int(package[1])) == lowest_value:
            if truck_number == 1:
                first_truck.append(package)
                first_truck_indices.append(package[1])
                package_list.pop(package_list.index(package))
                curr_location = location
                create_route(package_list, 1, curr_location)
            elif truck_number == 2:
                second_truck.append(package)
                second_truck_indices.append(package[1])
                package_list.pop(package_list.index(package))
                curr_location = location
                create_route(package_list, 2, curr_location)
            elif truck_number == 3:
                third_truck.append(package)
                third_truck_indices.append(package[1])
                package_list.pop(package_list.index(package))
                curr_location = location
                create_route(package_list, 3, curr_location)


# Returns Package Address List
# Space-Time Complexity: O(N)
def get_address():
    return address
