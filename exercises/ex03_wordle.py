"""EX03 - Wordle."""

__author__ = "730525708"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
#guess = a string that is being searched through for the second parameter
#character = a string that is expected to be a single character in length and is the character being searched for


def contains_char(guess: str, character: str) -> bool:
    """Finding single character of second string from first string."""
    assert len(character) == 1
    index: int = 0
    while index < len(guess):
        if guess[index] == character:
            return True
        index += 1 
    return False


def emojified(guess: str, secret: str) -> str:
    """Emoji box codification."""
    assert len(guess) == len(secret)
    index: int = 0 
    result: str = ""
    while index < len(secret):
        if contains_char(secret, guess[index]):
            if secret[index] == guess[index]:
                result += GREEN_BOX
            if secret[index] != guess[index]:
                result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1
    return result


def input_guess(expected_length: int) -> str:
    """Prompt until guess of expected length is provided."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while expected_length != len(guess):
        guess = str(input(f"That wasn't {expected_length} chars! Try again: "))
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn: int = 1
    guess: str = ""
    playing: bool = True
    while turn < 7 and playing:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            playing = False
        turn += 1
    if turn == 7:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()