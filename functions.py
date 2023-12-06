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
    # Making sure that y is the operand with one digit in hexadecimal format
    if IsHexadecimal(y) == False:
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
    ValidateOperandsForMultiplication(x, y)

    ans = MultiplyNumbers(x, y, base)
    return ans


def DivideNumbers(x: str, y: str, base: int) -> (str, str):
    cpy = x

    x = BaseXToBase10(x, base)
    x = int(x)
    x //= HexaToDecimal(y)

    quotient = Base10ToBaseX(str(x), base)
    remainder = SubtractNumbers(cpy, MultiplyNumbers(quotient, y, base), base)

    return quotient, remainder


def ManageDivideNumbers() -> (str, str):
    base = ui.InputBase()
    x = ui.InputFirstNumber()
    y = ui.InputSecondNumber()

    ValidateBase(base)
    base = int(base)
    ValidateNumber(x, base)
    ValidateNumber(y, base)
    ValidateOperandsForDivision(y)

    quotient, remainder = DivideNumbers(x, y, base)
    return quotient, remainder


def ConvertUsingSuccessiveDivisions(x: str, sourceBase: int, destinationBase: int) -> str:
    ans = ""

    while x != "0":
        remainder, quotient = DivideNumbers(x, DecimalToHexa(destinationBase), sourceBase)
        x = remainder
        ans = quotient + ans

    return ans


def ManageConvertUsingSuccessiveDivisions() -> str:
    sourceBase = ui.InputSourceBase()
    destinationBase = ui.InputDestinationBase()
    x = ui.InputNumber()

    ValidateBase(sourceBase)
    ValidateBase(destinationBase)
    sourceBase = int(sourceBase)
    destinationBase = int(destinationBase)
    ValidateNumber(x, sourceBase)
    ValidateBasesForSuccessiveDivisions(sourceBase, destinationBase)

    ans = ConvertUsingSuccessiveDivisions(x, sourceBase, destinationBase)
    return ans


def BaseXToBase10(x: str, sourceBase: int) -> str:
    ans, pow = 0, 1
    for i in range(len(x) - 1, -1, -1):
        ans = ans + pow * HexaToDecimal(x[i])
        pow *= sourceBase

    return str(ans)


def Base10ToBaseX(x: str, sourceBase: int) -> str:
    # Edge case
    if x == "0":
        return "0"

    x = int(x)
    ans = ""
    while x != 0:
        ans = str(DecimalToHexa(x % sourceBase)) + ans
        x //= sourceBase

    return ans


def ConvertUsing10AsIntermediaryBase(x: str, sourceBase: int, destinationBase: int) -> str:
    ans = BaseXToBase10(x, sourceBase)
    ans = Base10ToBaseX(ans, destinationBase)
    return ans


def ManageConvertUsing10AsIntermediaryBase() -> str:
    sourceBase = ui.InputSourceBase()
    destinationBase = ui.InputDestinationBase()
    x = ui.InputNumber()

    ValidateBase(sourceBase)
    ValidateBase(destinationBase)
    sourceBase = int(sourceBase)
    destinationBase = int(destinationBase)
    ValidateNumber(x, sourceBase)

    ans = ConvertUsing10AsIntermediaryBase(x, sourceBase, destinationBase)
    return ans


def ConvertUsingRapidConversions(x: str, sourceBase: int, destinationBase: int) -> str:
    ans = ""
    di = {2: 1, 4: 2, 8: 3, 16: 4}

    if sourceBase == 2:
        gap = di[destinationBase]

        x = x[::-1]  # Reversing the string
        li = [x[i : i + gap] for i in range(0, len(x), gap)]  # Slicing the string

        li.reverse()  # Reversing the list

        # Reversing every element from the list
        for i in range(len(li)):
            li[i] = li[i][::-1]

        # Computing the answer
        for i in range(len(li)):
            ans += ConvertUsing10AsIntermediaryBase(li[i], sourceBase, destinationBase)
    else:  # destinationBase = 2
        gap = di[sourceBase]

        for i in range(len(x)):
            temp = ConvertUsing10AsIntermediaryBase(x[i], sourceBase, destinationBase)

            # Adding the leading zeros
            while len(temp) < gap:
                temp = "0" + temp

            ans += temp

    ans = ans.lstrip("0")  # Removing the leading zeros
    return ans


