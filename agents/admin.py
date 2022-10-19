from django.contrib import admin
from .models import Client, Agent, Category, Problem, CustomerUser

admin.site.register(Agent)
admin.site.register(CustomerUser)


class ClientAdmin(admin.ModelAdmin):
    list_display = ['pk', 'first_name', 'last_name', 'age', 'email']


admin.site.register(Client, ClientAdmin)
admin.site.register(Problem)
admin.site.register(Category)
