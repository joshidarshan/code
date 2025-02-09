# 1
print("Ascending order from 1 to 10:")
for i in range(1, 11):
    print(i)
print("Descending order from 10 to 1:")
for i in range(10, 0, -1):
    print(i)

# 2
print("Odd numbers between 1 to 50:")
for i in range(1, 51, 2):
    print(i)

# 3
for i in range(1, 6):
    print('*' * i)

# 4
print("Number pyramid:")
for i in range(1, 6):
    print(" ".join(map(str, range(1, i + 1))))

# 5
user_string = input("Enter a string to reverse: ")
print("Reversed string:", user_string[::-1])

# 6
user_tuple = tuple(input("Enter elements of a tuple separated by commas: ").split(','))
print("Reversed tuple:", user_tuple[::-1])

# 7
original_string = input("Enter a string to replace 'o' with '@': ")
modified_string = "".join('@' if char == 'o' else char for char in original_string)
print("Modified string:", modified_string)

# 8
vowels = ('a', 'e', 'i', 'o', 'u')
input_string = input("Enter a string to count vowels: ").lower()
vowel_count = sum(1 for char in input_string if char in vowels)
print("Total number of vowels:", vowel_count)

# Example content for Day 6
print("This is Day 6 of Python programming.")
