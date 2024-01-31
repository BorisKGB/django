from django.db import models


class User(models.Model):
    # id field will be added automatically
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()
# also able to use any from https://docs.djangoproject.com/en/5.0/ref/models/fields/#field-types
# also ForeignKey, OneToOneField and ManyToManyField for relations

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, age: {self.age}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')  # where images will be stored (path field|link to real files?)
    # need external lib Pillow


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)  # CASCADE: on user deletion all orders also will be deleted
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"Name: {self.name}, email: {self.email}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"Title: {self.title}"

    # custom logic over data to use in get methods
    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:8])}...'
