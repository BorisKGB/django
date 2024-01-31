from djangoproject.dbRouter import AppSpecificDBRouter


class l2DBRouter(AppSpecificDBRouter):
    app_name = 'l2app'  # use short app name, not import like path
    db_name = 'app_l2'
