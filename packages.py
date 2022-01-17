# This file sorts all packages into the 3 trucks
# based on information given for the packages
# in the package_info file.
# It then also maps these packages into the hash_map
# with package ID as the key and the information as the value
# Includes getter functions to retrieve truck lists for corresponding trucks.

import csv
from package_table import PackageMap

# sets size equal to number of packages in file data
# Space-Time: O(N)
size = 0
with open('./package_data/package_info.csv') as package_size:
    size = len(list(package_size))

# open package info file and split the information for use
# Space-Time: O(N)
with open('./package_data/package_info.csv') as package_data:
    package_details = csv.reader(package_data, delimiter=',')
    # Creates instance of hash map with size
    # initialize three truck package lists
    package_map = PackageMap(size)
    first_truck = []
    second_truck = []
    third_truck = []

    # Insert values from csv file into key/value pairs of the hash table: O(n)
    for item in package_details:
        package_id = item[0]
        distance_index = ""
        address = item[1]
        city = item[2]
        state = item[3]
        zip_code = item[4]
        delivery = item[5]
        size = item[6]
        note = item[7]
        delivery_start = ""
        delivery_status = "At hub."

        # puts all package info together in a list
        package_info = [package_id, distance_index, address, city, state, zip_code, delivery, size,
                        note, delivery_start, delivery_status]

        # The following conditional statements determine what packages go
        # into corresponding trucks based on requirements for packages
        if package_info[0] == '19':
            first_truck.append(package_info)

        if '84104' in package_info[5] and '10:30' not in package_info[6]:
            third_truck.append(package_info)
        # Puts package 9 with wrong address in third truck
        # which leaves past 10:20
        elif 'Wrong' in package_info[8]:
            third_truck.append(package_info)

        if 'EOD' not in package_info[6]:
            if 'Must' in package_info[8] or 'NA' in package_info[8]:
                first_truck.append(package_info)

        if 'truck 2' in package_info[8] or 'Delayed on flight' in package_info[8]:
            second_truck.append(package_info)

        # Checks remaining packages.
        # Inserts packages according to amount of packages on trucks
        # this ensures trucks package counts are evened out and do not
        # exceed 16 packages
        # O(N)
        if package_info not in first_truck and package_info not in second_truck and package_info not in third_truck:
            if len(first_truck) < len(second_truck):
                if len(first_truck) < len(third_truck):
                    first_truck.append(package_info)
                else:
                    third_truck.append(package_info)
            elif len(second_truck) < len(third_truck):
                second_truck.append(package_info)
            else:
                third_truck.append(package_info)

        # Inserts (key, value) pair into hash map
        # O(N)
        package_map.insert_package(package_id, package_info)

    # getter functions to return truck package information
    def get_first_truck_packages():
        return first_truck


    def get_second_truck_packages():
        return second_truck


    def get_third_truck_packages():
        return third_truck


    def get_package_map():
        return package_map
