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
