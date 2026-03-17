""" Модуль для нахождения среднего значения """


def calculate_average(nums):
    """ Функция вычисления среднего значения """
    total = sum(nums)
    count = len(nums)
    average = total / count
    return average


nums_list = [10, 15, 20]
result = calculate_average(nums_list)
print("The average is:", result)
