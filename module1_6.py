my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(my_dict)
print(my_dict['Masha'])
print(my_dict.get('Kamila'))
del my_dict ['Egor']
print(my_dict)
my_dict['Kamila']= 1981
my_dict['Artem']= 1915
print(my_dict)

my_set = {(1), 'Яблоко', 42.314}
print(my_set)
list_ = {(1),'Яблоко', 42.314, 13, (5, 6, 1.6)}
list_ = set(list_)
print(my_set)
print(list_.remove(1))
print(list_)