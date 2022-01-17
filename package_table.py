
class PackageMap:

    # Initializes map and appends empty lists to self.map to store information
    def __init__(self, size=40):
        self.map = []
        self.size = size
        for _ in range(size):
            self.map.append([])

    # Returns size of map
    def get_size(self):
        return self.size

    # Function creates a package hash key
    # using key % len(map) to determine placements
    # Space-Time Complexity: O(1)
    def create_package_key(self, key):
        return int(key) % self.get_size()

    # Insert package into hash table
    # Space-Time Complexity: O(1)
    def insert_package(self, key, value):
        package_key = self.create_package_key(key)
        key_value_pair = [key, value]

        # maps key-value pair to hash map if empty
        if self.map[package_key] is None:
            self.map[package_key] = list(key_value_pair)

            return

        # inserts package pair to given key
        # Space-Time Complexity: O(1)
        else:
            for pair in self.map[package_key]:
                if pair[0] == key:
                    pair[1] = key_value_pair
                    return
            self.map[package_key].append(key_value_pair)
            return

    # Updates a package in the hash table
    # Space-Time Complexity: O(1)
    def update_package(self, key, value):
        hash_key = self.create_package_key(key)
        if self.map[hash_key] is not None:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    pair[1] = value
                    return

    # returns package info from a given key in the hash table
    # Space-Time Complexity: O(1)
    def get_package_info(self, key):
        hash_key = self.create_package_key(key)
        if self.map[hash_key] is not None:
            for pair in self.map[hash_key]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Removes a package from the hash table at a given key
    # Space-Time Complexity: O(N)
    def remove_package(self, key):
        package_key = self.create_package_key(key)

        if self.map[package_key] is None:
            return
        for i in range(0, len(self.map[package_key])):
            if self.map[package_key][i][0] == key:
                self.map[package_key].pop(i)
                return
        return
