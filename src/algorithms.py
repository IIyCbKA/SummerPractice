def SearchLargestProgression(array: list, length: int, isArith: bool) -> int:
    actionSymbol: str = '-' if isArith else '/'
    largest: int = 0
    currentLength: int = 2
    currentCoef: float = eval(f'{array[1]} {actionSymbol} {array[0]}')
    for ind in range(2, length):
        actuallyCoef = eval(f'{array[ind]} {actionSymbol} {array[ind - 1]}')

        if actuallyCoef == currentCoef:
            currentLength += 1
        else:
            largest = max(largest, currentLength)
            currentLength = 2
            currentCoef = actuallyCoef

    largest = max(largest, currentLength)

    return largest


def FindRightNums(num: str, limit: int, isIncreasing: bool | None) -> int:
    numGreaterLimit: bool = (int(num) > limit)
    numIsStrictlyIncreasing: bool = (
        len(num) > 1 and int(num[-1]) <= int(num[-2])) if isIncreasing \
        else len(num) > 1 and int(num[-1]) >= int(num[-2])
    numIsBig: bool = len(num) > 10
    anyCheck: bool = numGreaterLimit or numIsStrictlyIncreasing or numIsBig

    if anyCheck:
        count: int = 0

    else:
        count: int = 1
        if isIncreasing or isIncreasing is None:
            for nextDigit in range(int(num[-1]), 10):
                count += FindRightNums(num + str(nextDigit), limit, True)
        if not isIncreasing or isIncreasing is None:
            for nextDigit in range(0, int(num[-1])):
                count += FindRightNums(num + str(nextDigit), limit, False)

    return count


def sortedArraysByIndexAndAddResult(arrayDots: list, arrayResult: list,
                                    lengthArray: int, halfLength: int,
                                    keyInd: int) -> None:
    arrayDots.sort(key=lambda x: x[keyInd])
    if lengthArray % 2 == 0:
        result = round((arrayDots[halfLength][keyInd] +
                        arrayDots[halfLength - 1][keyInd]) / 2, 2)
    else:
        result = arrayDots[halfLength][keyInd]

    arrayResult.append(result)


def addChainLengthToCompressedArray(chainLength: int,
                                    compressedArray: list) -> None:
    if chainLength < 15:
        compressedArray.append(chainLength)
    elif chainLength == 15:
        compressedArray.append(chainLength)
        compressedArray.append(0)
    else:
        while chainLength > 0:
            if chainLength >= 15:
                numAdd = 15
            else:
                numAdd = chainLength

            chainLength -= numAdd
            compressedArray.append(numAdd)
