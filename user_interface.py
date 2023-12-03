from sys import exit

import functions as functions


def PrintMenu():
    OutputString("")
    OutputString("Press 1 to add two numbers.")
    OutputString("Press 2 to subtract two numbers.")
    OutputString("Press 3 to multiply two numbers.")
    OutputString("Press 4 to divide two numbers.")
    OutputString("Press 5 to convert numbers using successive divisions.")
    OutputString("Type \"exit\" to close the application.")


def HandleOptions(option: str):
    try:
        if option == "1":
            OutputString("The result is: " + functions.ManageAddNumbers())
        elif option == "2":
            OutputString("The result is: " + functions.ManageSubtractNumbers())
        elif option == "3":
            OutputString("The result is: " + functions.ManageMultiplyNumbers())
        elif option == "4":
            pass
        elif option == "5":
            pass
        elif option == "exit":
            exit()
        else:
            raise Exception(HandleErrors(1))

    except Exception as exception:
        OutputString(str(exception))


def HandleErrors(errorCode: int) -> str:
    string = "Error: "

    if errorCode == 1:
        string += "The input is invalid!"
    elif errorCode == 2:
        string += "The base is not between 2 and 16!"
    elif errorCode == 3:
        string += "The digits of the number cannot be higher or equal to the base!"
    elif errorCode == 4:
        string += "At least one of the operands should have one digit!"
    elif errorCode == 5:
        pass

    return string


def InputBase() -> str:
    OutputString("")
    OutputString("Enter the base in which the operation will take place.")

    base = InputString()
    return base


def InputSourceBase() -> str:
    OutputString("")
    OutputString("Enter the source base.")

    sourceBase = InputString()
    return sourceBase


def InputDestinationBase() -> str:
    OutputString("")
    OutputString("Enter the destination base.")

    destinationBase = InputString()
    return destinationBase


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