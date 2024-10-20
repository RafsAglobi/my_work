2024-10-02 01:46:07,797 | WARNING | Неверный тип данных для объекта Runner
Имя может быть только строкой, передано int
2024-10-02 01:46:07,799 | WARNING | Traceback (most recent call last):
  File "/Users/miron/PycharmProjects/Urban/UrbanProject/output/module12/tests_12_4.py", line 83, in test_run
    r2 = Runner(2)
         ^^^^^^^^^
  File "/Users/miron/PycharmProjects/Urban/UrbanProject/output/module12/tests_12_4.py", line 11, in __init__
    raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
TypeError: Имя может быть только строкой, передано int

2024-10-02 01:46:07,800 | WARNING | Неверная скорость для Runner
Скорость не может быть отрицательной, сейчас -10
2024-10-02 01:46:07,802 | WARNING | Traceback (most recent call last):
  File "/Users/miron/PycharmProjects/Urban/UrbanProject/output/module12/tests_12_4.py", line 72, in test_walk
    r1 = Runner('Пешеход', -10)
         ^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/miron/PycharmProjects/Urban/UrbanProject/output/module12/tests_12_4.py", line 16, in __init__
    raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')
ValueError: Скорость не может быть отрицательной, сейчас -10