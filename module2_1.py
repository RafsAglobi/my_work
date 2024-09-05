number1 = int(input("Введите число:")) # Fizz, Buzz, FizzBuzz
if number1 % 3 == 0 and number1 % 5 == 0:
print('FizzBuzz')
elif number1 % 3 == 0:
print('Fizz')
elif number1 % 5 == 0:
print('Buzz')
else:
print('Неверное число')

number2 = int(input("Введите число")) # Fizz, Buzz, FizzBuzz
if number2 % 2 == 0 and number2 % 8 ==0:
print('FizzBuzz')
elif number2 % 2 == 0:
print('Fizz')
elif number2 % 8 == 0:
print('Buzz')
else:
print('Неверное число')
