t = (['кит', 1, 3], 5)
t[0][0] = 'кот'
t[0].remove(1)
t[0][1] = 3**2
print("Измененный кортеж:", t)
try:
    t[1] *= 2
except TypeError:
    print("При попытке изменить второй элемент кортежа (умножить его на 2) возникает ошибка TypeError. \nЭто объясняется тем, что кортежи являются неизменяемыми в Python")