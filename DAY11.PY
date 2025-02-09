def calculate_sum(numbers):
    return sum(numbers)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def int_divide(a, b):
    return a // b

def power(a, b):
    return a ** b

def area_rectangle(width, length):
    return width * length

def area_triangle(height, base):
    return 0.5 * height * base

def area_circle(radius):
    return 3.14 * radius * radius

def decimal_to_binary(n):
    return bin(n).replace("0b", "")

def decimal_to_octal(n):
    return oct(n).replace("0o", "")

def decimal_to_hexadecimal(n):
    return hex(n).replace("0x", "")

def unique_values(input_list):
    return list(set(input_list))

def multiply_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

def is_in_range(number, start, end):
    return start <= number <= end

def count_case(string):
    upper_case = sum(1 for c in string if c.isupper())
    lower_case = sum(1 for c in string if c.islower())
    return upper_case, lower_case

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print("Sum:", calculate_sum([1, 2, 3, 4, 5]))
print("Addition:", add(5, 3))
print("Subtraction:", subtract(5, 3))
print("Multiplication:", multiply(5, 3))
print("Division:", divide(5, 3))
print("Integer Division:", int_divide(5, 3))
print("Power:", power(5, 3))
print("Area of Rectangle:", area_rectangle(5, 3))
print("Area of Triangle:", area_triangle(5, 3))
print("Area of Circle:", area_circle(3))
print("Decimal to Binary:", decimal_to_binary(10))
print("Decimal to Octal:", decimal_to_octal(10))
print("Decimal to Hexadecimal:", decimal_to_hexadecimal(10))
print("Unique Values:", unique_values([1, 2, 3, 3, 3, 4, 5]))
print("Multiply List:", multiply_list([1, 2, 3, 4, 5]))
print("Is in Range:", is_in_range(5, 1, 10))
print("Count Case:", count_case("Hello World"))
print("Is Prime:", is_prime(7))
