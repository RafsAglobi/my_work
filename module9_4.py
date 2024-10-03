from random import choice

# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)


# Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, mode='w') as file:
            for i in data_set:
                file.write(str(i))
                file.write('\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__:
class MysticBall:
    def __init__(self, *word):
        self.words = word

    def __call__(self):
        word = choice(self.words)
        return word


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())