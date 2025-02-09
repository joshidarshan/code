# 1
input_string = input("Enter a string: ").lower()
vowels = ('a', 'e', 'i', 'o', 'u')
vowel_counts = {vowel: input_string.count(vowel) for vowel in vowels}
total_vowels = sum(vowel_counts.values())
print("Total number of vowels:", total_vowels)
for vowel, count in vowel_counts.items():
    print(f"Count of '{vowel}':", count)

# 2
students = {}
for _ in range(5):
    roll_no = input("Enter roll number: ")
    marks = list(map(int, input("Enter marks of 6 subjects separated by commas: ").split(',')))
    students[roll_no] = marks

# 3
subject_marks = {i: [] for i in range(6)}
for marks in students.values():
    for i, mark in enumerate(marks):
        subject_marks[i].append(mark)

min_max_marks = {i: {"min": min(marks), "max": max(marks)} for i, marks in subject_marks.items()}
print("Minimum and maximum marks of each subject:")
for subject, marks in min_max_marks.items():
    print(f"Subject {subject + 1}: Min = {marks['min']}, Max = {marks['max']}")

# Example content for Day 10
print("This is Day 10 of Python programming.")
