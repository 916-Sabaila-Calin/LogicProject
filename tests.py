import functions as functions


def RunAllTests():
    TestAddNumbers()
    TestMultiplyNumbers()
    TestSubtractNumbers()
    TestDivideNumbers()

    TestConvertUsing10AsIntermediaryBase()
    TestConvertUsingSubstitutionMethod()
    TestConvertUsingRapidConversions()
    TestConvertUsingSuccessiveDivisions()

    TestBaseXToBase10()
    TestBase10ToBaseX()


def TestAddNumbers():
    assert functions.AddNumbers("4234", "525532", 7) == "533066"
    assert functions.AddNumbers("4323FFED2", "42AD", 16) == "43240417F"
    assert functions.AddNumbers("1543264745", "41264527846", 9) == "42817803702"
    assert functions.AddNumbers("1010110101", "1010101110111110", 2) == "1010111001110011"
    assert functions.AddNumbers("4132121", "312123", 5) == "4444244"


def TestMultiplyNumbers():
    assert functions.MultiplyNumbers("421352", "6", 7) == "3462135"
    assert functions.MultiplyNumbers("31AFF", "A", 16) == "1F0DF6"
    assert functions.MultiplyNumbers("B", "31FEE31AD2", 16) == "225F3C22706"
    assert functions.MultiplyNumbers("6666666666666", "6", 7) == "56666666666661"
    assert functions.MultiplyNumbers("5", "23412", 7) == "153663"


def TestSubtractNumbers():
    assert functions.SubtractNumbers("20", "10", 10) == "10"
    assert functions.SubtractNumbers("54324", "54214", 7) == "110"
    assert functions.SubtractNumbers("32ABB89DF52AFF", "F45AD34B", 16) == "32ABB7A99A57B4"
    assert functions.SubtractNumbers("42AF", "B52CD53A", 16) == "-B52C928B"
    assert functions.SubtractNumbers("10", "10", 10) == "0"


def TestDivideNumbers():
    assert functions.DivideNumbers("4302", "5", 6) == ("522", "4")
    assert functions.DivideNumbers("7", "8", 9) == ("0", "7")
    assert functions.DivideNumbers("32141AAF432E3DC2EF12", "E", 16) == ("393B8C3603A28FBA35C", "A")
    assert functions.DivideNumbers("6", "6", 9) == ("1", "0")
    assert functions.DivideNumbers("5167542662", "1", 8) == ("5167542662", "0")


def TestConvertUsing10AsIntermediaryBase():
    assert functions.ConvertUsing10AsIntermediaryBase("25341321", 6, 12) == "337841"
    assert functions.ConvertUsing10AsIntermediaryBase("10101010101", 2, 2) == "10101010101"
    assert functions.ConvertUsing10AsIntermediaryBase("101010101101110101", 2, 16) == "2AB75"
    assert functions.ConvertUsing10AsIntermediaryBase("5345261151", 8, 14) == "6D180105"
    assert functions.ConvertUsing10AsIntermediaryBase("613472A", 11, 3) == "202101202102121"


def TestConvertUsingSubstitutionMethod():
    assert functions.ConvertUsingSubstitutionMethod("10101100011101", 2, 16) == "2B1D"
    assert functions.ConvertUsingSubstitutionMethod("41234124132", 5, 10) == "42098667"
    assert functions.ConvertUsingSubstitutionMethod("76254313232", 8, 12) == "1755BA378A"
    assert functions.ConvertUsingSubstitutionMethod("4A", 15, 16) == "46"
    assert functions.ConvertUsingSubstitutionMethod("524635153456", 10, 16) == "7A26B12430"


def TestConvertUsingRapidConversions():
    assert functions.ConvertUsingRapidConversions("1010101101010", 2, 8) == "12552"
    assert functions.ConvertUsingRapidConversions("101010110101010101011010", 2, 16) == "AB555A"
    assert functions.ConvertUsingRapidConversions("101010110", 2, 2) == "101010110"
    assert functions.ConvertUsingRapidConversions("32132131212", 4, 2) == "1110011110011101100110"
    assert functions.ConvertUsingRapidConversions("BAF3EC43", 16, 2) == "10111010111100111110110001000011"


def TestConvertUsingSuccessiveDivisions():
    assert functions.ConvertUsingSuccessiveDivisions("2B1D", 16, 2) == "10101100011101"
    assert functions.ConvertUsingSuccessiveDivisions("42098667", 10, 5) == "41234124132"
    assert functions.ConvertUsingSuccessiveDivisions("1755BA378A", 12, 8) == "76254313232"
    assert functions.ConvertUsingSuccessiveDivisions("46", 16, 15) == "4A"
    assert functions.ConvertUsingSuccessiveDivisions("7A26B12430", 16, 10) == "524635153456"


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
