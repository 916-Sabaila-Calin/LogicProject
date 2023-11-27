from sys import exit

import functions as functions


def PrintMenu():
    OutputString("")
    OutputString("Press 1 if you want to add two numbers.")
    OutputString("Type \"exit\" to close the application.")


def HandleOptions(option: str):
    if option == "1":
        base = InputBase()
        x = InputFirstNumber()
        y = InputSecondNumber()

        functions.ManageAddNumbers(x, y, base)

    elif option == "exit":
        exit()

    else:
        OutputString(HandleErrors(1))


def HandleErrors(errorCode: int) -> str:
    string = "Error: "

    if errorCode == 1:
        string += "The input is invalid!"
    elif errorCode == 2:
        string += "The base is not between 2 and 16!"
    elif errorCode == 3:
        string += "The digits of the number cannot be higher or equal to the base!"
    elif errorCode == 4:
        pass

    return string


def InputBase():
    OutputString("")
    OutputString("Enter the base in which the operation will take place.")

    base = InputString()
    return base


def InputFirstNumber() -> str:
    OutputString("")
    OutputString("Enter the first number.")

    number = InputString()
    return number


def InputSecondNumber() -> str:
    OutputString("")
    OutputString("Enter the second number.")

    number = InputString()
    return number


def InputString() -> str:
    string = input()
    return string


def OutputString(string: str):
    print(string)