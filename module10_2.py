import time
from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        self.king_name = name
        self.power = power
        super().__init__()

    def run(self):
        days = 0
        enemies = 100
        print(f'{self.king_name}, на нас напали!')
        while enemies > 0:
            time.sleep(1)
            days += 1
            enemies -= self.power
            if enemies > 0:
                print(f'{self.king_name} сражается {days}..., осталось {enemies} воинов.')
            else:
                print(f'{self.king_name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')