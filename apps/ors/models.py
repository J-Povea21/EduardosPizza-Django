from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg, Sum
import random


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    price_per_pizza = models.FloatField()

    def __str__(self):
        return f'{self.name}'


class Person(models.Model):
    name = models.CharField(max_length=30, blank=False)
    cedula = models.PositiveIntegerField(validators=[
        MinValueValidator(1000000000),
        MaxValueValidator(9999999999)],
        help_text='La cédula debe contener 10 dígitos',
        blank=False
    )

    class Meta:
        abstract = True


class Customer(Person):
    phone_number = models.CharField(max_length=10, blank=False)
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

    message = models.CharField(max_length=200, blank=True)

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
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    deliveryman = models.ForeignKey(Deliveryman, on_delete=models.PROTECT)

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

    def save(self, customer=None, coupon_discount=None, *args, **kwargs):
        self.discount = coupon_discount
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

    mass_types = (
        ('NORMAL', 'Normal'),
        ('INTEGRAL', 'Integral'),
        ('EDUARDOS CHEESE', 'Eduardos Cheese')
    )

    mass_type = models.CharField(max_length=15, choices=mass_types)

    price_per_size = models.FloatField(default=0)

    price_per_mass = models.FloatField(default=0)

    ingredients = models.ManyToManyField(Ingredient)

    total_price = models.FloatField(default=0)

    def save(self, order=None, ingredients=None,
             *args, **kwargs):
        self.price_per_mass = self.values_dict['mass'][self.mass_type]
        self.price_per_size = self.values_dict['size'][self.size]
        self.order = order

        super(Pizza, self).save(*args, **kwargs)

        self.ingredients.set(ingredients)

        self.total_price += self.price_per_mass \
                            + self.price_per_size \
                            + self.ingredients.aggregate(
            Sum('price_per_pizza'))['price_per_pizza__sum']

        super(Pizza, self).save(*args, **kwargs)
