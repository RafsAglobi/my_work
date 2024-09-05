from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            file = open(self.__file_name, 'r')
        except FileNotFoundError:
            print("Файл не существует")
            return ""

        products = file.read()
        file.close()
        return products

    def add(self, *products):
        existing_product_names = set()
        try:
            file = open(self.__file_name, 'r')
            for line in file:
                name = line.split(',')[0].strip()
                existing_product_names.add(name)
            file.close()
        except FileNotFoundError:
            print("Файл не существует")

        file = open(self.__file_name, 'a')
        for product in products:
            if product.name in existing_product_names:
                print(
                    f'Продукт {product.name} уже есть в магазине')
            else:
                file.write(f'{product}\n')
                existing_product_names.add(product.name)
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())