from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from .validators import *
from django.db.models import Sum
import random


# Create your models here.

class Product(models.Model):

    name = models.CharField(max_length=30)
    price_per_pizza = models.FloatField(validators=[validate_price])
    available = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.name}'


class Ingredient(Product):
    pass


class Mass(Product):
    pass


class Person(models.Model):

    name = models.CharField(max_length=30, blank=False)
    cedula = models.PositiveIntegerField(
        blank=False,
        validators=[validate_cedula],
        unique=True
    )

    def __str__(self):
        return f'{self.name}'



    class Meta:
        abstract = True


class Customer(Person):
    phone_number = models.CharField(
        max_length=10,
        blank=False,
        validators=[validate_phone_number]
    )

    address = models.CharField(blank=False)


class Deliveryman(Person):
    stars = models.FloatField(default=0)
    ratings_counter = models.PositiveIntegerField(default=0)


class Coupon(models.Model):
    code = models.CharField(max_length=7, blank=False)
    discount = models.FloatField(validators=[
        MinValueValidator(0.1),
        MaxValueValidator(0.3)
    ])

    status_options = (
        ('CANJEADO', 'Canjeado'),
        ('DISPONIBLE', 'Disponible'),
    )

    status = models.CharField(max_length=11, choices=status_options)

    def update_status_to_available(self):
        self.status = 'DISPONIBLE'
        self.save()

    def update_status_to_redeemed(self):
        self.status = 'CANJEADO'
        self.save()


class Rating(models.Model):
    order = models.OneToOneField('Order', on_delete=models.DO_NOTHING, related_name='rating',
                                 null=True)

    rating_values = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    rating_value = models.PositiveIntegerField(choices=rating_values)

    message = models.CharField(max_length=200, default='Sin mensaje', blank=True)

    def save(self, order=None, *args, **kwargs):
        self.order = order
        super(Rating, self).save(*args, **kwargs)

        deliveryman = Deliveryman.objects.get(id=self.order.deliveryman.id)
        total_ratings = deliveryman.ratings_counter + 1

        current_stars = deliveryman.stars
        new_average = current_stars + ((self.rating_value - current_stars) / total_ratings)
        new_average = round(new_average, 2)

        deliveryman.stars = new_average
        deliveryman.ratings_counter = total_ratings
        deliveryman.save()


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='orders')
    deliveryman = models.ForeignKey(Deliveryman, on_delete=models.PROTECT, related_name='deliveries')

    payment_methods = (
        ('EFECTIVO', 'Efectivo'),
        ('NEQUI', 'Nequi')
    )

    payment_method = models.CharField(max_length=8, choices=payment_methods)

    date = models.DateTimeField(auto_now_add=True, blank=False)

    destination = models.CharField(default='Null', blank=False)

    discount = models.FloatField(default=0)

    total_value = models.FloatField(default=0)

    domicile_price = models.PositiveIntegerField(default=8000)

    def save(self, customer=None, coupon=None, *args, **kwargs):
        if coupon:
            self.discount = coupon.discount
            coupon.update_status_to_redeemed()

        self.customer = customer
        self.deliveryman = random.choice(Deliveryman.objects.all())
        self.destination = self.customer.address
        super(Order, self).save(*args, **kwargs)

    def calculate_total_value(self) -> None:
        pizza = Order.objects.latest('id').pizza

        total_value_calc = pizza.total_price + self.domicile_price
        total_value_calc -= total_value_calc * self.discount

        self.total_value = total_value_calc
        super().save()


class Pizza(models.Model):
    values_dict = {
        'size': {
            'S': 20000,
            'M': 32000,
            'L': 42000,
            'XL': 60000
        },
        'mass': {
            'NORMAL': 0,
            'INTEGRAL': 4000,
            'EDUARDOS CHEESE': 6000
        }
    }

    size_types = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large')
    )

    order = models.OneToOneField(Order, on_delete=models.CASCADE,
                                 null=True, related_name='pizza')

    size = models.CharField(max_length=2, choices=size_types)

    mass_type = models.ForeignKey(Mass, on_delete=models.DO_NOTHING)

    price_per_size = models.FloatField(default=0)

    price_per_mass = models.FloatField(default=0)

    ingredients = models.ManyToManyField(Ingredient)

    total_price = models.FloatField(default=0)

    def save(self, order=None, ingredients=None,
             *args, **kwargs):
        self.price_per_mass = self.mass_type.price_per_pizza
        self.price_per_size = self.values_dict['size'][self.size]
        self.order = order

        super(Pizza, self).save(*args, **kwargs)

        self.ingredients.set(ingredients)

        self.total_price += self.price_per_mass \
                            + self.price_per_size \
                            + self.ingredients.aggregate(
            Sum('price_per_pizza'))['price_per_pizza__sum']

        super(Pizza, self).save(*args, **kwargs)
