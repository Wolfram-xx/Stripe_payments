from django.db import models

class Currency(models.TextChoices):
    RUB = "rub", 'Рубли'
    USD = 'usd', 'Доллары'

class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    currency = models.CharField(max_length=5, choices=Currency, default=Currency.RUB)

class Discount(models.Model):
    name = models.CharField(max_length=50)
    percent = models.DecimalField(max_digits=5, decimal_places=2)   # Не очень понял из ТЗ, как это должно работать
    coupon_id = models.CharField(max_length=100)                    # Поэтому подразумевается создание купонов и налогов через сайт Stripe
class Tax(models.Model):                                            # И добавление через админку. Их вроде можно
    name = models.CharField(max_length=100)                         # Создавать в коде, но как это практически должно работать, не понимаю
    percent = models.DecimalField(max_digits=5, decimal_places=2)
    tax_id = models.CharField(max_length=100)

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, null=True)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True)
    def total_price(self):
        return sum(
            order_item.item.price * order_item.quantitiy
            for order_item in self.orderitem_set.all()
        )

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantitiy = models.PositiveIntegerField(default=1)

