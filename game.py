import time
import sys

# Time to try and guess correctly, be careful

print("---------------------------------")
print("      Can You Guess Right?!      ")
print("---------------------------------")


class your_guess:
    def __init__(self, guess):
        self.guess = guess

    def guessing_big(self):
        global guess
        global guess_count
        while int(guess) > int(answer):
            print("")
            print("your guess is too big... {}".format(guess_distance.distance()))
            guess_count += 1
            so_far.append(guess)
            print("")
            print("=" * 25)
            print("")
            if guess_count == 4:
                if guess == answer:
                    guess_right.guessing_right()

                else:
                    print("--------------------")
                    print("  You have lost...  ")
                    print("--------------------")
                    break

            else:
                print("----------------------")
                print("  You're on guess {}  ".format(guess_count))
                print("----------------------")

                print("\n")

                print("----------------------")
                print(f"    Guesses so far\n    {so_far}")
                print("----------------------")

                guess = int(input("Please guess again...\n"))

                if int(guess) < int(answer):
                    guess_smoll.guessing_smoll()

                elif int(guess) == int(answer):
                    guess_right.guessing_right()

    def guessing_smoll(self):
        global guess
        global guess_count
        while int(guess) < int(answer):
            print("")
            print("your guess is too small... {}".format(guess_distance.distance()))
            guess_count += 1
            so_far.append(guess)
            print("")
            print("=" * 25)
            print("")
            if guess_count == 4:
                if guess == answer:
                    guess_right.guessing_right()

                else:
                    print("--------------------")
                    print("  You have lost...  ")
                    print("--------------------")
                    break

            else:
                print("----------------------")
                print("  You're on guess {}  ".format(guess_count))
                print("----------------------")

                print("\n")

                print("----------------------")
                print(f"    Guesses so far\n    {so_far}")
                print("----------------------")

                guess = int(input("Please guess again...\n"))

                if int(guess) == int(answer):
                    guess_right.guessing_right()

                elif int(guess) > int(answer):
                    guess_right.guessing_big()

    def guessing_right(self):
        global guess
        global guess_count
        if int(guess) == int(answer):
            print("")
            print("-----------------")
            print(" You guessed it! ")
            print("-----------------")
            print("")
            print("==================")
            print("The answer was {}".format(answer))
            print("==================")

    def distance(self):

        if answer > guess:
            dist = answer - guess

        else:
            dist = guess - answer

        if dist > 5:
            how_close = "Not close"

        else:
            how_close = "Close!"

        return how_close


so_far = list()

guess_count = 1
answer = int(input("Please enter an answer\n"))
time.sleep(5)

print("\n"*5)
print("---------------------------------")
print("")

guess = int(input("What is your guess?\n"))

guess_big = your_guess(guess)
guess_smoll = your_guess(guess)
guess_right = your_guess(guess)
guess_distance = your_guess(guess)


if guess > answer:
    guess_big.guessing_big()

elif guess < answer:
    guess_smoll.guessing_smoll()

elif guess == answer:
    guess_right.guessing_right()

else:
    print("error...")
    sys.exit()













