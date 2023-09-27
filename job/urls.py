from django.urls import path
from job import views
from .views import JobPostCreateListView

app_name = 'job'

urlpatterns = [
    #    user authentication
    path("register/", views.Register, name="register"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),

    path('index', views.index, name='index'),
    path('', views.dashboard, name='dashboard'), 
    # path('job/create/', views.create_job_post, name='create_job_post'),
    path('create_job_post', views.CreateJobPost.as_view(), name='create_job_post'),
    path('job_post/<int:pk>/update/', views.JobPostUpdateView.as_view(), name='job_post_update'),
    
    path('job-list', views.job_list, name='job-list'), 
    path('approve-job-list', views.approved_job_list, name='approve-job-list'),
    path('delete_post/<int:id>/', views.delete_job_post, name='delete_post'), 
    path('category-list', views.show_job_categories, name='category-list'),
    path('create_job_category', views.JobCategoryCreateView.as_view(), name='create_job_category'),
    path('category/<int:pk>/update/', views.JobCategoryUpdateView.as_view(), name='category_update'),
    path('sliders', views.show_carousel_slider, name='sliders'),
    path('add_sliders', views.CarouselSliderCreateView.as_view(), name='add_sliders'),
    

    #===================APIS URLS==================
    path('api', JobPostCreateListView.as_view()),
    path('<int:id>', JobPostCreateListView.as_view()),
]   
