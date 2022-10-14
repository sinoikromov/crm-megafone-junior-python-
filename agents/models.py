from django.contrib.auth.models import User
from django.db import models


# category problem
class Category(models.Model):
    title = models.CharField('category', max_length=150)

    def __str__(self):
        return self.title


# problem client
class Problem(models.Model):
    STATUS_PROBLEM = (
        ('active', 'active'),
        ('canceled', 'canceled'),
        ('done', 'done')
    )
    description = models.TextField('description')
    category = models.ForeignKey(Category, verbose_name='category', on_delete=models.CASCADE)
    status = models.CharField('Status', max_length=100, choices=STATUS_PROBLEM)
    date_added = models.DateTimeField('created_at', auto_now_add=True)
    client = models.ForeignKey("Client", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.description


# client model
class Client(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# front and beck model class
class Agent(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    is_front_agent = models.BooleanField(default=False)
    is_back_agent = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name
