from rest_framework.serializers import ModelSerializer
from .models import student

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = student
        fields = "__all__"