from algorithms import *
import numpy as np
import re


# максимально смешное условие, которое можно двояко интерпретировать
# решение соответствует условию
def TimeRounding(hours: int, minutes: int, seconds: int) -> str:
    only_hours: str = f'{hours + 1 if minutes >= 30 else hours} ч'
    hours_with_minutes: str = \
        f'{hours} ч {minutes + 1 if seconds >= 30 else minutes} м'
    result: str = f'{hours_with_minutes} или {only_hours}'

    return result


# опять задачка со смешным условием и не менее смешным решением...
def ReturnAgeText(age: int) -> str:
    if (10 < age % 100 < 20) or (age % 10 >= 5) or (age % 10 == 0):
        correctForm: str = 'лет'
    elif age % 10 == 1:
        correctForm: str = 'год'
    else:
        correctForm: str = 'года'
    result: str = f'Мне {age} {correctForm}'

    return result


# нет уточнения того, что сначала делать - отнимать план или увеличивать площадь
# решение опять соответствует условию...
def CalculateAgeDeathForest(area: int, growth: int, plan: int) -> int:
    countAge: int = 0
    while area > 0:
        area = area * (1 + growth / 100) - plan
        countAge += 1

    return countAge


# странная задачка без логики, никогда не используемая в продуктовых решениях
def ReplacingArrayElements(lengthArray: int, array: list,
                           countFirstNumbers: int) -> None:
    if (countFirstNumbers > lengthArray) | (countFirstNumbers == 0):
        return

    firstNumsSum: int = 0
    for ind in range(0, countFirstNumbers):
        firstNumsSum += array[ind]

    firstNumsAverage: float = firstNumsSum / countFirstNumbers

    for ind in range(0, lengthArray):
        array[ind] = firstNumsAverage


# Гнилое задание, сильный упор в мат, хотя информации в интернете очень мало.
# Хорошо, что есть numpy...
def ComposePolynoms(coefsP: list | None, coefsQ: list | None) -> list | None:
    if coefsP is None:
        result: None = None
    elif coefsQ is None:
        result: list = [coefsP[-1]]
    else:
        PolynomP = np.poly1d(coefsP)
        PolynomQ = np.poly1d(coefsQ)
        composedPolynom = PolynomP(PolynomQ)
        result: list = composedPolynom.coefficients.tolist()

    return result


# более-менее норм задачка, в которой просто нужно в алгом
def SearchLargestArithOrGeomProgression(lengthArray: int, array: list) -> int:
    if lengthArray <= 2:
        largestProgression: int = lengthArray
    else:
        largestArith: int = SearchLargestProgression(
            array, lengthArray, True)
        largestGeom: int = SearchLargestProgression(
            array, lengthArray, False)
        largestProgression: int = max(largestArith, largestGeom)

    return largestProgression


# интересная задачка, нужно немного подумать над алгомом для норм скорости,
# в код не стал упарываться, получился over некрасивым,
# а вот в скорость оч неплохо вышло
def SearchNaturalNumsWithSortedDigits(limit: int) -> int:
    countRightNums: int = 0
    for startNum in range(1, 10):
        countRightNums += FindRightNums(str(startNum), limit, None)

    return countRightNums


# не совсем понятное условие без примеров, решение методом тыка (вроде так)
def FindMedianXY(countDots: int, arrayDots: list) -> list:
    halfLength: int = countDots // 2
    arrayResult: list = []

    if countDots > 0:
        # вертикальная
        sortedArraysByIndexAndAddResult(arrayDots, arrayResult, countDots,
                                        halfLength, 0)

        # горизонтальная
        sortedArraysByIndexAndAddResult(arrayDots, arrayResult, countDots,
                                        halfLength, 1)

    return arrayResult


# Максимально странная задачка без примеров, которую можно сделать только
# методом тыка. А как иначе...
def BinaryArrayCompression(array: list) -> list:
    currentBit: int | None = None
    currentBitCount: int = 0
    compressionArray: list = []

    for bit in array:
        if currentBit is None:
            currentBit = bit
            currentBitCount += 1
        elif bit == currentBit:
            currentBitCount += 1
        else:
            addChainLengthToCompressedArray(currentBitCount, compressionArray)
            currentBitCount = 1
            currentBit = bit

    if currentBitCount > 0:
        addChainLengthToCompressedArray(currentBitCount, compressionArray)

    return compressionArray


# довольно приятная задачка с простым решением на первый взгляд,
# но для оптимизации необходимо сделать решение без replace
def CorrectionText(text: str) -> str:
    # Убираем лишние пробелы после знаков препинания .,;:!?)]}
    text = re.sub(r'\s+([.,;:!?)}\]])', r'\1', text)

    # Добавляем недостающие пробелы после знаков препинания .,;:!?)]}
    text = re.sub(r'([.,;:!?)}\]])([^\s.,;:!?)}\]])', r'\1 \2', text)

    # Убираем пробелы после открывающих скобок
    text = re.sub(r'(\(\s+)', '(', text)
    text = re.sub(r'(\[\s+)', '[', text)
    text = re.sub(r'(\{\s+)', '{', text)

    # Убираем лишние пробелы перед открывающими скобками
    text = re.sub(r'\s+([\(\[\{])', r' \1', text)

    return text
