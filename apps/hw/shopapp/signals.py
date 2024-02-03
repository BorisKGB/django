# from django.dispatch import receiver
# from django.db.models.signals import m2m_changed
# from apps.hw.shopapp.models import OrderModel

# old realisation use receiver decorator
# @receiver(m2m_changed, sender=OrderModel.products.through)
def count_total_amount(sender, instance, action, **kwargs):
    if action == 'post_add':
        instance.total_amount = 0
        for product in instance.products.all():
            instance.total_amount += product.cost
        instance.save()
