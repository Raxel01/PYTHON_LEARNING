from django.db import models

# Create your models here.
# 9999.99 max_digit >= decimalPlaces

class Promotion(models.Model):
    description = models.CharField(max_length=100)
    discount = models.FloatField()
    #prosuct_set
class Collection(models.Model):
    title = models.CharField(max_length=100)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')
    # '+' not creat reverse relation


class Product(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price       = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    inventory   = models.IntegerField(null=True)
    last_update = models.DateTimeField(auto_now_add=True, null=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT,null=True)
    promotions = models.ManyToManyField(Promotion, null=True)


class Customer(models.Model):
    FIRST_MEMEBERSHIP = 'A'
    SECOND_MEMEBERSHIP = 'B'
    THIRD_MEMEBERSHIP = 'C'

    MEMBERSHIP_TYPE = [
        (FIRST_MEMEBERSHIP, 'FIRST ABB'),
        (SECOND_MEMEBERSHIP, 'SEC ABB'),
        (THIRD_MEMEBERSHIP, 'THIRD ABB')
    ]
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    birth_date = models.DateField(null=True) # can Be Null so
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_TYPE, default=FIRST_MEMEBERSHIP)
    class Meta:
        db_table = 'store_customers'
        indexes = [
            models.Index(fields=['last_name', 'first_name'])
        ]


class Order(models.Model):
    PN  = 'P'
    CO  = 'C' 
    FA  = 'F'

    PAYMENTS_TYPE = [
        (PN, 'Pending'),
        (CO, 'Complete'),
        (FA, 'Failed')
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENTS_TYPE, default=PN)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Addresses(models.Model):
    addresszip = models.SmallIntegerField(null=True) 
    street = models.CharField(max_length=100)
    current_city = models.CharField(max_length=100)
    Customer = models.OneToOneField(Customer, on_delete= models.CASCADE,primary_key=True)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()


# one-to-many
# attribute = models.ForeignKEy(toTable: Customer, on_delete: CASCADE)