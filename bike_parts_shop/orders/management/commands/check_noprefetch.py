from django.core.management.base import BaseCommand
from django.db import connection, reset_queries
from orders.models import Orders

class Command(BaseCommand):
    help = 'Проверка SQL-запросов без prefetch_related'

    def handle(self, *args, **options):
        reset_queries()

        print(" Загрузка заказов БЕЗ prefetch_related...\n")

        orders = Orders.objects.all()  # <- без prefetch_related

        for order in orders:
            print(f"Заказ {order.id} от {order.user.username}:")
            for item in order.items.all():  # <- будут отдельные запросы!
                print(f"  - {item.product.name} x {item.quantity}")

        print("\n SQL-запросы:")
        for query in connection.queries:
            print(f"[{query['time']}s] {query['sql']}")

        print(f"\n Всего SQL-запросов: {len(connection.queries)}")
