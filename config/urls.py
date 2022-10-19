
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agent/', include('agents.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('client.urls')),
    path('problem/', include('problem.urls')),
]
