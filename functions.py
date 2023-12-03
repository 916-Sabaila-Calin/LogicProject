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


def SubtractNumbers(x: str, y: str, base: int) -> str:
    if x == y:
        return '0'

    # Checking if the result is negative
    isNegative = False
    if len(x) < len(y) or (len(x) == len(y) and x < y):
        x, y = y, x  # Swap
        isNegative = True

    li_x, li_y = [], []
    for i in range(len(x)):
        li_x.append(x[i])
    for i in range(len(y)):
        li_y.append(y[i])

    carry = 0
    ans = ""
    while len(li_x) > 0:
        ld_x = li_x[-1]
        li_x.pop()

        ld_y = '0'
        if len(li_y) > 0:
            ld_y = li_y[-1]
            li_y.pop()

        ld_x = HexaToDecimal(ld_x)
        ld_y = HexaToDecimal(ld_y)

        temp = ld_x - ld_y + carry
        if temp < 0:
            carry = -1
            temp += base
        else:
            carry = 0

        temp = DecimalToHexa(temp)
        ans = temp + ans

    ans = ans.lstrip("0")

    if isNegative == True:
        ans = "-" + ans

    return ans


def ManageSubtractNumbers() -> str:
    base = ui.InputBase()
    x = ui.InputFirstNumber()
    y = ui.InputSecondNumber()

    ValidateBase(base)
    base = int(base)
    ValidateNumber(x, base)
    ValidateNumber(y, base)

    ans = SubtractNumbers(x, y, base)
    return ans


def MultiplyNumbers(x: str, y: str, base: int) -> str:
    # Making sure that y is the operand with one digit
    if len(y) > 1:
        x, y = y, x  # Swap

    # Returning 0 when multiplying by 0
    if y == '0':
        return '0'

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


def SuccessiveDivisions():
    pass


def ManageSuccessiveDivisions() -> str:
    sourceBase = ui.InputSourceBase()
    destinationBase = ui.InputDestinationBase()
    x = ui.InputFirstNumber()

    ValidateBase(sourceBase)
    ValidateBase(destinationBase)
    sourceBase = int(sourceBase)
    destinationBase = int(destinationBase)
    ValidateBasesForSuccessiveDivisions(sourceBase, destinationBase)
    ValidateNumber(x, sourceBase)

    ans = ""
    return ans


def ToBase10(x: str, sourceBase: int) -> str:
    ans, pow = 0, 1
    for i in range(len(x) - 1, -1, -1):
        ans = ans + pow * HexaToDecimal(x[i])
        pow *= sourceBase

    return str(ans)


def ValidateNumber(number: str, base: int):
    if number[0] == '0' and len(number) > 1:
        raise Exception(ui.HandleErrors(1))

    for i in range(len(number)):
        if (number[i] != '0' and number[i] != '1' and number[i] != '2' and number[i] != '3' and number[i] != '4' and
            number[i] != '5' and number[i] != '6' and number[i] != '7' and number[i] != '8' and number[i] != '9' and
            number[i] != 'A' and number[i] != 'B' and number[i] != 'C' and number[i] != 'D' and number[i] != 'E' and
            number[i] != 'F' and number[i] != 'a' and number[i] != 'b' and number[i] != 'c' and number[i] != 'd' and
            number[i] != 'e' and number[i] != 'f') == True:
            raise Exception(ui.HandleErrors(1))

        if HexaToDecimal(number[i]) >= base:
            raise Exception(ui.HandleErrors(3))


def ValidateBase(base: str):
    base = int(base)
    if base < 2 or base > 17:
        raise Exception(ui.HandleErrors(2))


def ValidateBasesForSuccessiveDivisions(sourceBase: int, destinationBase: int):
    if sourceBase < destinationBase:
        raise Exception(ui.HandleErrors(5))


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
