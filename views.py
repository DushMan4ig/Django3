from django.shortcuts import render, redirect
from .models import Client, Product, Order
from .forms import ClientForm
from django.utils import timezone
from django.shortcuts import render

def index(request):
    client.delete()
    return redirect('all_clients') 
    return render(request, 'delete_client.html', {'client': client})


def client_ordered_products(request, client_id, days):
    # Определите дату, за которую вы хотите получить заказы
    end_date = timezone.now()
    start_date = end_date - timezone.timedelta(days=days)

    # Получите все заказы клиента за выбранный период времени
    orders = Order.objects.filter(client_id=client_id, order_date__range=(start_date, end_date))

    # Получите список товаров из всех заказов клиента
    ordered_products = []
    for order in orders:
        ordered_products.extend(order.products.all())

    # Удалите повторяющиеся товары из списка
    unique_ordered_products = list(set(ordered_products))

    # Отсортируйте товары по времени заказа
    sorted_ordered_products = sorted(unique_ordered_products, key=lambda x: x.order.order_date, reverse=True)

    context = {
        'client_id': client_id,
        'ordered_products': sorted_ordered_products,
        'days': days,
    }
    return render(request, 'client_ordered_products.html', context)