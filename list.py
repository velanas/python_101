a = 10 # integer
b = 10.2 # float
c = a + b # addition
d = "hello" # string

#list
e = [1, 1, 3, 4, 5] # list
f = [1.3, 1.5, 3.9, 4.61, 5.36] # list of floats
g = ["hello","world"] # list of strings
h = [] # empty list

#list constructor
i = list(range(1,11)) # list from 1 to 10
# slicing list from 1 to 4 not including 4
print (f[1:4])

x = []
x.append(5)
print("After appending 5:", x)
x.append(10)
print("After appending 10:", x)

x.insert(1,15)
print("After inserting 15 at index 1:", x)

x.extend([20,25,30])
print("After extending with [20,25,30]:", x)

x.remove(15)
print("After removing 15:", x)

z = x.pop(1)
print("After popping index 1:", x)
print(z, "was removed from the list")

del x[0]
print("After deleting index 0:", x)

x.clear()
print("After clearing the list:", x)