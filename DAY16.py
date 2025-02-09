# 1. Filter students whose names are less than 6 characters
def filter_short_names(students):
    return list(filter(lambda name: len(name) < 6, students))

students = ["Alice", "Bob", "Charlie", "Dave", "Eve"]
print("1. Filtered short names:", filter_short_names(students))

# 2a. Display words in upper case along with the length of each word
def words_uppercase_length(sentence):
    words = sentence.split()
    return list(map(lambda word: {'word': word.upper(), 'length': len(word)}, words))

sentence = "Hello how are you?"
print("2a. Words in uppercase with length:", words_uppercase_length(sentence))

# 2b. Display total number of each vowel in each word
def count_vowels_in_words(sentence):
    vowels = 'aeiou'
    words = sentence.split()
    return list(map(lambda word: {v: word.lower().count(v) for v in vowels} | {'length': len(word)}, words))

print("2b. Vowel count in words:", count_vowels_in_words(sentence))

# 3. Transpose matrix elements using lambda
def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
print("3. Transposed matrix:", transpose_matrix(matrix))
