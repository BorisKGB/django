from django.http import HttpResponse
from django.views import View
import logging
import random
"""
# Задание 4
Создайте представление “Привет, мир!” внутри вашего первого приложения.
Настройте маршруты
# Задание №5
Создайте новое приложение. Подключите его к проекту. В
приложении должно быть три простых представления,
возвращающих HTTP ответ:
* Орёл или решка
* Значение одной из шести граней игрального кубика
* Случайное число от 0 до 100
* Пропишите маршруты
# Задание №6
Добавьте логирование в проект.
Настройте возможность вывода в файл и в терминал.
"""

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("<h1>Hello world</h1>")


class IndexPageView(View):
    def get(self, request):
        return HttpResponse("<h1>Hello world</h1>")


def log(view):
    def wrapper(request, *args, **kwargs):
        res: HttpResponse = view(request, *args, **kwargs)
        logger.info(f'func {view.__name__} returned {res}')
        return res.content.decode('utf-8')
    return wrapper


@log
def coin_flip(request):
    side = random.choice(['head', 'tail'])
    return HttpResponse(f"<p>{side}</p>")


def dice_side(request):
    side = random.choice([1, 2, 3, 4, 5, 6])
    logger.info(f"dice flip to {side}")
    return HttpResponse(f"<p>{side}</p>")


def rand_number(request):
    number = random.randint(0, 100)
    logger.info(f"we got {number}")
    return HttpResponse(f"<p>{number}</p>")
