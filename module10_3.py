import threading
import random
import time
from threading import Lock


class Bank:
    def __init__(self):
        self.balance = 500
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            deposit_amount = random.randint(50, 500)
            self.balance += deposit_amount
            print(f"Пополнение: {deposit_amount}. Баланс: {self.balance}")
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            take_amount = random.randint(50, 500)
            print(f"Запрос на {take_amount}")

            if take_amount <= self.balance:
                self.balance -= take_amount
                print(f"Снятие: {take_amount}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
