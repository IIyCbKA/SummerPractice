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
