# 1. Add or find the difference between elements of two lists
def add_or_diff_lists(nums1, nums2):
    return list(map(lambda x, y: x + y if x > y else x - y, nums1, nums2))

nums1 = [6, 5, 3, 9]
nums2 = [0, 1, 7, 7]
print("1. Add or difference:", add_or_diff_lists(nums1, nums2))

# 2. Display all names in upper case using map()
def uppercase_names(names):
    return list(map(lambda name: name.upper(), names))

names = ["Alice", "Bob", "Charlie"]
print("2. Uppercase names:", uppercase_names(names))

# 3. Display list of all round numbers and round them with just 2 decimal points using map()
def round_numbers(numbers):
    rounded = list(map(lambda x: round(x), numbers))
    rounded_two_decimals = list(map(lambda x: round(x, 2), numbers))
    return rounded, rounded_two_decimals

numbers = [6.56773, 9.57668, 4.00914, 56.24241, 9.01344]
rounded, rounded_two_decimals = round_numbers(numbers)
print("3. Rounded numbers:", rounded)
print("3. Rounded to two decimals:", rounded_two_decimals)

# 4. Print all palindrome words using filter()
def filter_palindromes(words):
    return list(filter(lambda word: word == word[::-1], words))

words = ["madam", "racecar", "hello", "world"]
print("4. Palindromes:", filter_palindromes(words))
