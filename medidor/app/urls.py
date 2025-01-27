from django.urls import path
from.views import home

urlpatterns = [
    path('', home, name="home"),
]
# Compare this snippet from medidor/app/models.py:
