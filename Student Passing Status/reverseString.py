# Task 3(a)
# Reverse a string word-by-word. e.g. "how are you" ->"you are how"
string = input("Enter a String: ")
print(" ".join(string.split()[::-1]))