from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.
class JobCategory(models.Model):
    job_category_id = models.AutoField(primary_key=True)
    job_category_name = models.CharField(max_length=100)
    job_category_description = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.job_category_name

    
def validate_image_size(value):
    max_size = 2 * 1024 * 1024  # 2 MB
    if value.size > max_size:
        raise ValidationError(_('File size should not be more than 2 MB.'))

class JobPost(models.Model):
    id = models.AutoField(primary_key=True)
    job_category = models.ForeignKey(JobCategory, on_delete=models.DO_NOTHING, null=True, blank=True)
    post_name = models.CharField(max_length=200)
    post_image = models.ImageField(upload_to='job_posts', validators=[validate_image_size])
    whatsapp_phone = models.IntegerField(blank=True, null=True)
    mobile_phone = models.IntegerField()
    website = models.URLField(blank=True, null=True)
    city = models.CharField(max_length=100)
    post_description = models.TextField()
    is_approved = models.BooleanField(default=False, null=True, blank=True)
    is_active = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.post_name



# class JobManager(models.Model):
#     id = models.AutoField(primary_key=True)
#     job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
#     is_approved = models.BooleanField(default=False, null=True, blank=True)
#     is_active = models.BooleanField(default=False, null=True, blank=True)
#     job_period = models.IntegerField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.job}"


VIDESH_JOB_CATEGORY = (
    ('CI', 'Client Interview'),
    ('CS', 'CV Selection'),
    ('TI', 'Telephonic Interview'),
    ('LH', 'License Holder'),
)

class VideshJobPost(models.Model):
    id = models.AutoField(primary_key=True)
    job_category = models.CharField(choices= VIDESH_JOB_CATEGORY, max_length=100, null=True, blank=True)
    post_name = models.CharField(max_length=200)
    post_image = models.ImageField(upload_to='job_posts', validators=[validate_image_size])
    whatsapp_phone = models.IntegerField(blank=True, null=True)
    mobile_phone = models.IntegerField()
    website = models.URLField(blank=True, null=True)
    city = models.CharField(max_length=100)
    post_description = models.TextField()
    is_approved = models.BooleanField(default=False, null=True, blank=True)
    is_active = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.post_name

    


class CarouselSlider(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='home_sliders', null=True, blank=True)
    image2 = models.ImageField(upload_to='home_sliders', null=True, blank=True)
    image3 = models.ImageField(upload_to='home_sliders', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class AdPhotos(models.Model):
    id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=200)
    ad_type = models.CharField(max_length=100)
    ad_name = models.CharField(max_length=100)
    ad_image1 = models.ImageField(upload_to='ad_images', blank=True, null=True)
    ad_image2 = models.ImageField(upload_to='ad_images', blank=True, null=True)
    ad_image3 = models.ImageField(upload_to='ad_images', blank=True, null=True)
    ad_image4 = models.ImageField(upload_to='ad_images', blank=True, null=True)
    ad_price = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.client_name

