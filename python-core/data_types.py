# 1. Variables

#In Python, a variable is a name that points to an object. It doesn't hold the value itself.

x = [1, 2, 3]  # x is a variable that points to a list object
y = x  # y will point to same list, not a copy

print(y)
print(id(x), id(y))  # id() returns the identity of an object
print(type(x))  # type() returns the type of an object

# 2. Mutable and Immutable Data Types

# mutable objects can be changed after they are created, while immutable objects cannot be changed after they are created.
# mutuables are list, dict and set
# immuatble are int, float, bool, str, tuple


s = "hello"
print(id(s))
s = s + " world"  # creates a new string object
print(id(s))  # id of s has changed

# nums = [1, 2]
# print(id(nums))
# nums.append(3)  # modifies the existing list object
# print(id(nums))  # id of nums has not changed

# 3.String str

name = "Bhavana"
print(name[0])  # indexing
print(name[-1])  # negative indexing
print(name[0:3])  # slicing
print(name.upper())  # string methods
print(name.lower())
print(name[::2])
#print(name[0] = "b")  # strings are immutable, this will raise an error

# String methods always return a new string. The original never changes:

text = "Data Science"
print(text.strip())
print(text.lower())
print(text.replace("Data", "Machine"))
print("p".join(["Python", "is", "fun"]))
print("=".join(["Python", "is", "fun"]))
print("a,b,c".split(","))

city = "Hamburg"
print(f"The city is {city}")  # f-string formatting

# 4 Lists

nums = [5, 2, 8]

# nums.append(1)        # [5, 2, 8, 1]      add one item at the end
# nums.extend([7, 9])   # [5, 2, 8, 1, 7, 9] add many
# nums.insert(0, 10)    # add at a position
# nums.pop()            # removes and returns the last item
# nums.remove(8)        # removes the first 8 found
# len(nums)

nums = [5, 2, 8]

nums.append(1)
print(nums)           # [5, 2, 8, 1]

nums.extend([7, 9])
print(nums)           # [5, 2, 8, 1, 7, 9]

nums.insert(0, 10)
print(nums)           # [10, 5, 2, 8, 1, 7, 9]

last = nums.pop()     # pop() is different: it DOES return something
print(last)           # 9
print(nums)           # [10, 5, 2, 8, 1, 7]

nums.remove(8)
print(nums)           # [10, 5, 2, 1, 7]

print(len(nums))      # 5

#Trap 1: in-place methods return None
nums = [3, 1, 2]
result = nums.sort()   # sorts nums in place
print(result)          # None  ← common bug
sorted_copy = sorted(nums)   # returns a NEW sorted list
print(sorted_copy)

# Trap 2: Copies

a = [1, 2, 3]
b = a            # same list (alias)
c = a.copy()
print(b)
print(c)     # new list (shallow copy)

nested = [[1, 2], [3, 4]]
shallow = nested.copy()
shallow[0].append(99)
print(nested)    # [[1, 2, 99], [3, 4]] ← inner list is still shared!

import copy
deep = copy.deepcopy(nested)
print(deep)  # copies inner lists too

grid = [[0] * 3] * 3
grid[0][0] = 1
print(grid)   # [[1,0,0],[1,0,0],[1,0,0]] ← same inner list 3 times

# 5.  Tuples (tuple): ordered and immutable

point = (3,4)
x, y = point
a, b = b, a
print(x, y)
print(a, b)


single = (5,)   
print(single)      # a one-item tuple needs the comma
not_tuple = (5)       # this is just the int 5
print(not_tuple)

# Use tuples for fixed records (coordinates, RGB colours, database rows) and as dict keys, which lists can't be.

# A tuple holding a list can still have that inner list changed. The tuple itself stays fixed, but its contents aren't frozen:
t = ([1, 2], 3)
t[0].append(99)   # works → ([1, 2, 99], 3)

# 6. Dictionaries key → value, mutable

emp = {"name": "Asha", "role": "Data Scientist", "years": 3}

emp["name"]              # 'Asha'
#emp["salary"]            # KeyError if missing
emp.get("salary", 0)     # 0 → safe default
emp["city"] = "Hamburg"  # add or update
emp.pop("years")         # remove and return

"role" in emp            # True → checks KEYS, not values

for key, value in emp.items():
    print(key, value)

emp.keys(), emp.values()

# 7. Sets (set): unique items, unordered, mutable

tags = {"python", "sql", "python"}
print(tags)            # {'python', 'sql'} → duplicates removed

tags.add("git")
tags.discard("java")   # no error if missing (remove() would error)

a = {1, 2, 3}
b = {2, 3, 4}
a | b    # union        {1, 2, 3, 4}
a & b    # intersection {2, 3}
a - b    # difference   {1}

empty = set()   # NOT {} → that's an empty dict

# Use sets to remove duplicates or check membership quickly: x in my_set is much faster than x in my_list for large data.

# Q1
ah = "hi"
bh = ah
ah += "!"
print(bh)
print(ah)
# Q2
ac = [1]
bc = ac
ac += [2]
print(bc)
# Q3
d = {(1, 2): "ok"}
d[[1, 2]] = "no"
