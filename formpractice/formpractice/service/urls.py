from django.urls import path
from.import views

urlpatterns = [
    path('',views.index),
    path('former',views.former),
    path("submitted",views.submitted)
]
