def SearchLargestProgression(array: list, length: int, isArith: bool) -> int:
    actionSymbol: str = '-' if isArith else '/'
    largest: int = 0
    currentLength: int = 2
    currentCoef: float = eval(f'{array[1]} {actionSymbol} {array[0]}')
    for ind in range(2, length):
        if eval(f'{array[ind]} {actionSymbol} {array[ind - 1]}') == currentCoef:
            currentLength += 1
        else:
            largest = max(largest, currentLength)
            currentLength = 2
            currentCoef = eval(f'{array[ind]} {actionSymbol} {array[ind - 1]}')

    largest = max(largest, currentLength)

    return largest


def FindRightNums(num: str, limit: int, isIncreasing: bool | None) -> int:
    numGreaterLimit: bool = (int(num) > limit)
    numIsStrictlyIncreasing: bool = (
        len(num) > 1 and int(num[-1]) <= int(num[-2])) if isIncreasing \
        else len(num) > 1 and int(num[-1]) >= int(num[-2])
    numIsBig: bool = len(num) > 10

    if numGreaterLimit or numIsStrictlyIncreasing or numIsBig:
        return 0

    else:
        result: int = 1
        if isIncreasing or isIncreasing is None:
            for nextDigit in range(int(num[-1]), 10):
                result += FindRightNums(num + str(nextDigit), limit, True)
        if not isIncreasing or isIncreasing is None:
            for nextDigit in range(0, int(num[-1])):
                result += FindRightNums(num + str(nextDigit), limit, False)
        return result
