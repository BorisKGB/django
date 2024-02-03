from django.apps import AppConfig
from django.db.models.signals import m2m_changed


class ShopappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.hw.shopapp'

    def ready(self):
        # connect signals
        # old version, work, but looking strange
        # import apps.hw.shopapp.signals
        # current documentation adaptation attempt
        from .signals import count_total_amount
        from .models import OrderModel
        m2m_changed.connect(count_total_amount, sender=OrderModel.products.through)
