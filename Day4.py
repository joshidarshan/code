string = input("Enter the string: ")
print("Menu:")
print("a. Find the length of a string")
print("b. Print the string in upper case")
print("c. Print the string in lower case")
print("d. Print the string with initial capital")
print("e. Split the string")
print("f. Exit")

choice = input("Enter your choice: ")
if choice == 'a':
    print(len(string))
elif choice == 'b':
    print(string.upper())
elif choice == 'c':
    print(string.lower())
elif choice == 'd':
    print(string.capitalize())
elif choice == 'e':
    print(string.split())
else:
    print("Invalid choice. Please try again.")

#2
s1 = input("Enter the first string ")
s2 = input("Enter the second string ")

if s2 in s1:
    print(s2, "is present in", s1)
else:
    print(s2, "is not present in", s1)


#3
if s2 in s1:
    f1 = s1.find(s2)
    l1 = s1.rfind(s2)
    print(f1)
    print(l1)
else:
    print(s2, "is not present in", s1)
    
#4
if s2 in s1:
    count1 = s1.count(s2)
    print(count1)
else:
    print(s2, "is not present in", s1)
    
#5
total = len(string.split())
print("Total number of words in the input string:", total)

# Example content for Day 4
print("This is Day 4 of Python programming.")