class Hash:
    size = 5

    def __init__(self):
        self._data = [None for _ in range(self.size)]

    def __getitem__(self, key):
        h = self.__get_hash(key)
        return self._data[h]

    def __setitem__(self, key, value):
        h = self.__get_hash(key)
        self._data[h] = value

    def __get_hash(self, name):
        return hash(name) % self.size

    def __len__(self):
        counter = 0
        for i in self._data:
            if i != None:
                counter += 1
        return counter


obj = Hash()
obj['key'] = 123
print(obj['key'])
print(len(obj))
print(obj[1])
