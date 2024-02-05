from django.core.management.base import BaseCommand, CommandError
from apps.hw.shopapp.models import ClientModel, ProductModel, OrderModel
from django.utils import lorem_ipsum
import random


class Command(BaseCommand):
    help = "Generate <n> fake Client, Product and Order objects, values can be 0"

    def add_arguments(self, parser):
        parser.add_argument('n_clients', type=int, help='Number of Clients to generate')
        parser.add_argument('n_products', type=int, help='Number of Product to generate')
        parser.add_argument('n_orders', type=int, help='Number of Orders to generate')

    def handle(self, *args, **options):
        n_clients = options.get('n_clients')
        n_products = options.get('n_products')
        n_orders = options.get('n_orders')

        for i in range(n_clients):
            client = ClientModel(name=f"Client{i+1}", email=f"cl{i+1}@mail.srv",
                                 phone=f"+9876543214{i}", address=f"some_addr {i}")
            client.save()
            self.stdout.write(f"Created {client}")

        for i in range(n_products):
            product = ProductModel(name=f"Product{i+1}",
                                   description=lorem_ipsum.words(15),
                                   cost=round(random.random()*100, 2),
                                   amount=random.randint(1, 100))
            product.save()
            self.stdout.write(f"Created {product}")

        for i in range(n_orders):
            order = OrderModel(
                client=random.choice(ClientModel.objects.all())
            )
            random_products = random.choices(ProductModel.objects.all(),
                                             k=random.randint(1, ProductModel.objects.count()*2))
            order.save()
            order_products = []
            for product in random_products:
                if product.amount == 0:
                    product = ProductModel.objects.filter(amount__gt=0).first()
                    if not product:
                        raise CommandError('Unable to pick product to buy, out of stock, orders created partially')
                product.amount -= 1
                product.save()
                order_products.append(product)
            order.products.set(order_products)
            self.stdout.write(f"Created {order}")

        self.stdout.write("Fake data created")
