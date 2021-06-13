from django.urls import path
from. import views

urlpatterns = [
    path('', views.index,),
    path('contact/', views.contact),
    path('about/',views.about),
    path('videos/',views.videos),
    path('photos/',views.photos)
]