import user_interface as ui


def AddNumbers(x: str, y: str, base: int) -> str:
    # The two numbers are represented using two arrays
    num1, num2 = [], []
    for i in range(len(x) - 1, -1, -1):
        num1.append(x[i])
    for i in range(len(y) - 1, -1, -1):
        num2.append(y[i])

    length = max(len(num1), len(num2))
    carry = 0
    ans = ""
    for i in range(length):
        temp = 0
        if i < len(num1):
            temp += HexaToDecimal(num1[i])
        if i < len(num2):
            temp += HexaToDecimal(num2[i])
        temp += carry

        if carry > 0:
            carry = 0

        carry = temp // base
        ans += DecimalToHexa(temp % base)

    if carry > 0:
        ans += DecimalToHexa(carry)

    ans = ans[::-1]  # Reversing the string
    return ans


def MultiplyNumbers(x: str, y: str, base: int) -> str:
    # Making sure that y is the operand with one digit
    if len(y) > 1:
        x, y = y, x  # Swap

    ans = ""
    carry = 0
    for i in range(len(x) - 1, -1, -1):
        temp = HexaToDecimal(x[i]) * HexaToDecimal(y) + carry

        if carry > 0:
            carry = 0

        carry = temp // base
        ans += DecimalToHexa(temp % base)

    if carry > 0:
        ans += DecimalToHexa(carry)

    ans = ans[::-1]
    return ans


def ManageAddNumbers() -> str:
    base = ui.InputBase()
    x = ui.InputFirstNumber()
    y = ui.InputSecondNumber()

    ValidateBase(base)
    base = int(base)
    ValidateNumber(x, base)
    ValidateNumber(y, base)

    ans = AddNumbers(x, y, base)
    return ans


def ManageMultiplyNumbers() -> str:
    base = ui.InputBase()
    x = ui.InputFirstNumber()
    y = ui.InputSecondNumber()

    ValidateBase(base)
    base = int(base)
    ValidateNumber(x, base)
    ValidateNumber(y, base)
    ValidateOperands(x, y)

    ans = MultiplyNumbers(x, y, base)
    return ans


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


def ValidateOperands(x: str, y: str):
    if len(x) > 1 and len(y) > 1:
        raise Exception(ui.HandleErrors(4))


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


def DecimalToHexa(num: int) -> str:
    if 0 <= num and num <= 9:
        return str(num)
    elif num == 10:
        return 'A'
    elif num == 11:
        return 'B'
    elif num == 12:
        return 'C'
    elif num == 13:
        return 'D'
    elif num == 14:
        return 'E'
    elif num == 15:
        return 'F'
