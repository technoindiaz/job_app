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
    list_display = ['post_name', 'job_category','post_image', 'whatsapp_phone', 'mobile_phone', 'website', 'city', 'post_description', 'is_approved', 'is_active','created_at', 'updated_at']



admin.site.register(CarouselSlider)
admin.site.register(AdPhotos)