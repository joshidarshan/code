# 1
t1 = ("joshi", "darshan", "satishabhai")
print("Tuple t1:", t1)

# 2
t2 = (85, 90, 78, 92, 88)
print(t2)

# 3
print("Total marks (with sum()):", sum(t2))
print("Total marks:", sum(t2))

# 4
t3 = (t1, t2)
print("Nested tuple:", t3)

# 5
n = int(input("Enter a number to search in t3: "))
found = any(n in i for i in t3)
print("present in" if found else "not present in", n)

# 6
fruits = ("apple", "banana", "cherry", "date", "elderberry")
fruit_s = input("Enter a fruit name to search: ")
print(fruit_s if fruit_s in fruits else "Not found")

# 7
cities = ("anand", "virpur", "rajkot", "surat", "ahmedabad")

# 8
print("Length of each city name (without len()):")
for city in cities:
    print("city", len(city.strip()))

# 9
t4 = (("joshi", "darshan", "satishabhai"), ("reading", "coding", "gaming"), ("jay", "raj", "meet"), "mca")
print(t4)

# 10
find = input("Enter an element to find in t4: ")
found = False
for i, sub_tuple in enumerate(t4):
    if isinstance(sub_tuple, tuple) and find in sub_tuple:
        print(f"Element '{find}' found in position {i} at index {sub_tuple.index(find)}")
        found = True
        break
    elif find == sub_tuple:
        print(f"Element '{find}' found in position {i}")
        found = True
        break
if not found:
    print("Not found")

# 11
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
odd_numbers = tuple(num for num in numbers if num % 2 != 0)
even_numbers = tuple(num for num in numbers if num % 2 == 0)
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)

# Example content for Day 5
print("This is Day 5 of Python programming.")
