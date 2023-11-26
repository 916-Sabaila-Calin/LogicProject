from sys import exit

import functions as functions


def PrintMenu():
    OutputString("")
    OutputString("Press 1 if you want to add two numbers.")
    OutputString("Type \"exit\" to close the application.")


def HandleOptions(option: str):
    try:
        if option == "1":
            base = InputBase()
            x = InputNumber(1)
            y = InputNumber(2)

            result = functions.AddNumbers(base, x, y)
            OutputString(result)

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
        pass

    return string


def InputBase() -> int:
    OutputString("")
    OutputString("Enter the base in which the operation will take place.")

    base = InputString()
    base = int(base)

    if base < 2 or base > 16:
        raise Exception(HandleErrors(2))

    return base


def HandlePrintingForInputNumber(option: int):
    OutputString("")
    if option == 1:
        OutputString("Enter the first number.")
    elif option == 2:
        OutputString("Enter the second number.")


def InputNumber(option: int) -> float:
    HandlePrintingForInputNumber(option)
    number = InputString()
    number = float(number)
    return number


def InputString() -> str:
    string = input()
    return string


def InputInt() -> int:
    x = InputString()
    x = int(x)
    return x


def OutputString(string: str):
    print(string)