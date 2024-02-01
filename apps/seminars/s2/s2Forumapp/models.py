from django.db import models

"""
Создайте модель Автор. Модель должна содержать следующие поля:
имя до 100 символов
фамилия до 100 символов
почта
биография
день рождения
Дополнительно создай пользовательское поле “полное имя”, которое возвращает имя и фамилию.

Создайте модель Статья (публикация). Авторы из прошлой задачи могут писать статьи. У статьи может быть только один автор. У статьи должны быть следующие обязательные поля:
заголовок статьи с максимальной длиной 200 символов
содержание статьи
дата публикации статьи
автор статьи с удалением связанных объектов при удалении автора
категория статьи с максимальной длиной 100 символов
количество просмотров статьи со значением по умолчанию 0
флаг, указывающий, опубликована ли статья со значением по умолчанию False

Создайте модель Комментарий.
Авторы могут добавлять комментарии к своим и чужим статьям. Т.е. у комментария может быть один автор.
И комментарий относится к одной статье. У модели должны быть следующие поля
автор
статья
комментарий
дата создания
дата изменения
"""


class AuthorModel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateTimeField()
    fullname = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.fullname = self.name + " " + self.surname
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.fullname


class ArticleModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views_count = models.IntegerField(default=0)
    published_flag = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE)
    text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    changed_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
