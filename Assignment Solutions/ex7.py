import random


def main():
    number = random.randint(1, 100)
    if number < 10:
        print(str(number) + ":You lose")
    elif 10 < number < 50:
        print(str(number) + ":Try again")
    elif number > 50:
        print(str(number) + ": You win!")


if __name__ == "__main__":
    main()
