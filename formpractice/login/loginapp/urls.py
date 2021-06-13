from django.urls import path
from.import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('login/',LoginView.as_view(), name ="login"),
    path('accounts/profile/',views.profile,name="profile")
]