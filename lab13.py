def process_input(text):
    new = text + "-able"
    return new

def main():
    text = input("Enter a sentence: ")
    print(process_input(text))


if __name__ == "__main__":
    main()
