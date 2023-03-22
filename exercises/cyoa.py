"""Choose Your Own Adventure."""

__author__ = "730525708"

__name__ == "__main__"

player: str
points: int


def greet() -> None: 
    """Greeting player."""
    print("Welcome to the game!")
    player = input("What's your name?")
    print(f"Nice to meet you, {player}!")


def play_game() -> None:
   """Interacting with player and changing points."""
   print(f"Let's start the game, {player}")
   answer = input("Do you want to go left or right?")
   if answer == "left":
    points += 5
    print(f"Great choice, {player}! You gained 5 points.")
    if answer == "right":
        points -= 2
        print(f"Oh no, {player}! You lost 2 points.")
   else:
     print("Invalid input. Please try again.")


def adventure(points: int) -> int:
    """Making 3 choices and gain/lose points."""
    print(f"{player}, you find yourself at a crossroads. Which way do you want to go?")
    print("1. Go left")
    print("2. Go right")
    print("3. Roll the dice")

    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        print(f"{player}, you found a treasure chest and gained 10 points!")
        points += 10
    elif choice == "2":
        print(f"{player}, you stumbled into a trap and lost 5 points!")
        points -= 5
    elif choice == "3":
        dice_roll = random.randint(1, 6)
        print(f"{player}, you rolled a {dice_roll}!")
        if dice_roll <= 3:
            print(f"You landed on a lucky square and gained 8 points!")
            points += 8
        else:
            print(f"You fell into a pit and lost 3 points!")
            points -= 3
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
    return points


def main():
    points: int = 0
    player: str
    EMOJI = "\U0001F600"
    greet()
    while True:
        print(f"\n{player}, you have {points} adventure points. What do you want to do next?")
        print("1. Continue down the path")
        print("2. Take a break and rest")
        print("3. End the adventure")

        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == "1":
            points = adventure(points)
        elif choice == "2":
            print(f"{player}, you take a break and gain 3 points!")
            points += 3
        elif choice == "3":
            print(f"Thanks for playing, {player}! You accumulated {points} adventure points. {EMOJI}")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


EMOJI = "\U0001F600"


if __name__ == "__main__":
    main()