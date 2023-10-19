# Generated by Django 4.2.5 on 2023-10-19 13:09

from django.db import migrations, models
import django.db.models.deletion
import job.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselSlider',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='home_sliders')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='home_sliders')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='home_sliders')),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClientAdPhotos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=200)),
                ('ad_type', models.CharField(max_length=100)),
                ('ad_name', models.CharField(max_length=100)),
                ('ad_image1', models.ImageField(blank=True, null=True, upload_to='ad_images')),
                ('ad_image2', models.ImageField(blank=True, null=True, upload_to='ad_images')),
                ('ad_price', models.PositiveIntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('job_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_category_name', models.CharField(max_length=100)),
                ('job_category_description', models.CharField(blank=True, max_length=200, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='NormalJobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_category', models.CharField(blank=True, choices=[('DS', 'Desh Me Job'), ('HS', 'Hospital Me Job')], max_length=100, null=True)),
                ('post_name', models.CharField(max_length=200)),
                ('post_image', models.ImageField(upload_to='job_posts', validators=[job.models.validate_image_size])),
                ('mobile_phone1', models.IntegerField()),
                ('mobile_phone2', models.IntegerField(blank=True, null=True)),
                ('whatsapp_phone', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(max_length=100)),
                ('post_description', models.TextField()),
                ('is_approved', models.BooleanField(blank=True, default=False, null=True)),
                ('is_active', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Terms_and_conditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matter', models.TextField(verbose_name='Please Write App terms & conditions here')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VideshJobPost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('job_category', models.CharField(blank=True, choices=[('CI', 'Client Interview'), ('CS', 'CV Selection'), ('TI', 'Telephonic Interview'), ('LH', 'License Holder')], max_length=100, null=True)),
                ('post_name', models.CharField(max_length=200)),
                ('post_image', models.ImageField(upload_to='job_posts', validators=[job.models.validate_image_size])),
                ('mobile_phone1', models.IntegerField()),
                ('mobile_phone2', models.IntegerField(blank=True, null=True)),
                ('whatsapp_phone', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(max_length=100)),
                ('post_description', models.TextField()),
                ('is_approved', models.BooleanField(blank=True, default=False, null=True)),
                ('is_active', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('post_name', models.CharField(max_length=200)),
                ('post_image', models.ImageField(upload_to='job_posts', validators=[job.models.validate_image_size])),
                ('whatsapp_phone', models.IntegerField(blank=True, null=True)),
                ('mobile_phone', models.IntegerField()),
                ('website', models.URLField(blank=True, null=True)),
                ('city', models.CharField(max_length=100)),
                ('post_description', models.TextField()),
                ('is_approved', models.BooleanField(blank=True, default=False, null=True)),
                ('is_active', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('job_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='job.jobcategory')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
