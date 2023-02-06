"""EX02 - One-Shot Wordle - Loops!"""

_author_ = "730525708"
secret: str = "python"
number: int = len(secret)
guess: str = str(input(f"What is your {number}-letter guess? "))
playing: bool = True
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: int = 0
result: str = ""
    

while len(guess) != number:
    guess = str(input(f"That was not {number} letters! Try again: "))

while index < len(secret):
    if guess[index] == secret[index]:
        result += GREEN_BOX
    else:
        found: bool = False
        alt_indices: int = 0
        while found is False and alt_indices < len(secret):
            if secret[alt_indices] == guess[index]:
                found = True
            else:
                alt_indices +=1
        if found is True:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
    index += 1 
print(result)

while playing:
    if len(guess) == number and guess == secret:
        print("Woo! You got it!")
        playing = False
    else:
        if len(guess) == number and guess != secret:
                print("Not quite. Play again soon!")
                playing = False