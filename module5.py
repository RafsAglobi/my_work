class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to (self, new_flor):
        count = 0
        while 0 < new_flor < self.number_of_floors:
            count += 1
            print(count)
            if count == new_flor:
                break
        if new_flor > self.number_of_floors:
            print("Такого этажа не существует")


h1 = House('"ЖК Эльбрус"', 30)
h2 = House('"Домик в деревне"', 2)
print(h1.name, h1.number_of_floors)
print(h2.name, h2.number_of_floors)
h1.go_to(5)
h2.go_to(10)
