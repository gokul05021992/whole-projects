from django.urls import path
from.import views

urlpatterns = [
    path('', views.addition),
    path("add",views.add),
]

