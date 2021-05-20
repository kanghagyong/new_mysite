# ---------------------------------- [edit] ---------------------------------- #
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('get/', views.item_price_get),
]
# ---------------------------------------------------------------------------- #
