from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete, pre_delete
from django.db import models
from django.shortcuts import get_object_or_404


class CustomerUser(AbstractUser):
    pass


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
    client = models.ForeignKey("Client", on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.description


# client model
class Client(models.Model):
    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    was_born = models.DateField(default=2003)
    gender = models.CharField(max_length=100, choices=GENDER)
    age = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ('-date_added',)


# front and beck model class
class Agent(models.Model):
    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    gender = models.CharField(max_length=20, choices=GENDER)
    is_front_agent = models.BooleanField(default=False)
    is_back_agent = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    # was_born = models.DateField(default='2000-12-30')

    class Meta:
        verbose_name = 'Agent List'
        ordering = ['-pk', ]

    def __str__(self):
        return self.first_name

    def get_object_id(self, id):
        try:
            return Agent.objects.get(pk=id)
        except Agent.DoesNotExist:
            return False


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        CustomerUser.objects.create_user(username=f"{instance.first_name}_{instance.last_name}{instance.pk}",
                                         password=instance.password, email=instance.email)


def post_user_delete_signal(sender, instance, **kwargs):
    if Agent.get_object_id(instance, instance.pk):
        user = CustomerUser.objects.get(username=f"{instance.first_name}_{instance.last_name}{instance.pk}")
        user.delete()


post_save.connect(post_user_created_signal, sender=Agent)

pre_delete.connect(post_user_delete_signal, sender=Agent)
