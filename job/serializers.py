from rest_framework import serializers
from .models import ClientAdPhotos, JobPost, JobCategory, CarouselSlider, VideshJobPost, NormalJobPost, Terms_and_conditions

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = ['post_name', 'post_image', 'mobile_phone', 'website', 'city', 'post_description']  # You can specify the fields you want to include here if needed.



class JobCategorySerialzer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = '__all__'


class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselSlider
        fields = '__all__'



#========================NEW APIS===================================#



class VideshJobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideshJobPost
        fields = '__all__'


class NormalJobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormalJobPost
        fields = '__all__'


class CarouselSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselSlider
        fields = ['image1', 'image2', 'image3']


class ClientAdPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientAdPhotos
        fields = ['ad_image1', 'ad_image2']



class TermsAndConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terms_and_conditions
        fields = ['matter']
        