def findString(string1, string2='all'):
    positions = []
    index = string1.find(string2)
    while index != -1:
        positions.append(index)
        index = string1.find(string2, index + 1)
    if positions:
        return positions
    else:
        return "Not found"

str1 = "Hello all, Good Morning to all."
str2 = "all"
print("Positions of occurrences:", findString(str1, str2))

fruits = ["apple", "banana", "cherry"]

def add_fruit(fruit_list, fruit):
    fruit_list.append(fruit)

add_fruit(fruits, "orange")

def insert_fruit(fruit_list, fruit, position=1):
    fruit_list.insert(position, fruit)

insert_fruit(fruits, "mango", 2)

def update_fruit(fruit_list, index, new_fruit):
    fruit_list[index] = new_fruit

update_fruit(fruits, 1, "blueberry")

def remove_fruit(fruit_list, identifier):
    if isinstance(identifier, int):
        fruit_list.pop(identifier)
    elif isinstance(identifier, str):
        fruit_list.remove(identifier)

remove_fruit(fruits, "cherry")

def sort_fruits(fruit_list):
    fruit_list.sort()

sort_fruits(fruits)
print("Fruits list:", fruits)

def generate_prime(n):
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes

total_primes = int(input("Enter the number of prime numbers to generate: "))
print("Prime numbers:", generate_prime(total_primes))