def ManageConvertUsingRapidConversions() -> str:
    sourceBase = ui.InputSourceBase()
    destinationBase = ui.InputDestinationBase()
    x = ui.InputNumber()

    ValidateBase(sourceBase)
    ValidateBase(destinationBase)
    sourceBase = int(sourceBase)
    destinationBase = int(destinationBase)
    ValidateNumber(x, sourceBase)
    ValidateBasesForRapidConversions(sourceBase, destinationBase)

    ans = ConvertUsingRapidConversions(x, sourceBase, destinationBase)
    return ans


def ConvertUsingSubstitutionMethod(x: str, sourceBase: int, destinationBase: int) -> str:
    ans = ""
    pow = "1"

    for i in range(len(x) - 1, - 1, -1):
        temp = MultiplyNumbers(x[i], pow, destinationBase)
        pow = MultiplyNumbers(pow, DecimalToHexa(sourceBase), destinationBase)

        ans = AddNumbers(ans, temp, destinationBase)

    return ans


def ManageConvertUsingSubstitutionMethod() -> str:
    sourceBase = ui.InputSourceBase()
    destinationBase = ui.InputDestinationBase()
    x = ui.InputNumber()

    ValidateBase(sourceBase)
    ValidateBase(destinationBase)
    sourceBase = int(sourceBase)
    destinationBase = int(destinationBase)
    ValidateNumber(x, sourceBase)
    ValidateBasesForSubstitutionMethod(sourceBase, destinationBase)

    ans = ConvertUsingSubstitutionMethod(x, sourceBase, destinationBase)
    return ans


def ValidateNumber(number: str, base: int):
    if number[0] == '0' and len(number) > 1:
        raise Exception(ui.HandleErrors(1))

    for i in range(len(number)):
        if IsHexadecimal(number[i]) == False:
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


def ValidateBasesForSubstitutionMethod(sourceBase: int, destinationBase: int):
    if sourceBase > destinationBase:
        raise Exception(ui.HandleErrors(6))


def ValidateBasesForRapidConversions(sourceBase: int, destinationBase: int):
    if sourceBase != 2 and sourceBase != 4 and sourceBase != 8 and sourceBase != 16:
        raise Exception(ui.HandleErrors(7))
    if destinationBase != 2 and destinationBase != 4 and destinationBase != 8 and destinationBase != 16:
        raise Exception(ui.HandleErrors(7))
    if sourceBase != 2 and destinationBase != 2:
        raise Exception(ui.HandleErrors(7))


def ValidateOperandsForMultiplication(x: str, y: str):
    if IsHexadecimal(x) == False and IsHexadecimal(y) == False:
        raise Exception(ui.HandleErrors(4))


def ValidateOperandsForDivision(y: str):
    if IsHexadecimal(y) == False:
        raise Exception(ui.HandleErrors(8))
    if y == "0":
        raise Exception(ui.HandleErrors(9))


def HexaToDecimal(s: str) -> int:
    if (s == '0' or s == '1' or s == '2' or s == '3' or s == '4' or
        s == '5' or s == '6' or s == '7' or s == '8' or s == '9'):
        return int(s)
    elif s == 'A' or s == 'a':
        return 10
    elif s == 'B' or s == 'b':
        return 11
    elif s == 'C' or s == 'c':
        return 12
    elif s == 'D' or s == 'd':
        return 13
    elif s == 'E' or s == 'e':
        return 14
    elif s == 'F' or s == 'f':
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


def IsHexadecimal(s: str) -> bool:
    return (s == '0' or s == '1' or s == '2' or s == '3' or
            s == '4' or s == '5' or s == '6' or s == '7' or
            s == '8' or s == '9' or s == 'A' or s == 'a' or
            s == 'B' or s == 'b' or s == 'C' or s == 'c' or
            s == 'D' or s == 'd' or s == 'E' or s == 'e' or
            s == 'F' or s == 'f')
