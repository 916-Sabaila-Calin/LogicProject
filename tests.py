import functions as functions


def RunAllTests():
    TestAddNumbers()
    TestMultiplyNumbers()
    TestSubtractNumbers()

    TestConvertUsing10AsIntermediaryBase()

    TestBaseXToBase10()
    TestBase10ToBaseX()


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


def TestConvertUsing10AsIntermediaryBase():
    assert functions.ConvertUsing10AsIntermediaryBase("25341321", 6, 12) == "337841"
    assert functions.ConvertUsing10AsIntermediaryBase("2643572", 10, 10) == "2643572"
    assert functions.ConvertUsing10AsIntermediaryBase("101010101101110101", 2, 16) == "2AB75"
    assert functions.ConvertUsing10AsIntermediaryBase("5345261151", 8, 14) == "6D180105"
    assert functions.ConvertUsing10AsIntermediaryBase("613472A", 11, 3) == "202101202102121"


def TestBaseXToBase10():
    assert functions.BaseXToBase10("234322", 5) == "8712"
    assert functions.BaseXToBase10("10101011101111101101001", 2) == "5627753"
    assert functions.BaseXToBase10("61456236", 8) == "12999838"
    assert functions.BaseXToBase10("143252353", 10) == "143252353"
    assert functions.BaseXToBase10("43AD2CC3F86D", 16) == "74411059443821"


def TestBase10ToBaseX():
    assert functions.Base10ToBaseX("41351", 16) == "A187"
    assert functions.Base10ToBaseX("26453", 2) == "110011101010101"
    assert functions.Base10ToBaseX("143252353", 10) == "143252353"
    assert functions.Base10ToBaseX("12999838", 8) == "61456236"
    assert functions.Base10ToBaseX("2642313211", 12) == "618AA4537"