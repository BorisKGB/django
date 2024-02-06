from django.apps import AppConfig


class S3AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.seminars.s3.s3app'


"""
Доработаем задачу 7 из урока 1, где бросали монетку, игральную кость и генерировали случайное число.
Маршруты могут принимать целое число - количество бросков.
Представления создают список с результатами бросков и передают его в контекст шаблона.
Необходимо создать универсальный шаблон для вывода результатов любого из трёх представлений.
"""

"""
Доработаем задачи из прошлого семинара по созданию моделей автора, статьи и комментария.
Создайте шаблон для вывода всех статей автора в виде списка заголовков.
Если статья опубликована, заголовок должен быть ссылкой на статью.
Если не опубликована, без ссылки.
Не забываем про код представления с запросом к базе данных и маршруты.
"""

"""
Доработаем задачу 4.
Создай шаблон для вывода подробной информации о статье.
Внесите изменения в views.py - создайте представление и в urls.py - добавьте маршрут.

*Увеличивайте счётчик просмотра статьи на единицу при каждом просмотре
"""
