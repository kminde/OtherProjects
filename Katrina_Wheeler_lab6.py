
class MyHashtable(object):

    def __init__(self, size): #Creates an empty hash table
        self.size = size

        #Create the list (of size) of empty lists(chaining)
        self.table = []
        for i in range(self.size):
            self.table.append([])

    def str(self): #for print
        return str(self.table)

    def insert(self, elem): #Adds an element into the hashtable
        hash = ord(elem[0]) % self.size
        self.table[hash].append(elem)

    def member(self, elem): #returns if element exists in hashtable
        hash = ord(elem[0]) % self.size
        return elem in self.table[hash]

    def delete(self, elem): #Removes an element from the hashtable
        hash = ord(elem[0]) % self.size
        self.table[hash].remove(elem)

#Testing code
s = MyHashtable(10)
s.insert("amy") #97
s.insert("chase") #99
s.insert("chris") #99
print(s.member("amy"))
print(s.member("chris"))
print(s.member("alyssa"))
s.delete("chase")
print(s.member("chris"))


class MyHashtable2(object):

    def __init__(self, size): #Creates a list of none values
        self.table = [None] * size
        self.status = ["Empty"] * size #Creates a second table for status
        self.size = size


    def str(self): #for print
        return str(self.table)

    def insert(self, elem): #Adds an element into the hashtable, loops list until empty value is found
        hash = ord(elem[0]) % self.size
        if self.table[hash] is None:
            self.table[hash] = elem
            self.status[hash] = "Filled"
        else:
            i = 1
            done = False
            while not done:
                new_hash = (hash + i) % len(self.table)
                if new_hash == hash:
                    raise ValueError("Hash table is full!")
                if self.table[new_hash] is None or self.table[new_hash] == elem:
                    self.table[new_hash] = elem
                    done = True
                    self.status[hash] = "Filled"
                else:
                    i += 1

    def hash(self, elem):
        return elem % len(self.table) #Modulo function

    def member(self, elem): #returns if element exists in hashtable
        hash = ord(elem[0]) % self.size
        if self.table[hash] == elem:
            return elem in self.table[hash]
        else:
            done = False
            i = 1
            while not done:
                new_hash = (hash + i) % len(self.table)
                if self.table[new_hash] == elem:
                    done = True
                    return elem in self.table[new_hash]
                else:
                    return "Value is not in hashtable"

    def delete(self, elem): #Removes an element from the hashtable
        hash = ord(elem[0]) % self.size
        self.table[hash] = None
        self.status[hash] = "Deleted"


#Testing code
s = MyHashtable2(10)
s.insert("amy") #97
s.insert("chase") #99
s.insert("chris") #99
print(s.member("amy"))
print(s.member("chris"))
print(s.member("alyssa"))
s.delete("chase")
print(s.member("chris"))