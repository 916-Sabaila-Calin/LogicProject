import functions as functions


def RunAllTests():
    TestAddNumbers()
    TestMultiplyNumbers()
    TestSubtractNumbers()


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