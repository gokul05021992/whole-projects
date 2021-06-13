from django.urls import path
from.views import students,studentlist,editEmployee

urlpatterns = [
    path('',students),
    path('list/',studentlist.as_view()),
    path('edit/<id>',editEmployee.as_view()),
]
