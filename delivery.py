
import route
import packages

# Initialize variables for total miles of each route
first_truck_miles = 0
second_truck_miles = 0
third_truck_miles = 0

# Lists for truck packages
truck_one = []
truck_two = []
truck_three = []

# Initialize time each truck starts delivering
first_truck_leaves = ['8:00:00']
second_truck_leaves = ['9:05:00']
third_truck_leaves = ['10:30:00']

# Initialize all start times for packages to the initial leave time of truck 1
# Space-Time Complexity: O(N)
for index, package_info in enumerate(packages.get_first_truck_packages()):
    packages.get_first_truck_packages()[index][9] = first_truck_leaves[0]
    truck_one.append(packages.get_first_truck_packages()[index])

# Compares packages from truck 1 to packages in distance address
# If the addresses match up, then set package distance index in package list
# equal to the address info index
# Space-Time Complexity: O(N^2)
for index, loaded_address in enumerate(truck_one):
    for address_info in route.get_address():
        if loaded_address[2] == address_info[2]:
            truck_one[index][1] = address_info[0]

# Calls greedy algorithm to determine shortest route for truck 1
# Space-Time: O(N^2)
route.create_route(truck_one, 1, 0)

# try and except block is here so that when the index does go out of range
# at index + 1 at the end, it doesn't break the function and simply passes
#
# calculates the total distance of truck 1 by
# calculating distance to each package from the shortest_route calculated
# sets the delivery time index of optimized list to calculated delivery time
# then updates the package in the hash map to contain this change
# Space-Time: O(N)
for index in range(len(route.truck_one_indices())):
    try:

        # Calculate current distance using indices
        row = int(route.truck_one_indices()[index])
        col = int(route.truck_one_indices()[index + 1])
        current_distance = route.distance_from_location(row, col)

        # calculate total distance truck traveled
        first_truck_miles = route.calc_total_dist(row, col, first_truck_miles)

        # calculate delivery time of package
        delivery_time = route.get_delivery_time(current_distance, first_truck_leaves)

        # put delivery time in list and update package in hash map
        route.truck_one_shortest()[index][10] = (str(delivery_time))
        packages.get_package_map().update_package(int(route.truck_one_shortest()[index][0]), truck_one)
    except IndexError:
        pass

# Initialize all start times for packages to the initial leave time of truck 2
# Space-Time Complexity: O(n)
for index, package_info in enumerate(packages.get_second_truck_packages()):
    packages.get_second_truck_packages()[index][9] = second_truck_leaves[0]
    truck_two.append(packages.get_second_truck_packages()[index])

# Compares packages from truck 2 to packages in distance address
# If the addresses match up, then set package distance index in package list
# equal to the address info index
# Space-Time Complexity: O(N^3)
for index, loaded_address in enumerate(truck_two):
    for address_info in route.get_address():
        if loaded_address[2] == address_info[2]:
            truck_two[index][1] = address_info[0]

# Calls greedy algorithm to determine shortest route for truck 2
# Space-Time: O(N^2)
route.create_route(truck_two, 2, 0)

# try and except block is here so that when the index does go out of range
# at index + 1 at the end, it doesn't break the function and simply passes
#
# calculates the total distance of truck 2 by
# calculating distance to each package from the shortest_route calculated
# sets the delivery time index of optimized list to calculated delivery time
# then updates the package in the hash map to contain this change
# Space-Time: O(N)
for index in range(len(route.truck_two_indices())):
    try:
        # Calculate current distance using indices
        row = int(route.truck_two_indices()[index])
        col = int(route.truck_two_indices()[index + 1])
        current_distance = route.distance_from_location(row, col)

        # calculate total distance truck traveled
        second_truck_miles = route.calc_total_dist(row, col, second_truck_miles)

        # calculate delivery time of package
        delivery_time = route.get_delivery_time(current_distance, second_truck_leaves)

        # put delivery time in list and update package in hash map
        route.truck_two_shortest()[index][10] = (str(delivery_time))
        packages.get_package_map().update_package(int(route.truck_two_shortest()[index][0]), truck_two)
    except IndexError:
        pass

# Initialize all start times for packages to the initial leave time of truck 3
# Space-Time Complexity: O(n)
for index, package_info in enumerate(packages.get_third_truck_packages()):
    packages.get_third_truck_packages()[index][9] = third_truck_leaves[0]
    truck_three.append(packages.get_third_truck_packages()[index])

# Compares packages from truck 3 to packages in distance address
# If the addresses match up, then set package distance index in package list
# equal to the address info index
# Space-Time Complexity: O(N^3)
for index, loaded_address in enumerate(truck_three):
    for address_info in route.get_address():
        if loaded_address[2] == address_info[2]:
            truck_three[index][1] = address_info[0]
            break

# Calls greedy algorithm to determine shortest route for truck 3
# Space-Time: O(N^2)
route.create_route(truck_three, 3, 0)

# try and except block is here so that when the index does go out of range
# at index + 1 at the end, it doesn't break the function and simply passes
#
# calculates the total distance of truck 3 by
# calculating distance to each package from the shortest_route calculated
# sets the delivery time index of optimized list to calculated delivery time
# then updates the package in the hash map to contain this change
# Space-Time: O(N)
for index in range(len(route.truck_three_indices())):
    try:
        row = int(route.truck_three_indices()[index])
        col = int(route.truck_three_indices()[index + 1])
        # Calculate current distance using indices
        current_distance = route.distance_from_location(row, col)

        # calculate total distance truck traveled
        third_truck_miles = route.calc_total_dist(row, col, third_truck_miles)

        # calculate delivery time of package
        delivery_time = route.get_delivery_time(current_distance, third_truck_leaves)

        # put delivery time in list and update package in hash map
        route.truck_three_shortest()[index][10] = (str(delivery_time))
        packages.get_package_map().update_package(int(route.truck_three_shortest()[index][0]), truck_three)
    except IndexError:
        pass


# returns total distance travelled by all 3 trucks
def total_miles_traveled():
    return sum([first_truck_miles, second_truck_miles, third_truck_miles])
