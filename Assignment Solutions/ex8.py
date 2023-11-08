def main():
    myList = [6,2,7,3,77,7,1]
    min = None
    for x in myList:
        if min == None or x < min:
            min = x
    print(min)

if __name__ == "__main__":
    main()