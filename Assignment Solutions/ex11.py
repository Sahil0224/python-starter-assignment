from datetime import datetime


def main():
    date = datetime.today().strftime('%m/%d/%Y')
    f = open("C:\\Users\\C:\\Users\\f96s96x\\tedprojects\\Python\\python-starter-assignment\\Assignment Solutions", "w")
    f.write(f"Today's date is: {date}.")
    f.close()


if __name__ == "__main__":
    main()
