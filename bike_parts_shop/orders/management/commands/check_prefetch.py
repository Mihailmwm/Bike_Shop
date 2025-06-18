# orders/management/commands/check_prefetch.py

from django.core.management.base import BaseCommand
from django.db import connection
from orders.models import Orders
from pprint import pprint

class Command(BaseCommand):
    help = 'Проверить эффективность prefetch_related()'

    def handle(self, *args, **kwargs):
        connection.queries.clear()

        self.stdout.write(self.style.MIGRATE_HEADING("\n Загружаем заказы с prefetch_related..."))

        orders = Orders.objects.select_related('user').prefetch_related('items__product')

        for order in orders:
            print(f"Заказ {order.id} от {order.user.username}")
            for item in order.items.all():
                print(f"  - {item.product.name}: {item.quantity} шт.")

        total_queries = len(connection.queries)
        self.stdout.write(self.style.SUCCESS(f"\n Выполнено SQL-запросов: {total_queries}\n"))

        if total_queries > 10:
            self.stdout.write(self.style.WARNING("Возможно, prefetch_related работает неэффективно или не все связи указаны."))
        else:
            self.stdout.write(self.style.SUCCESS("prefetch_related работает корректно."))


