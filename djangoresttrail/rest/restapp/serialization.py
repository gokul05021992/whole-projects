from rest_framework.serializers import ModelSerializer
from .models import employee

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = employee
        fields = ["id", "name"]