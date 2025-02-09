from functools import reduce

# 1. Sort the list elements using lambda
sort_list = lambda lst: sorted(lst)

lst = [5, 2, 9, 1, 5, 6]
print("1. Sorted list:", sort_list(lst))

# 2. Find the average of all the elements passed as an argument in lambda
average = lambda *args: sum(args) / len(args) if args else 0

print("2. Average:", average(1, 2, 3, 4, 5))

# 3. Find the square of each element of a list using map()
square_elements = lambda lst: list(map(lambda x: x ** 2, lst))

print("3. Squared elements:", square_elements(lst))

# 4. Calculate grades for a list of scores using map()
calculate_grades = lambda scores: list(map(lambda x: 'A' if x >= 90 else 'B' if x >= 80 else 'C' if x >= 70 else 'D' if x >= 60 else 'F', scores))

scores = [88, 92, 78, 95, 86]
print("4. Grades:", calculate_grades(scores))

# 5. Add all the elements of the list using reduce()
sum_elements = lambda lst: reduce(lambda x, y: x + y, lst)

print("5. Sum of elements:", sum_elements(lst))

# 6. Multiply all the elements of the list using reduce()
multiply_elements = lambda lst: reduce(lambda x, y: x * y, lst)

print("6. Product of elements:", multiply_elements(lst))

# 7. Find the maximum element from the list using reduce()
max_element = lambda lst: reduce(lambda x, y: x if x > y else y, lst)

print("7. Maximum element:", max_element(lst))

# Desirable Assignment
# 8. Sorting the dictionary elements using lambda
sort_dict = lambda lst: sorted(lst, key=lambda x: (x['age'], x['name']))

stud = [{'name': 'Amit', 'age': 25}, {'name': 'Bina', 'age': 22}, {'name': 'Dax', 'age': 25}]
print("8. Sorted dictionary:", sort_dict(stud))
