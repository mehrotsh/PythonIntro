# Example:
jobs = {"David": "Professor", "Sahan": "Postdoc", "Shawn": "Grad student"}
print(jobs["Sahan"])
# output : Postdoc
# Can change in place
jobs["Shawn"] = "Postdoc"
print(jobs["Shawn"])
# Oupup : Postdoc
# Lists of keys and values
print(jobs.keys())
# Output : ['Sahan', 'Shawn', 'David'] # note order is diff
print(jobs.values())
# Output : ['Postdoc', 'Postdoc', 'Professor’]
print(jobs.items())
# Output : [('Sahan', 'Postdoc'), ('Shawn', 'Postdoc'), ('David', 'Professor')]

# A dictionary works with keys and values
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
phonebook[1]=78
print(phonebook)

# another way to implement Dictionary is

phonebook1 = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}
print(phonebook1)


# Iterating over dictionaries

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))


# Removing a value one can use del or pop

del phonebook["John"]
print(phonebook)

phonebook1.pop("John")
print(phonebook1)

#Add an entry

phonebook['Johny']=938477567
print(phonebook)

#See if a key is in dictionary
print("tested" in phonebook)

#To fech a value 

print(phonebook.get("tested"))

print(phonebook.get("tested","defaultVal"))



# defaultdict means that if a key is not found in the dictionary,
#  then instead of a KeyError being thrown, a new entry is created.
# The type of this new entry is given by the argument of defaultdict.

# somedict = {}
# print(somedict[3]) # KeyError

from collections import defaultdict

someddict = defaultdict(int)
someddict[0]=1
someddict[2]=3
print(someddict[0])
print(someddict[3])  # print int(), thus 0
print(someddict[8])
print(someddict[6])

#Update Map
print(jobs)
print(phonebook)

phonebook.update(jobs)

print(phonebook)
