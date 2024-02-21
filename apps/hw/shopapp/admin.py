from django.contrib.admin import AdminSite, ModelAdmin, site, display
from django.contrib.admin import SimpleListFilter, action as add_action
from django.utils.translation import gettext_lazy
from .models import ClientModel, ProductModel, OrderModel

shop_admin = AdminSite(name='shop_db')


@add_action
def product_reset_amount(modeladmin, request, queryset):
    queryset.update(amount=0)


@add_action
def product_mark_delete(modeladmin, request, queryset):
    queryset.update(amount=0)


class ClientAdmin(ModelAdmin):
    list_display = [field.name for field in ClientModel._meta.fields]  # all fields, including 'id'
    list_filter = ['registered']
    ordering = ['id']
    search_fields = ['name', 'email']
    search_help_text = 'Search by name or email'

    readonly_fields = ['id', 'registered']
    fieldsets = [
        (None, {'fields': ['id', 'name', 'registered']}),
        ('Contact info', {'fields': ['email', 'phone', 'address']})
    ]


class HasImageFilter(SimpleListFilter):
    """https://docs.djangoproject.com/en/5.0/ref/contrib/admin/filters/#using-a-simplelistfilter"""
    title = gettext_lazy('has image')

    parameter_name = 'has image'

    def lookups(self, request, model_admin):
        return ('yes', gettext_lazy('yes')), ('no', gettext_lazy('no'))

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.exclude(image__exact='')
        if self.value() == 'no':
            return queryset.filter(image__exact='')


class ProductAdmin(ModelAdmin):
    list_display = ['id', 'name', 'amount', 'cost', 'deleted', 'has_image']
    list_filter = ['amount', 'deleted', HasImageFilter]
    ordering = ['id']
    search_fields = ['name']
    search_help_text = 'Search by name'
    actions = [product_reset_amount, product_mark_delete]

    readonly_fields = ['id', 'created', 'deleted']
    fieldsets = [
        (None, {'fields': ['id', 'name', 'created', 'deleted']}),
        ('Description', {'classes': ['collapse'], 'fields': ['description', 'image']}),
        ('Shop info', {'fields': ['cost', 'amount']})
    ]

    @display(boolean=True)
    def has_image(self, product: ProductModel) -> bool:
        return bool(product.image)


class OrderAdmin(ModelAdmin):
    list_display = ['id', 'client_name', 'total_amount', 'registration_date', 'is_open']
    list_filter = ['client__name']
    ordering = ['id']
    search_fields = ['client__name', 'client__email']
    search_help_text = 'Search by client name or email'

    readonly_fields = ['id', 'total_amount', 'is_open', 'registration_date']
    fieldsets = [
        (None, {'fields': ['id', 'client', 'registration_date', 'is_open']}),
        ('Content', {'fields': ['products', 'total_amount'],
                     'description': 'total_amount will be automatically updated after order change'})
    ]

    def client_name(self, order: OrderModel) -> str:
        return order.client.name

    @display(boolean=True)
    def is_open(self, order: OrderModel) -> bool:
        return not bool(order.applied_date)


site.register(ClientModel, ClientAdmin)
site.register(ProductModel, ProductAdmin)
site.register(OrderModel, OrderAdmin)
site.disable_action('delete_selected')

shop_admin.register(ClientModel, ClientAdmin)
shop_admin.register(ProductModel, ProductAdmin)
shop_admin.register(OrderModel, OrderAdmin)
shop_admin.disable_action('delete_selected')
