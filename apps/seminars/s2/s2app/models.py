from django.db import models

# Create your models here.

"""
# Создайте модель для запоминания бросков монеты: орёл или решка.
Также запоминайте время броска
# Доработаем задачу 1.
Добавьте статический метод для статистики по n последним броскам монеты.
Метод должен возвращать словарь с парой ключей-значений, для орла и для решки.
"""


# class CoinFlip(models.Model):
#     result = models.BooleanField()
#     date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         side = "Head" if self.result else "Tail"
#         return f"flip {side} at {self.date}"
#
#     @staticmethod
#     def flip_info(last_n: int = 0):
#         records = CoinFlip.objects.all().order_by('-id')[:last_n:-1]


from random import choice
class HeadsAndTailsModel(models.Model):
    SIDE = ['heads', 'tails']
    side = models.CharField(max_length=10, default=choice(SIDE))
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Монета упала стороной "{self.side}"'

    @staticmethod
    def get_info(n: int = None):
        if not n:
            n = 0
        # records = HeadsAndTailsModel.objects.all().order_by('-time')[:n]
        records = HeadsAndTailsModel.objects.all()[-n:]
        # result = {}
        # for side in HeadsAndTailsModel.SIDE:
        #     result[side] = [record for record in records if record.side == side].count()
        head_count = sum(i.side == 'heads' for i in records)
        tail_count = n - head_count
        return {'heads': head_count, 'tail_count': tail_count}
