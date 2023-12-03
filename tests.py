import functions as functions


def RunAllTests():
    TestAddNumbers()
    TestMultiplyNumbers()
    TestSubtractNumbers()

    TestToBase10()


def TestAddNumbers():
    assert functions.AddNumbers("4234", "525532", 7) == "533066"


def TestMultiplyNumbers():
    assert functions.MultiplyNumbers("421352", "6", 7) == "3462135"


def TestSubtractNumbers():
    assert functions.SubtractNumbers("20", "10", 10) == "10"
    assert functions.SubtractNumbers("54324", "54214", 7) == "110"
    assert functions.SubtractNumbers("32ABB89DF52AFF", "F45AD34B", 16) == "32ABB7A99A57B4"
    assert functions.SubtractNumbers("42AF", "B52CD53A", 16) == "-B52C928B"
    assert functions.SubtractNumbers("10", "10", 10) == "0"


def TestToBase10():
    assert functions.ToBase10("0", 5) == "0"
    assert functions.ToBase10("10101011101111101101001", 2) == "5627753"
    assert functions.ToBase10("61456236", 8) == "12999838"
    assert functions.ToBase10("143252353", 10) == "143252353"
    assert functions.ToBase10("43AD2CC3F86D", 16) == "74411059443821"