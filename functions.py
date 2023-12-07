import user_interface as ui


def AddNumbers(x: str, y: str, base: int) -> str:
    """
    This function adds two numbers in a specified base
    :param x: a string representing the first operand of the addition
    :param y: a string representing the second operand of the addition
    :param base: an integer representing the base in which the addition will take place
    :return: a string representing the result of the addition of the two numbers
    """

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

        carry = temp // base
        ans += DecimalToHexa(temp % base)

    if carry > 0:
        ans += DecimalToHexa(carry)

    ans = ans[::-1]  # Reversing the string
    return ans


def ManageAddNumbers() -> str:
    """
    This function takes in and validates all parameters for the AddNumbers function
    :return: a string representing the result of the addition of the two numbers, if no exceptions are raised
    """

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
    """
    This function subtracts two numbers in a specified base
    :param x: a string representing the first operand of the subtraction
    :param y: a string representing the second operand of the subtraction
    :param base: an integer representing the base in which the subtraction will take place
    :return: a string representing the result of the subtraction of the two numbers
    """

    # Edge case
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
    """
    This function takes in and validates all parameters for the SubtractNumbers function
    :return: a string representing the result of the subtraction of the two numbers, if no exceptions are raised
    """

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
    """
    This function multiplies two numbers in a specified base
    :param x: a string representing the first operand of the multiplication
    :param y: a string representing the second operand of the multiplication, which
             must be a digit in the hexadecimal format
    :param base: an integer representing the base in which the multiplication will take place
    :return: a string representing the result of the multiplication of the two numbers
    """

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

        carry = temp // base
        ans += DecimalToHexa(temp % base)

    if carry > 0:
        ans += DecimalToHexa(carry)

    ans = ans[::-1]
    return ans


def ManageMultiplyNumbers() -> str:
    """
    This function takes in and validates all parameters for the MultiplyNumbers function
    :return: a string representing the result of the multiplication of the two numbers, if no exceptions are raised
    """

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
    """
    This function divides two numbers in a specified base
    :param x: a string representing the first operand of the division
    :param y: a string representing the second operand of the division, which
             must be a digit in the hexadecimal format
    :param base: an integer representing the base in which the division will take place
    :return: a tuple of strings representing the quotient and the remainder
    """

    cpy = x

    x = BaseXToBase10(x, base)
    x = int(x)
    x //= HexaToDecimal(y)

    quotient = Base10ToBaseX(str(x), base)
    remainder = SubtractNumbers(cpy, MultiplyNumbers(quotient, y, base), base)

    return quotient, remainder


def ManageDivideNumbers() -> (str, str):
    """
    This function takes in and validates all parameters for the DivideNumbers function
    :return: a tuple of strings representing the quotient and the remainder, if no exceptions are raised
    """

    base = ui.InputBase()
    x = ui.InputFirstNumber()
    y = ui.InputSecondNumber()

    ValidateBase(base)
    base = int(base)
    ValidateNumber(x, base)
    ValidateNumber(y, base)
    ValidateOperandForDivision(y)

    quotient, remainder = DivideNumbers(x, y, base)
    return quotient, remainder


def ConvertUsingSuccessiveDivisions(x: str, sourceBase: int, destinationBase: int) -> str:
    """
    This function converts a number from a source base to a destination base, using the successive divisions method
    The source base should be greater of equal than the destination base
    :param x: a string representing the number that will be converted
    :param sourceBase: an integer representing the base of the number that will be converted
    :param destinationBase: an integer representing the base in which the number will be converted
    :return: a string representing the converted number
    """

    ans = ""

    while x != "0":
        remainder, quotient = DivideNumbers(x, DecimalToHexa(destinationBase), sourceBase)
        x = remainder
        ans = quotient + ans

    return ans


def ManageConvertUsingSuccessiveDivisions() -> str:
    """
    This function takes in and validates all parameters for the ConvertUsingSuccessiveDivisions function
    :return: a string representing the converted number, if no exceptions are raised
    """

    sourceBase = ui.InputSourceBase()
    destinationBase = ui.InputDestinationBase()
    x = ui.InputNumber()

    ValidateBase(sourceBase)
    ValidateBase(destinationBase)
    sourceBase = int(sourceBase)
    destinationBase = int(destinationBase)
    ValidateNumber(x, sourceBase)
    ValidateBasesForSuccessiveDivisionsMethod(sourceBase, destinationBase)

    ans = ConvertUsingSuccessiveDivisions(x, sourceBase, destinationBase)
    return ans


