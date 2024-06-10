from algorithms import *


# максимально смешное условие, которое можно двояко интерпретировать
# решение соответствует условию
def TimeRounding(hours: int, minutes: int, seconds: int) -> str:
    if minutes >= 30:
        return f'{hours + 1} ч'
    else:
        return f'{hours} ч'


# опять задачка со смешным условием и не менее смешным решением...
def ReturnAgeText(age: int) -> str:
    if (10 < age % 100 < 20) or (age % 10 >= 5) or (age % 10 == 0):
        return f'Мне {age} лет'
    elif age % 10 == 1:
        return f'Мне {age} год'
    else:
        return f'Мне {age} года'


# нет уточнения того, что сначала делать - отнимать план или увеличивать площадь
# решение опять соответствует условию...
def CalculateAgeDeathForest(area: int, growth: int, plan: int) -> int:
    countAge: int = 0
    while area > 0:
        area = area * (1 + growth / 100) - plan
        countAge += 1

    return countAge


# странная задачка без логики, никогда не используемая в продуктовых решениях
def ReplacingArrayElements(array: list, countFirstNumbers: int) -> None:
    lengthArray: int = len(array)

    if (countFirstNumbers > lengthArray) | (countFirstNumbers == 0):
        return

    firstNumsSum: int = 0
    for ind in range(0, countFirstNumbers):
        firstNumsSum += array[ind]

    firstNumsAverage: float = firstNumsSum / countFirstNumbers

    for ind in range(0, lengthArray):
        array[ind] = firstNumsAverage


# гнилое задание, написаное поверхностными словами
def CalculateCoefCompositionPolynomial():
    pass


# более-менее норм задачка, в которой просто нужно в алгом
def SearchLargestArithOrGeomProgression(array: list) -> int:
    arrayLength: int = len(array)

    if arrayLength <= 2:
        return arrayLength

    largestArith: int = SearchLargestProgression(array, arrayLength, True)
    largestGeom: int = SearchLargestProgression(array, arrayLength, False)
    largestProgression: int = max(largestArith, largestGeom)

    return largestProgression


# интересная задачка, нужно немного подумать над алгомом для норм скорости,
# в код не стал упарываться, получился овер некрасивым,
# а вот в скорость оч неплохо вышло
def SearchNaturalNumsWithSortedDigits(limit: int) -> int:
    countRightNums: int = 0
    for startNum in range(1, 10):
        countRightNums += FindRightNums(str(startNum), limit, None)

    return countRightNums
