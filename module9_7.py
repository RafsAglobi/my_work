
def is_prime(func):
    def wrapper(*args):
        summa = sum(args)
        if all([(summa % i) != 0 for i in range(2, summa)]):
            print('Простое')
        else:
            print('Составное')
        res = func(summa)
        return res

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
