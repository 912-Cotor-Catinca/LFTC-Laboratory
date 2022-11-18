from collections import deque


class HashTable:
    def __init__(self, size):
        self._size = size
        self.elements = [deque() for _ in range(size)]

    def getSize(self):
        return self._size

    def hash(self, key):
        sum_of_ascii = 0
        for character in key:
            sum_of_ascii += ord(character) - ord('0')
        return sum_of_ascii % self._size

    def contains(self, key):
        if key in self.elements[self.hash(key)]:
            return True
        return False

    def getPosition(self, key):
        current_pos = self.hash(key)
        return_index = 0
        for element in self.elements[current_pos]:
            if element != key:
                return_index += 1
            else:
                break
        return (current_pos, return_index)

    def add(self, key):
        if self.contains(key):
            return self.getPosition(key)
        current_pos = self.hash(key)
        self.elements[current_pos].append(key)
        return self.getPosition(key)

    def remove(self, key):
        if self.contains(key):
            current_pos = self.hash(key)
            self.elements[current_pos].remove(key)
            return True
        return False

    def __str__(self):
        result = ""
        for i in range(self._size):
            if self.elements[i]:
                result = result + str(i) + "->" + str(self.elements[i]) + "\n"
        return result


class SymbolTable:
    def __init__(self, size):
        self._hash_table = HashTable(size)

    def add(self, key):
        return self._hash_table.add(key)

    def remove(self, key):
        return self._hash_table.remove(key)

    def contains(self, key):
        return self._hash_table.contains(key)

    def getPosition(self, key):
        return self._hash_table.getPosition(key)

    def __str__(self):
        return str(self._hash_table)
