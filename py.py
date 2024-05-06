from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Order, Product


def ordered_products_list(request):
    # Получаем текущую дату
    current_date = timezone.now().date()

    # Вычисляем даты начала и конца периодов
    last_7_days_start = current_date - timedelta(days=7)
    last_30_days_start = current_date - timedelta(days=30)
    last_365_days_start = current_date - timedelta(days=365)

    # Получаем заказы клиента за каждый период
    orders_last_7_days = Order.objects.filter(order_date__gte=last_7_days_start)
    orders_last_30_days = Order.objects.filter(order_date__gte=last_30_days_start)
    orders_last_365_days = Order.objects.filter(order_date__gte=last_365_days_start)

    # Получаем все товары из заказов за каждый период
    ordered_products_last_7_days = Product.objects.filter(order__in=orders_last_7_days).distinct()
    ordered_products_last_30_days = Product.objects.filter(order__in=orders_last_30_days).distinct()
    ordered_products_last_365_days = Product.objects.filter(order__in=orders_last_365_days).distinct()

    # Передаем данные в шаблон
    return render(request, 'orders_list.html', {
        'ordered_products_last_7_days': ordered_products_last_7_days,
        'ordered_products_last_30_days': ordered_products_last_30_days,
        'ordered_products_last_365_days': ordered_products_last_365_days,
    })