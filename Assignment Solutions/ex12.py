def main():
    number = input("Enter integer: ")
    try:
        number = int(number)
    except ValueError:
        print(number + " is not a number")
        exit()

    number = -int(number)
    print(number)


if __name__ == "__main__":
    main()