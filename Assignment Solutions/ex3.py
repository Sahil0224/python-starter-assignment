def main():
    number = (input("Enter list of numbers: "))
    numberList = number.split(',')
    if (numberList[0] == numberList[-1]):
        print(True)
    else:
        print(False)


if __name__ == "__main__":
    main()