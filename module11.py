from PIL import Image
import requests
import sys


# Библиотека Requests — это модуль для исполнения HTTP-запросов в Python.
# Он имеет простой и удобный интерфейс для отправки и получения ответов от серверов.
# Основные возможности библиотеки:
# выполнение базового GET-запроса;
# передача параметров запроса;
# отправка заголовков;
# передача данных в POST-запросе;
# работа с JSON-данными;
# обработка исключений;
# работа с файлами;
# управление cookies.


# Мы используем библиотеку requests для загрузки изображения.

class Req:
    global resp
    url = ('https://img.freepik.com/free-photo/'
           'white-notebook-black-data-firewall_1150-1733'
           '.jpg?w=900&t=st=1725998287~exp=1725998887~hmac='
           '9020d39bae348d2177d5213d73ca4ed5a95a30e9284c37f5dea87a38f0de1010')
    try:
        resp = requests.get(url, stream=True).raw
    except requests.exceptions.RequestException as e:
        sys.exit(1)

    try:
        img = Image.open(resp)
    except IOError:
        print("Unable to open image")
        sys.exit(1)

    img.save('sid.jpg', 'jpeg')


# Pillow и его предшественник PIL — это оригинальные библиотеки Python для работы с изображениями.
# Основные возможности библиотеки:
# Поддержка различных форматов файлов изображений.
# Выполнение различных операций с изображениями, таких как обрезка, изменение размера, добавление текста, поворот и др.
# Возможность сохранять изменения в файле изображения

# Мы используем библиотеку Pillow для обрезки изображения
class Pill(Req):
    def __init__(self):
        self.size = None

    def crop_center(pil_img, crop_width: int, crop_height: int) -> Image:
        img_width, img_height = pil_img.size
        return pil_img.crop(((img_width - crop_width) // 2,
                             (img_height - crop_height) // 2,
                             (img_width + crop_width) // 2,
                             (img_height + crop_height) // 2))

    im = Image.open('sid.jpg')
    im_new = crop_center(im, 500, 600)
    im_new.save('sid.png', quality=95)