def BaseXToBase10(x: str, sourceBase: int) -> str:
    """
    This function converts a number from a source base to base 10
    :param x: a string representing the number that will be converted
    :param sourceBase: an integer representing the base of the number that will be converted
    :return: a string representing the converted number
    """

    ans, pow = 0, 1
    for i in range(len(x) - 1, -1, -1):
        ans = ans + pow * HexaToDecimal(x[i])
        pow *= sourceBase

    return str(ans)


def Base10ToBaseX(x: str, destinationBase: int) -> str:
    """
    This function converts a number from base 10 to a destination base
    :param x: a string representing the number that will be converted
    :param destinationBase: an integer representing the base in which the number will be converted
    :return: a string representing the converted number
    """

    # Edge case
    if x == "0":
        return "0"

    x = int(x)
    ans = ""
    while x != 0:
        ans = str(DecimalToHexa(x % destinationBase)) + ans
        x //= destinationBase

    return ans


def ConvertUsing10AsIntermediaryBase(x: str, sourceBase: int, destinationBase: int) -> str:
    """
    This function converts a number from a source base to a destination base, using 10 as an intermediary base
    :param x: a string representing the number that will be converted
    :param sourceBase: an integer representing the base of the number that will be converted
    :param destinationBase: an integer representing the base in which the number will be converted
    :return: a string representing the converted number
    """

    ans = BaseXToBase10(x, sourceBase)
    ans = Base10ToBaseX(ans, destinationBase)
    return ans


def ManageConvertUsing10AsIntermediaryBase() -> str:
    """
    This function takes in and validates all parameters for the ConvertUsing10AsIntermediaryBase function
    :return: a string representing the converted number, if no exceptions are raise
    """

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
    """
    This function converts a number from a source base to a destination base, using rapid conversions
    At least one of the bases should be 2
    :param x: a string representing the number that will be converted
    :param sourceBase: an integer (2, 4, 8, or 16) representing the base of the number that will be converted
    :param destinationBase: an integer (2, 4, 8, or 16) representing the base in which the number will be converted
    :return: a string representing the converted number
    """

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
    """
    This function takes in and validates all parameters for the ConvertUsingRapidConversions function
    :return: a string representing the converted number, if no exceptions are raised
    """

    sourceBase = ui.InputSourceBase()
    destinationBase = ui.InputDestinationBase()
    x = ui.InputNumber()

    ValidateBase(sourceBase)
    ValidateBase(destinationBase)
    sourceBase = int(sourceBase)
    destinationBase = int(destinationBase)
    ValidateNumber(x, sourceBase)
    ValidateBasesForRapidConversionsMethod(sourceBase, destinationBase)

    ans = ConvertUsingRapidConversions(x, sourceBase, destinationBase)
    return ans


def ConvertUsingSubstitutionMethod(x: str, sourceBase: int, destinationBase: int) -> str:
    """
    This function converts a number from a source base to a destination base, using ths substitution method
    The source base should be less or equal than the destination base
    :param x: a string representing the number that will be converted
    :param sourceBase: an integer representing the base of the number that will be converted
    :param destinationBase: an integer representing the base in which the number will be converted
    :return: a string representing the converted number
    """

    ans = ""
    pow = "1"

    for i in range(len(x) - 1, - 1, -1):
        temp = MultiplyNumbers(x[i], pow, destinationBase)
        pow = MultiplyNumbers(pow, DecimalToHexa(sourceBase), destinationBase)

        ans = AddNumbers(ans, temp, destinationBase)

    return ans


def ManageConvertUsingSubstitutionMethod() -> str:
    """
    This function takes in and validates all parameters for the ConvertUsingSubstitutionMethod function
    :return: a string representing the converted number, if no exceptions are raised
    """

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
    """
    This function validates a number of a given base
    :param number: a string representing a number
    :param base: an integer representing the base of the number
    :return: -, if no exceptions are raised
    :raise: - an exception with the string message "Error: The input is invalid!", if the number start with a 0
            - an exception with the string message "Error: The input is invalid!", if the number
              does not contain hexadecimal digits
            - an exception with the string message "Error: The digits of the number cannot be greater or equal than
              the base!", if the hexadecimal digits of the number are greater or equal than the base
    """

    if number[0] == '0' and len(number) > 1:
        raise Exception(ui.HandleErrors(1))

    for i in range(len(number)):
        if IsHexadecimal(number[i]) == False:
            raise Exception(ui.HandleErrors(1))

        if HexaToDecimal(number[i]) >= base:
            raise Exception(ui.HandleErrors(3))


