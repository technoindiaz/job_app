from rest_framework import serializers
from .models import JobPost, JobCategory, CarouselSlider, VideshJobPost

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = ['post_name', 'post_image', 'mobile_phone', 'website', 'city', 'post_description']  # You can specify the fields you want to include here if needed.



class VideshJobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideshJobPost
        fields = ['job_category', 'post_name', 'post_image', 'whatsapp_phone', 'mobile_phone', 'website', 'city', 'post_description', 'is_approved', 'is_active', 'created_at']



class JobCategorySerialzer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = '__all__'


class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselSlider
        fields = '__all__'