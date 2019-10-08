#!/usr/bin/env python3

# Created by: Evano Fotia
# Created on: oct 2019
# this program creates a Positive  Negative program


def main():

    # input
    integer = int(input("Enter a number: "))

    # process & output
    if integer > 0:
        print(" Your integer is postive!")
    elif integer < 0:
        print("Your integer is negeative!")
    elif integer == 0:
        print("your integer is 0!")
    else:
        print("Error, your code is invald! :( ")


if __name__ == "__main__":
    main()
