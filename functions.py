import user_interface as ui


def AddNumbers(x: str, y: str, base: int) -> str:
    pass


def ManageAddNumbers(x: str, y: str, base: str):
    try:
        ValidateBase(base)
        base = int(base)

        ValidateNumber(x, base)
        ValidateNumber(y, base)

        AddNumbers(x, y, base)
    except Exception as exception:
        ui.OutputString(str(exception))


def ValidateNumber(number: str, base: int):
    for i in range(len(number)):
        if (number[i] != '0' and number[i] != '1' and number[i] != '2' and number[i] != '3' and number[i] != '4' and
            number[i] != '5' and number[i] != '6' and number[i] != '7' and number[i] != '8' and number[i] != '9' and
            number[i] != 'A' and number[i] != 'B' and number[i] != 'C' and number[i] != 'D' and number[i] != 'E' and
            number[i] != 'F' and number[i] != 'a' and number[i] != 'b' and number[i] != 'c' and number[i] != 'd' and
            number[i] != 'e' and number[i] != 'f' and number[i] != '-' and number[i] != '.') == True:
            raise Exception(ui.HandleErrors(1))

    for i in range(len(number)):
        if number[i] == '-' or number[i] == '.':  # For negative numbers and decimal numbers
            continue

        if HexaToDecimal(number[i]) >= base:
            raise Exception(ui.HandleErrors(3))


def ValidateBase(base: str):
    base = int(base)
    if base < 2 or base > 17:
        raise Exception(ui.HandleErrors(2))


def HexaToDecimal(string: str) -> int:
    if '0' <= string and string <= '9':
        return int(string)
    elif string == 'A' or string == 'a':
        return 10
    elif string == 'B' or string == 'b':
        return 11
    elif string == 'C' or string == 'c':
        return 12
    elif string == 'D' or string == 'd':
        return 13
    elif string == 'E' or string == 'e':
        return 14
    elif string == 'F' or string == 'f':
        return 15
