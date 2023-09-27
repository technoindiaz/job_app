from django.urls import path
from job import views
from .views import JobPostCreateListView, JobPostUpdateDelete
app_name = 'job'

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.dashboard, name='dashboard'), 
    # path('job/create/', views.create_job_post, name='create_job_post'),
    path('create_job_post', views.CreateJobPost.as_view(), name='create_job_post'),
    path('<int:pk>/', views.update_job_post, name='update_job_post'),
    path('job-list', views.job_list, name='job-list'), 
    path('approve-job-list', views.approved_job_list, name='approve-job-list'),
    path('delete_post/<int:id>/', views.delete_job_post, name='delete_post'), 

    #===================APIS URLS==================
    path('api', JobPostCreateListView.as_view()),
    path('<int:id>', JobPostCreateListView.as_view()),
]   
