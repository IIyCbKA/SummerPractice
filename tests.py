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


def test_CalculateCoefCompositionPolynomial():
    pass


def test_SearchLargestArithOrGeomProgression():
    firstArray: list = [1, 3, 5, 7, 9]
    assert SearchLargestArithOrGeomProgression(firstArray) == 5

    secondArray: list = [2, 1, 3, 5, 9]
    assert SearchLargestArithOrGeomProgression(secondArray) == 3

    thirdArray: list = [2, 4, 1, 3, 9, 27, 7]
    assert SearchLargestArithOrGeomProgression(thirdArray) == 4

    fourthArray: list = [3, 4, 11, 2]
    assert SearchLargestArithOrGeomProgression(fourthArray) == 2

    fifthArray: list = [1, 2, 4, 8, 16]
    assert SearchLargestArithOrGeomProgression(fifthArray) == 5

    sixthArray: list = [1, 12]
    assert SearchLargestArithOrGeomProgression(sixthArray) == 2

    seventhArray: list = [8, 9, 10, 12, 14, 16]
    assert SearchLargestArithOrGeomProgression(seventhArray) == 4


def test_SearchNaturalNumsWithSortedDigits():
    firstLimit: int = 50
    assert SearchNaturalNumsWithSortedDigits(firstLimit) == 46

    secondLimit: int = 100
    assert SearchNaturalNumsWithSortedDigits(secondLimit) == 90

    thirdLimit: int = 500
    assert SearchNaturalNumsWithSortedDigits(thirdLimit) == 174

    fourthLimit: int = 1000
    assert SearchNaturalNumsWithSortedDigits(fourthLimit) == 294

    fifthLimit: int = 10000000
    assert SearchNaturalNumsWithSortedDigits(fifthLimit) == 1458


def allTests():
    test_TimeRounding()
    test_ReturnAgeText()
    test_CalculateAgeDeathForest()
    test_ReplacingArrayElements()
    test_CalculateCoefCompositionPolynomial()
    test_SearchLargestArithOrGeomProgression()
    test_SearchNaturalNumsWithSortedDigits()


allTests()
