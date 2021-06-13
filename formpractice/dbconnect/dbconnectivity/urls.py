from django.urls import path
from. import views

urlpatterns = [
    path('index',views.index,name="index"),
    path('',views.sample,name="sample"),
    path('login/',views.login,name='login')
]