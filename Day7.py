# 1
L1 = ["Alice", "Bob", "Charlie", "David", "Eve"]

# 2
print("Total number of students:", len(L1))

# 3
L1.append("Frank")
print("Updated list of students:", L1)

# 4
print("Students in sorted order:", sorted(L1))

# 5
student_name = input("Enter a student's name to check: ")
print(f"{student_name} is {'present' if student_name in L1 else 'not present'} in the list.")

# 6
if student_name in L1:
    print(f"Total number of students named {student_name}: {L1.count(student_name)}")
    print(f"First occurrence of {student_name} is at position {L1.index(student_name)}")

# 7
L1.pop()
print("List after removing the last student:", L1)

# 8
student_to_remove = input("Enter the name of the student to remove: ")
L1 = [student for student in L1 if student != student_to_remove]
print("List after removing the student:", L1)

# 9
student_to_remove_all = input("Enter the name of the student to remove all occurrences: ")
L1 = [student for student in L1 if student != student_to_remove_all]
print("List after removing all occurrences of the student:", L1)

# 10
numbers = [23, 45, 12, 67, 34, 89, 90, 11, 56, 78]
print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))

# 11
alphabets = list("abcdefghijklmnopqrstuvwxyz")
vowels = ('a', 'e', 'i', 'o', 'u')
vowel_count = sum(1 for char in alphabets if char in vowels)
print("Total number of vowels in the list:", vowel_count)

# Example content for Day 7
print("This is Day 7 of Python programming.")
