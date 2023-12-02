import functions as functions


def RunAllTests():
    TestAddNumbers()
    TestMultiplyNumbers()


def TestAddNumbers():
    assert functions.AddNumbers("4234", "525532", 7) == "533066"


def TestMultiplyNumbers():
    assert functions.MultiplyNumbers("421352", "6", 7) == "3462135"