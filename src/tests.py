from functions import *


def test_TimeRounding():
    firstInput: list = [14, 21, 45]
    assert TimeRounding(*firstInput) == '14 ч 22 м или 14 ч'

    secondInput: list = [9, 59, 23]
    assert TimeRounding(*secondInput) == '9 ч 59 м или 10 ч'


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
    firstArrayLength: int = 5
    firstArray: list = [1, 2, 3, 4, 5]
    first_countFirstNumbers: int = 6
    ReplacingArrayElements(firstArrayLength, firstArray,
                           first_countFirstNumbers)
    assert firstArray == [1, 2, 3, 4, 5]

    secondArrayLength: int = 5
    secondArray: list = [1, 2, 3, 4, 5]
    second_countFirstNumbers: int = 3
    ReplacingArrayElements(secondArrayLength, secondArray,
                           second_countFirstNumbers)
    assert secondArray == [2, 2, 2, 2, 2]

    thirdArrayLength: int = 5
    thirdArray: list = [1, 2, 3, 4, 5]
    third_countFirstNumbers: int = 0
    ReplacingArrayElements(thirdArrayLength, thirdArray,
                           third_countFirstNumbers)
    assert thirdArray == [1, 2, 3, 4, 5]


def test_ComposePolynoms():
    firstPolyP: list = [2, 0, -5]
    firstPolyQ: list = [1, -1, 2]
    assert ComposePolynoms(firstPolyP, firstPolyQ) == [2, -4, 10, -8, 3]

    secondPolyP: list = [1, 2]
    secondPolyQ: list = [2, -5]
    assert ComposePolynoms(secondPolyP, secondPolyQ) == [2, -3]

    thirdPolyP: list = [1]
    thirdPolyQ: list = [2, 0, 11]
    assert ComposePolynoms(thirdPolyP, thirdPolyQ) == [1]

    fourthPolyP: None = None
    fourthPolyQ: list = [2, 0, 11]
    assert ComposePolynoms(fourthPolyP, fourthPolyQ) is None

    fifthPolyP: list = [2, 0, 11]
    fifthPolyQ: None = None
    assert ComposePolynoms(fifthPolyP, fifthPolyQ) == [11]


def test_SearchLargestArithOrGeomProgression():
    lengthFirstArray: int = 5
    firstArray: list = [1, 3, 5, 7, 9]
    assert SearchLargestArithOrGeomProgression(lengthFirstArray,
                                               firstArray) == 5

    lengthSecondArray: int = 5
    secondArray: list = [2, 1, 3, 5, 9]
    assert SearchLargestArithOrGeomProgression(lengthSecondArray,
                                               secondArray) == 3

    lengthThirdArray: int = 7
    thirdArray: list = [2, 4, 1, 3, 9, 27, 7]
    assert SearchLargestArithOrGeomProgression(lengthThirdArray,
                                               thirdArray) == 4

    lengthFourthArray: int = 4
    fourthArray: list = [3, 4, 11, 2]
    assert SearchLargestArithOrGeomProgression(lengthFourthArray,
                                               fourthArray) == 2

    lengthFifthArray: int = 5
    fifthArray: list = [1, 2, 4, 8, 16]
    assert SearchLargestArithOrGeomProgression(lengthFifthArray,
                                               fifthArray) == 5

    lengthSixthArray: int = 2
    sixthArray: list = [1, 12]
    assert SearchLargestArithOrGeomProgression(lengthSixthArray,
                                               sixthArray) == 2

    lengthSeventhArray: int = 6
    seventhArray: list = [8, 9, 10, 12, 14, 16]
    assert SearchLargestArithOrGeomProgression(lengthSeventhArray,
                                               seventhArray) == 4


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


def test_FindMedianXY():
    # формат координат [x, y]
    firstCountDots: int = 4
    firstDots: list = [[3, 4], [1, 2], [7, 8], [5, 6]]
    assert FindMedianXY(firstCountDots, firstDots) == [4.00, 5.00]

    secondCountDots: int = 5
    secondDots: list = [[4, 6], [1, 7], [10, 20], [11, 13], [18, 26]]
    assert FindMedianXY(secondCountDots, secondDots) == [10, 13]

    thirdCountDots: int = 1
    thirdDots: list = [[10, 20]]
    assert FindMedianXY(thirdCountDots, thirdDots) == [10, 20]

    fourthCountDots: int = 4
    fourthDots: list = [[4.5, 5.4], [1.1, 7.2], [11.3, 5.4], [12.3, 7.7]]
    assert FindMedianXY(fourthCountDots, fourthDots) == [7.90, 6.30]

    fifthCountDots: int = 0
    fifthDots: list = []
    assert FindMedianXY(fifthCountDots, fifthDots) == []


def test_BinaryArrayCompression():
    firstArray: list = [1, 1, 1, 0, 0, 1]
    assert BinaryArrayCompression(firstArray) == [3, 2, 1]

    secondArray: list = [1, 0, 1, 0, 1, 0]
    assert BinaryArrayCompression(secondArray) == [1, 1, 1, 1, 1, 1]

    thirdArray: list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
    assert BinaryArrayCompression(thirdArray) == [15, 0, 2]

    fourthArray: list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    assert BinaryArrayCompression(fourthArray) == [15, 2, 1, 1]

    fifthArray: list = []
    assert BinaryArrayCompression(fifthArray) == []


def test_CorrectionText():
    firstText: str = '( Привет, Андрей ) , - говорил он'
    assert CorrectionText(firstText) == '(Привет, Андрей), - говорил он'

    secondText: str = '(Да \n? Ты в этом уверен ? )'
    assert CorrectionText(secondText) == '(Да? Ты в этом уверен?)'

    thirdText: str = '( ( Проверю на скобках ) )'
    assert CorrectionText(thirdText) == '((Проверю на скобках))'

    fourthText: str = ''
    assert CorrectionText(fourthText) == ''

    fifthText: str = 'Да , забавно   (получается)'
    assert CorrectionText(fifthText) == 'Да, забавно (получается)'

    sixthText: str = '(       Чек        ) , посмотрим'
    assert CorrectionText(sixthText) == '(Чек), посмотрим'


def allTests():
    test_TimeRounding()
    test_ReturnAgeText()
    test_CalculateAgeDeathForest()
    test_ReplacingArrayElements()
    test_ComposePolynoms()
    test_SearchLargestArithOrGeomProgression()
    test_SearchNaturalNumsWithSortedDigits()
    test_FindMedianXY()
    test_BinaryArrayCompression()
    test_CorrectionText()


allTests()
