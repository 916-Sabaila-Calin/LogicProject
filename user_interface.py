from sys import exit

import functions as functions


def PrintMenu():
    """
    This function prints the menu
    :return: -
    """

    OutputString("")
    OutputString("Press 1 to add two numbers.")
    OutputString("Press 2 to subtract two numbers.")
    OutputString("Press 3 to multiply two numbers.")
    OutputString("Press 4 to divide two numbers.")
    OutputString("Press 5 to convert numbers using successive divisions.")
    OutputString("Press 6 to convert numbers using 10 as an intermediary base.")
    OutputString("Press 7 to convert numbers using rapid conversions.")
    OutputString("Press 8 to convert numbers using the substitution method.")
    OutputString("Type \"exit\" to close the application.")


def HandleOptions(option: str):
    """
    This function handles the options of the program
    :param option: a string representing the option
    :raise: an exception with the string message "Error: The input is invalid!", if
            the option is invalid
    """

    try:
        if option == "1":
            OutputString("The result is: " + functions.ManageAddNumbers())
        elif option == "2":
            OutputString("The result is: " + functions.ManageSubtractNumbers())
        elif option == "3":
            OutputString("The result is: " + functions.ManageMultiplyNumbers())
        elif option == "4":
            ans = functions.ManageDivideNumbers()
            OutputString("The quotient is: " + ans[0] + " and the remainder is: " + ans[1])
        elif option == "5":
            OutputString("The result is: " + functions.ManageConvertUsingSuccessiveDivisions())
        elif option == "6":
            OutputString("The result is: " + functions.ManageConvertUsing10AsIntermediaryBase())
        elif option == "7":
            OutputString("The result is: " + functions.ManageConvertUsingRapidConversions())
        elif option == "8":
            OutputString("The result is: " + functions.ManageConvertUsingSubstitutionMethod())
        elif option == "exit":
            exit()
        else:
            raise Exception(HandleErrors(1))

    except Exception as exception:
        OutputString(str(exception))


def HandleErrors(errorCode: int) -> str:
    """
    This function handles the errors of the program
    :param errorCode: an integer representing the error code
    :return: a string of the form "Error: + custom message"
    """

    string = "Error: "

    if errorCode == 1:
        string += "The input is invalid!"
    elif errorCode == 2:
        string += "The base is not between 2 and 16!"
    elif errorCode == 3:
        string += "The digits of the number cannot be greater or equal than the base!"
    elif errorCode == 4:
        string += "At least one of the operands should have one digit in the hexadecimal format!"
    elif errorCode == 5:
        string += "The source base should be greater or equal than the destination base!"
    elif errorCode == 6:
        string += "The source base should be less or equal than the destination base!"
    elif errorCode == 7:
        string += "Cannot do rapid conversions using the provided bases!"
    elif errorCode == 8:
        string += "The divisor should have one digit!"
    elif errorCode == 9:
        string += "Cannot divide by 0!"

    return string


def InputBase() -> str:
    """
    This function takes as input from the user a string and returns it
    :return: a string representing the base of a number
    """

    OutputString("")
    OutputString("Enter the base in which the operation will take place.")

    base = InputString()
    return base


def InputSourceBase() -> str:
    """
    This function takes as input from the user a string and returns it
    :return: a string representing the base of a number
    """

    OutputString("")
    OutputString("Enter the source base.")

    sourceBase = InputString()
    return sourceBase


def InputDestinationBase() -> str:
    """
    This function takes as input from the user a string and returns it
    :return: a string representing the base of a number
    """

    OutputString("")
    OutputString("Enter the destination base.")

    destinationBase = InputString()
    return destinationBase


def InputFirstNumber() -> str:
    """
    This function takes as input from the user a string and returns it
    :return: a string representing a number
    """

    OutputString("")
    OutputString("Enter the first number.")

    number = InputString()
    return number


def InputSecondNumber() -> str:
    """
    This function takes as input from the user a string and returns it
    :return: a string representing a number
    """

    OutputString("")
    OutputString("Enter the second number.")

    number = InputString()
    return number


def InputNumber() -> str:
    """
    This function takes as input from the user a string and returns it
    :return: a string representing a number
    """

    OutputString("")
    OutputString("Enter the number.")

    number = InputString()
    return number


def InputString() -> str:
    """
    This function takes as input from the user a string and returns it
    :return: a string
    """

    string = input()
    return string


def OutputString(string: str):
    """
    This function outputs a string
    :param string: a string
    :return: -
    """

    print(string)
