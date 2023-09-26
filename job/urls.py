from django.urls import path
from job import views
app_name = 'job'

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.dashboard, name='dashboard'), 
    path('job-list', views.job_list, name='job-list'), 

    path('job_posts/', views.job_post_list, name='job_post_list'), 
]   
