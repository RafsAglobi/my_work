from pprint import pprint


def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        position = file.tell()
        file.write(i + '\n')
        strings_positions[(len(strings_positions) + 1, position)] = i
    return strings_positions
    file.close()


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)