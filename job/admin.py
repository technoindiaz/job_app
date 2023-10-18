from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ['post_name', 'post_image', 'whatsapp_phone', 'mobile_phone', 'website', 'city', 'post_description', 'created_at', 'updated_at']

@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ['job_category_id', 'job_category_name', 'job_category_description', 'is_active', 'created_at']


@admin.register(VideshJobPost)
class VideshJobPostAdmin(admin.ModelAdmin):
    list_display = ['post_name', 'job_category','post_image', 'mobile_phone1', 'mobile_phone2', 'whatsapp_phone', 'city', 'post_description', 'is_approved', 'is_active','created_at', 'updated_at']

@admin.register(NormalJobPost)
class NormalJobPostAdmin(admin.ModelAdmin):
    list_display = ['post_name', 'job_category','post_image', 'mobile_phone1', 'mobile_phone2', 'whatsapp_phone',  'city', 'post_description', 'is_approved', 'is_active','created_at', 'updated_at']



@admin.register(CarouselSlider)
class CarouselSliderAdmin(admin.ModelAdmin):
    list_display = ['name', 'image1', 'image2', 'image3', 'is_active', 'created_at']

admin.site.register(ClientAdPhotos)
admin.site.register(Terms_and_conditions)