from sys import argv
import os


def main():
    try:
        with open(argv[1], 'r') as f:
            words = f.read()
    except:
        print("Err")

    print("What message would you like to censor?")
    message = input()
    message = message.lower()
    tokens = message.split()
    index = 0
    while index < len(tokens):
        if tokens[index] in words:
            tokens[index] = len(tokens[index]) * "*"
        index += 1
    output = " ".join(tokens)
    print(output)


if __name__ == "__main__":
    main()