def ValidateBase(base: str):
    """
    This function validates a given base
    :param base: a string representing a base
    :return: -, if no exceptions are raised
    :raise: - an exception with the string message "invalid literal for int() with base 10: 'user_input'", if the base
              cannot be converted to an integer
            - an exception with the string message "Error: The base is not between 2 and 16!", if the base is not
              between 2 and 16
    """

    base = int(base)
    if base < 2 or base > 17:
        raise Exception(ui.HandleErrors(2))


def ValidateBasesForSuccessiveDivisionsMethod(sourceBase: int, destinationBase: int):
    """
    This function validates two bases for the conversions using the successive divisions method
    :param sourceBase: an integer representing the source base
    :param destinationBase: an integer representing the destination base
    :return: -, if no exceptions are raised
    :raise: an exception with the string message "Error: The source base should be greater or equal than the
            destination base!", if the source base is less than the destination base
    """

    if sourceBase < destinationBase:
        raise Exception(ui.HandleErrors(5))


def ValidateBasesForSubstitutionMethod(sourceBase: int, destinationBase: int):
    """
    This function validates two bases for the conversions using the substitution method
    :param sourceBase: an integer representing the source base
    :param destinationBase: an integer representing the destination base
    :return: -, if no exceptions are raised
    :raise: an exception with the string message "Error: The source base should be less or equal than the
            destination base!", if the source base is greater than the destination base
    """

    if sourceBase > destinationBase:
        raise Exception(ui.HandleErrors(6))


def ValidateBasesForRapidConversionsMethod(sourceBase: int, destinationBase: int):
    """
    This function validates two bases for the conversions using the rapid conversion method
    :param sourceBase: an integer representing the source base
    :param destinationBase: an integer representing the destination base
    :return: -, if no exceptions are raised
    :raise: an exception with the string message "Error: Cannot do rapid conversions using the provided bases!", if
            one of the bases does not belong to the set {2, 4, 8, 16}, or if one of the bases is not 2
    """

    if sourceBase != 2 and sourceBase != 4 and sourceBase != 8 and sourceBase != 16:
        raise Exception(ui.HandleErrors(7))
    if destinationBase != 2 and destinationBase != 4 and destinationBase != 8 and destinationBase != 16:
        raise Exception(ui.HandleErrors(7))
    if sourceBase != 2 and destinationBase != 2:
        raise Exception(ui.HandleErrors(7))


def ValidateOperandsForMultiplication(x: str, y: str):
    """
    This function validates two operands for multiplications
    :param x: a string representing the first operand
    :param y: a string representing the second operand
    :return: -, if no exceptions are raised
    :raise: an exception with the string message "Error: At least one of the operands should have one digit in the
            hexadecimal format!", if at least one of the operands is not composed of a single hexadecimal digit
    """

    if IsHexadecimal(x) == False and IsHexadecimal(y) == False:
        raise Exception(ui.HandleErrors(4))


def ValidateOperandForDivision(y: str):
    """
    This function validates an operand for divisions
    :param y: a string representing the operand
    :return: -, if no exceptions are raised
    :raise: - an exception with the string message "Error: The divisor should have one digit!", if the number is not
              composed of a single hexadecimal digit
            - an exception with the string message :Error: Cannot divide by 0!", if the number is "0"
    """

    if IsHexadecimal(y) == False:
        raise Exception(ui.HandleErrors(8))
    if y == "0":
        raise Exception(ui.HandleErrors(9))


def HexaToDecimal(s: str) -> int:
    """
    This function converts a hexadecimal digit to its correspondent in base 10
    The hexadecimal digit should belong to the set {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'A', 'b',
                                                    'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F'}
    :param s: a string representing the hexadecimal digit
    :return: an integer representing the hexadecimal digit's correspondent in base 10
    """

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
    """
    This function converts a decimal number to a hexadecimal digit
    The decimal number should be between 0 and 15
    :param num: an integer representing the decimal number
    :return: a string representing the hexadecimal digit
    """

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
    """
    This function checks is a string is a hexadecimal digit
    :param s: a string
    :return: True if the string is a hexadecimal digit, False otherwise
    """

    return (s == '0' or s == '1' or s == '2' or s == '3' or
            s == '4' or s == '5' or s == '6' or s == '7' or
            s == '8' or s == '9' or s == 'A' or s == 'a' or
            s == 'B' or s == 'b' or s == 'C' or s == 'c' or
            s == 'D' or s == 'd' or s == 'E' or s == 'e' or
            s == 'F' or s == 'f')
