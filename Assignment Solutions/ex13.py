def main():
    while True:
        number1 = input("Enter first integer: ")
        if(number1 == "exit"):
            exit()
        else:
            number2 = input("Enter second integer: ")
        if(number2 == "exit"):
            exit()
        sum = int(number1) + int(number2)
        print("Answer: ", sum)


if __name__ == "__main__":
    main()