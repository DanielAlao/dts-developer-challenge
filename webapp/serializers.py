from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Title required")
        return value

    def validate_status(self, value):
        if value not in ['Started', 'In progress', 'Done']:
            raise serializers.ValidationError("Invalid status")
        return value

    def validate_due_date(self, value):
        from datetime import date
        if value < date.today():
            raise serializers.ValidationError(
                "Due date cannot be in past")
        return value

    class Meta:
        model = Task
        fields = '__all__'
