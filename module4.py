
#Модуль fake_math.py
def divide(first, second):
if first != 0 and second != 0:
result = first / second
return (result)
else:
try:
result = first / second
return result
except ZeroDivisionError:
return('Ошибка')

#Модуль true_math.py
def divide(first, second):
if first != 0 and second != 0:
result = first / second
return(result)
else:
try:
result = first / second
return result
except ZeroDivisionError:
result = math.inf
return(result)

#Модуль main.py
from fake_math import divide as fake_divide
from true_math import divide as true_divide

result1 = fake_divide(69,3)
result2 = fake_divide(3,0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)