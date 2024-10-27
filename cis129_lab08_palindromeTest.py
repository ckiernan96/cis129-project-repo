# Function to check if word is a palindrome
def is_palindrome(x):
    stack = []
    # all characters get pushed into the stack
    for letter in x:
        stack.append(letter)
    # pops characters from stack and compares them to the string    
    for letter in x:
        if letter != stack.pop():
            return False
    return True
# Function to remove punctuation from word
def remove_punctuation(word):
    word = ' '.join(filter(lambda x: x.isalpha() or x.isdigit() or x.isspace(), word))
    return word
    
# Input for the palindrome checker
print('This program will tell you if that word is a palindrome.')
word = input('Enter a word:')
oldWord = word
# Code to remove spaces, change all letters to lowercase, and Call to function to remove punctuation
word = remove_punctuation(word)
word = word.replace(" ", "")
word = word.lower()
print(f"Is {oldWord} a palindrome? : {is_palindrome(word)}") 

print()
input("Press Enter to Exit")
