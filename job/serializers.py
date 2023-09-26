from rest_framework import serializers
from .models import JobPost

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'  # You can specify the fields you want to include here if needed.
