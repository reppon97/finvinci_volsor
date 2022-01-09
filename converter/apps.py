import sys

from django.apps import AppConfig


class ConverterConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "converter"

    # save records to DB on start up
    def ready(self):
        if "runserver" not in sys.argv:
            return True
        from converter.utils.db_updater import save_to_db

        save_to_db()
