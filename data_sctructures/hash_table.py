class HashTable:
    def __init__(self):
        self.table = [None] * 100

    def hash_function(self, key):
        return key % len(self.table)

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = value

    def get(self, key):
        index = self.hash_function(key)
        return self.table[index]


ha_tab = HashTable()
ha_tab.insert(1, "one")
ha_tab.insert(2, "two")
ha_tab.insert(3, "three")
ha_tab.insert(4, "four")
ha_tab.insert(5, "five")
ha_tab.insert(6, "six")
ha_tab.insert(7, "seven")
ha_tab.insert(8, "eight")
ha_tab.insert(9, "nine")
ha_tab.insert(145, "ten")

print(ha_tab.get(145))
