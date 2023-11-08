def main():
    name = input("Enter a string: ")
    string = name.lower()
    vowelCount = 0
    consonantsCount = 0

    for x in string:
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
            vowelCount = vowelCount + 1
        else:
            consonantsCount = consonantsCount + 1
    print("Vowels: ", vowelCount)
    print("Consonants: ", consonantsCount)


if __name__ == "__main__":
    main()
