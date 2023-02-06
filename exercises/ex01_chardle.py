"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730525708"
    
solution = input("Enter a 5-character word: ")
if len(solution) != 5:
    print("Error: Word must contain 5 characters")
    exit()

letter = input("Enter a single chracter: ")
if len(letter) != 1:
    print("Error: Character must be a single character")
    exit()
    
print("searching for " + letter + " in " + solution)
instance = 0

if letter == solution[0]:
    print(letter + " found at index 0")
    instance += 1
if letter == solution[1]:
    print(letter + " found at index 1")
    instance += 1
if letter == solution[2]:
    print(letter + " found at index 2")
    instance += 1
if letter == solution[3]:
    print(letter + " found at index 3")
    instance += 1
if letter == solution[4]:
    print(letter + " found at index 4")
    instance += 1
if instance == 1:
    print(str(instance) + " instance of " + letter + " found in " + solution)
if instance > 1:
    print(str(instance) + " instances of " + letter + " found in " + solution)
if instance == 0:
    print("No instances of " + letter + " found in " + solution)