import random


def main():
    myList = []
    for x in range(0, 10):
        myList.append(random.randint(0, 100))
    total = sum(myList)
    print(myList)
    print(f'the sum is: {total}')


if __name__ == "__main__":
    main()
