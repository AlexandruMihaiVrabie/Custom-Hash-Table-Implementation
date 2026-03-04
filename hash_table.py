class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        total = 0
        for letter in string:
            total += ord(letter)

        return total

    def add(self, key, value):
        hashed_key = self.hash(key)

        if not hashed_key in self.collection:
            self.collection[hashed_key] = {key: value}
        else:
            self.collection[hashed_key][key] = value

    def remove(self, key):
        hashed_key = self.hash(key)

        if hashed_key in self.collection and key in self.collection[hashed_key]:
            del self.collection[hashed_key][key]

    def lookup(self, key):
        hashed_key = self.hash(key)

        if hashed_key in self.collection and key in self.collection[hashed_key]:
            return self.collection[hashed_key][key]
        else:
            return None


ht = HashTable()

print(ht.hash('golf'))

ht.add('golf', 'sport')
print(ht.collection[424])

ht.add('dear', 'friend')
ht.add('read', 'book')
print(ht.collection[412])

ht.remove('dear')
print(ht.collection[412])

print(ht.lookup('golf'))

ht.remove('golf')
print(ht.lookup('golf'))

ht.add('fcc', 'coding')
print(ht.lookup('cfc'))

ht.add('rose', 'flower')
print(ht.collection[441])

ht.add('cfc', 'chemical')
print(ht.collection[300])
