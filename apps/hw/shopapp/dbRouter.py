from djangoproject.dbRouter import AppSpecificDBRouter


class ShopDBRouter(AppSpecificDBRouter):
    app_name = 'shopapp'
    db_name = 'shop_db'
