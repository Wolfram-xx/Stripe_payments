import stripe
from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import Http404, JsonResponse
from Payments.models import *
import os

stripe.api_key = os.getenv("SECRET_STRIPE_KEY")
stripe_public_key = os.getenv("PUBLIC_STRIPE_KEY")

def index_page(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})

def create_page(request):
    return render(request, 'create.html')

def create_item(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get('description')
        price = request.POST.get("price")
        currency = request.POST.get("currency")
        if currency == '':
            currency = "rub"
        Item.objects.create(
            name=name,
            description=description,
            price=price,
            currency=currency,
        )
        return redirect('/home/')

def item_page(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'item.html', {'item': item, 'public_key': stripe_public_key})
    return render(request, 'item.html', {'item': item, 'public_key': stripe_public_key})


def buy_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': item.currency,
                'unit_amount': item.price * 100,
                'product_data': {
                    'name': item.name,
                },
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='https://localhost/home/',
        cancel_url='https://localhost/home/',
    )
    return JsonResponse({'session': session})

def add_to_order(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    order_id = request.session.get('order_id')
    if order_id:
        order = get_object_or_404(Order, id=order_id)
        if len(order.orderitem_set.all()) > 0:
            if order.orderitem_set.all()[0].item.currency != item.currency:
                return redirect('/currency_error/')
    else:
        order = Order.objects.create()
        request.session['order_id'] = order.id

    order_item, created = OrderItem.objects.get_or_create(order=order, item=item)
    if not created:
        order_item.quantitiy += 1
    order_item.save()
    return redirect('/home/')

def currency_error_page(request):
    return render(request, 'currency_error.html')

def order_page(request):
    order_id = request.session.get('order_id')
    if order_id:
        order = get_object_or_404(Order, id=order_id)
    else:
        order = Order.objects.create()
        request.session['order_id'] = order.id
    return render(request, 'order.html', {'order': order, 'public_key': stripe_public_key})

def delete_from_order(request, item_id):
    order_id = request.session.get('order_id')
    if order_id:
        order = get_object_or_404(Order, id=order_id)
        order_item = OrderItem.objects.filter(order=order, item_id=item_id)
        if order_item:
            order_item[0].delete()

        return redirect('/order/')

def buy_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    line_items = []
    for order_item in order.orderitem_set.all():

        line = {
            'price_data': {
                'currency': order_item.item.currency,
                'unit_amount': int(order_item.item.price * 100),
                'product_data': {
                    'name': order_item.item.name
                },
            },
            'quantity': order_item.quantitiy,
        }

        if order.tax:
            line['tax_rates'] = [order.tax.tax_id]

        line_items.append(line)

    discount = []
    if order.discount:
        discount.append({'coupon': order.discount.coupon_id})




    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url='https://localhost/home/',
        cancel_url='https://localhost/home/',
        discounts=discount if discount else None,
    )
    return JsonResponse({'session': session})
