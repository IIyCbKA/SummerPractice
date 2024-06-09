from functions import *


def test_TimeRounding():
    firstInput: list = [14, 21, 45]
    assert TimeRounding(*firstInput) == '14 ч'

    secondInput: list = [9, 59, 23]
    assert TimeRounding(*secondInput) == '10 ч'


def test_ReturnAgeText():
    firstInput: int = 11
    assert ReturnAgeText(firstInput) == 'Мне 11 лет'

    secondInput: int = 1
    assert ReturnAgeText(secondInput) == 'Мне 1 год'

    thirdInput: int = 21
    assert ReturnAgeText(thirdInput) == 'Мне 21 год'

    fourthInput: int = 30
    assert ReturnAgeText(fourthInput) == 'Мне 30 лет'

    fifthInput: int = 42
    assert ReturnAgeText(fifthInput) == 'Мне 42 года'


def test_CalculateAgeDeathForest():
    firstInput: list = [10, 9, 4]
    assert CalculateAgeDeathForest(*firstInput) == 3

    secondInput: list = [10, 10, 4]
    assert CalculateAgeDeathForest(*secondInput) == 4

    thirdInput: list = [1, 100, 2]
    assert CalculateAgeDeathForest(*thirdInput) == 1

    fourthInput: list = [0, 1000, 1]
    assert CalculateAgeDeathForest(*fourthInput) == 0


def test_ReplacingArrayElements():
    firstArray: list = [1, 2, 3, 4, 5]
    first_countFirstNumbers: int = 6
    ReplacingArrayElements(firstArray, first_countFirstNumbers)
    assert firstArray == [1, 2, 3, 4, 5]

    secondArray: list = [1, 2, 3, 4, 5]
    second_countFirstNumbers: int = 3
    ReplacingArrayElements(secondArray, second_countFirstNumbers)
    assert secondArray == [2, 2, 2, 2, 2]

    thirdArray: list = [1, 2, 3, 4, 5]
    third_countFirstNumbers: int = 0
    ReplacingArrayElements(thirdArray, third_countFirstNumbers)
    assert thirdArray == [1, 2, 3, 4, 5]


def allTests():
    test_TimeRounding()
    test_ReturnAgeText()
    test_CalculateAgeDeathForest()
    test_ReplacingArrayElements()


allTests()
