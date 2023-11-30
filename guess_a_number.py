import random
max_num = 100
computer_number = random.randint(1, max_num)
print(computer_number)
guess_count = 3

while guess_count != 0:
    player_input = input(f"Guess the number: (1-{max_num}): ")


    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue

    player_number = int(player_input)

    if player_number == computer_number:
        print("You guessed it!")
        max_num += 100
        computer_number = random.randint(1, max_num)
    elif player_number > computer_number:
        print("Too high!")
        guess_count -= 1
    elif player_number < computer_number:
        print("Too low!")
        guess_count -= 1

    print(f"Guesses remaining: {guess_count}")
    print()
    print(computer_number)