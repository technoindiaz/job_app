from rest_framework import serializers
from .models import JobPost

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = ['post_name', 'post_image', 'mobile_phone', 'city', 'post_description']  # You can specify the fields you want to include here if needed.
