#%%
""" DATA TYPES """

# TUPLES
dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])		# output: Bruce
#dog[1] = 'dachshund'	# ERROR: cannot be modified ('tuple' object does not support item assignment)

# LISTS
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']

# DICTIONARIES
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists
new_person['hobbies'] = ['climbing', 'coding']	# adds a key-value pair if the key doesn't exist
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}


""" CONDITIONAL STATEMENTS """
x = 12
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")
# because x is not greater than 50, the second print statement is the only one that will execute

x = 55
if x > 10:
    print("bigger than 10")
elif x > 50:
    print("bigger than 50")
else:
    print("smaller than 10")
# even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'

if x < 10:
    print("smaller than 10")
# nothing happens, because the statement is false   


""" LOOPS """
# FOR loops through Lists
my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(str(i) + ": ", str(my_list[i]))

# FOR loops through Dictionaries
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])

# another way to iterate through the keys
capitals = {"france": "paris", "usa": "washington dc", "belgium": "brussels", "ethiopia": "addis ababa"}
for key in capitals.keys():
    print(key)
print("BREAK")

#to iterate through the values
for val in capitals.values():
    print(val)
print("BREAK")

#to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)


count = 0
while count < 5:
    print("looping - ", count)
    count += 1

#while <expression>:
    # do something, including progress towards making the expression False. Otherwise we'll never get out of here!

y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")

for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r

for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
    print("Final else statement")
# output: 3, 2, 1


"""

LECTURE 1-12-21
"""
#%%
my_list = [1,2,3,4,5,6,7,8]
for i in range(len(my_list)):
    print(my_list[i])

bird = {
    'feathers':'blue',
    'wings':2,
    'name':'floppy'
}

for thing in bird:
    print(thing, bird[thing])
# %%
player = {'first_name': 'Michael', 'last_name': 'Jordan'}

students = ['a', 'b', 'c', 'd']
# Indices    0    1    2    3

#
# IN JavaScript
# if(bird['feathers'] == 'blue'){
#       console.log('it's a blue bird")}

# PYTHON
# 
# pl = list(player)
# #print(pl)

# my_list = [1,2,3,4,5,6,7,8,]

# for i in range(len(my_list)):
#     print(my_list[i])

bird = {
    'feathers':'blue',
    'wings':2,
    'name':'floppy',
    'friends': ["Tom", "Tweety", "Woodie"]
}

for thing in bird:
    print(thing, bird['friends'])
