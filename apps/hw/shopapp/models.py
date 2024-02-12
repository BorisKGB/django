from django.db.models import Model, CharField, EmailField, DateTimeField
from django.db.models import TextField, DecimalField, IntegerField, BooleanField, ImageField
from django.db.models import ForeignKey, RESTRICT, ManyToManyField

"""
Клиент может иметь несколько заказов.
Заказ может содержать несколько товаров.
Товар может входить в несколько заказов.

Поля модели «Клиент»:
* имя клиента
* электронная почта клиента
* номер телефона клиента
* адрес клиента
* дата регистрации клиента

Поля модели «Товар»:
* название товара
* описание товара
* цена товара
* количество товара
* дата добавления товара

Поля модели «Заказ»:
* связь с моделью «Клиент», указывает на клиента, сделавшего заказ
* связь с моделью «Товар», указывает на товары, входящие в заказ
* общая сумма заказа
* дата оформления заказа
"""


class ClientModel(Model):
    name = CharField(max_length=15)
    email = EmailField()
    phone = CharField(max_length=15)
    address = CharField(max_length=200)
    registered = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Client {self.name}, @: {self.email}, №: {self.phone}"


class ProductModel(Model):
    name = CharField(max_length=50)
    description = TextField()
    cost = DecimalField(max_digits=8, decimal_places=2)
    amount = IntegerField(default=0)
    # Полагаю, что дата добавления это время регистрации, а не последнее пополнение количества
    created = DateTimeField(auto_now_add=True)
    # (Extra field) флаг удаления
    deleted = BooleanField(default=False)
    image = ImageField(upload_to='shopapp/images/', default=None, null=True, blank=True)

    def __str__(self):
        return f"Product {self.name}, cost: {self.cost}, amount: {self.amount}{', deleted' if self.deleted else ''}"


class OrderModel(Model):
    client = ForeignKey(ClientModel, on_delete=RESTRICT)
    products = ManyToManyField(ProductModel)
    # total_amount field will be handled by m2m_changed signal
    total_amount = DecimalField(max_digits=8, decimal_places=2, default=0)
    registration_date = DateTimeField(auto_now_add=True)  # Оформление -> дата создания
    # (Extra field) Дата выполнения, можно использовать как флаг завершённых заказов
    applied_date = DateTimeField(null=True)

    def __str__(self):
        result = f"Order from {self.client.name} "
        # got recursion error if access M2M field before saving object to DB
        result += f"for {0 if self._state.adding else self.products.count()} products, "
        result += f"total at {self.total_amount}. "
        result += f"Order {'closed' if self.applied_date else 'is open.'}"
        return result
