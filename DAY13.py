# ...existing code...

# 1. Lambda function to return maximum of two numbers
max_two = lambda a, b: a if a > b else b

print("1. Max of 2 and 3:", max_two(2, 3))

# 2. Lambda function to return maximum of three numbers
max_three = lambda a, b, c: max(a, b, c)

print("2. Max of 1, 4, and 2:", max_three(1, 4, 2))

# 3. Lambda function to multiply by 5 if even, by 10 if odd
multiply_even_odd = lambda x: x * 5 if x % 2 == 0 else x * 10

print("3. Multiply 4 (even):", multiply_even_odd(4))
print("3. Multiply 5 (odd):", multiply_even_odd(5))

# 4a. Lambda function to separate integer elements from a list
separate_integers = lambda lst: list(filter(lambda x: isinstance(x, int), lst))

mixed_list = [1, 'apple', 2, 'banana', 3, 'cherry']
print("4a. Separated integers:", separate_integers(mixed_list))

# 4b. Lambda function to separate string elements from a list
separate_strings = lambda lst: list(filter(lambda x: isinstance(x, str), lst))

print("4b. Separated strings:", separate_strings(mixed_list))

# 5. Filter all vowels from a given string
filter_vowels = lambda s: ''.join(filter(lambda x: x.lower() in 'aeiou', s))

sample_string = "Hello World"
print("5. Filtered vowels:", filter_vowels(sample_string))

filter_even = lambda lst: list(filter(lambda x: x % 2 == 0, lst))
filter_odd = lambda lst: list(filter(lambda x: x % 2 != 0, lst))

numbers = [1, 2, 3, 4, 5, 6]
print("Even numbers:", filter_even(numbers))
print("Odd numbers:", filter_odd(numbers))

product_or_concat = lambda a, b: a * b if isinstance(a, int) and isinstance(b, int) else str(a) + str(b)

print("Product of 2 and 3:", product_or_concat(2, 3))
print("Concatenation of 'Hello' and 'World':", product_or_concat('Hello', 'World'))