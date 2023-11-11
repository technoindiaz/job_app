from django.urls import path
from job import views
from job import serializerviews
from .serializerviews import JobPostCreateListView, CarouselView, JobPostsByCategoryAPIView


app_name = 'job'

urlpatterns = [
    #    user authentication
    path("register/", views.Register, name="register"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
    path('index', views.index, name='index'),
    path('', views.dashboard, name='dashboard'), 
    
    #------------------------New URLS----------------------------------#
    path('approve-job-list', views.approved_job_list, name='approve-job-list'),
    path('create_videsh_job', views.create_job_post, name='create_videsh_job'),
    path('videsh_job_list/', views.videsh_job_list, name='videsh_job_list'),
    path('videsh_job/<int:pk>/', views.videsh_job_detail, name='job_detail'),
    path('videsh_job/update/<int:pk>/', views.update_videsh_job_post, name='update_videsh_job_post'),
    path('client_interview', views.client_interview_posts, name='client_interview'),
    path('delete_videsh_job_post/<int:pk>/', views.delete_videsh_job_post, name='delete_videsh_job_post'),
    path('telephonic_interview', views.telephonic_interview_posts, name='telephonic_interview'),
    path('licence_holder', views.licence_holder_posts, name='licence_holder'),
    path('cv_selection', views.cv_selection_posts, name='cv_selection'),
    path('job/create/', views.create_normal_job_post, name='create_normal_job_post'),
    path('normal_job_list', views.normal_job_list, name='normal_job_list'),
    path('job/<int:pk>/', views.normal_job_detail, name='normal_job_detail'),
    path('update_normal_job_post/<int:pk>/', views.update_normal_job_post, name='update_normal_job_post'),
    path('delete_normal_job_post/<int:pk>/', views.delete_normal_job_post, name='delete_normal_job_post'),
    path('show_hospital_jobs', views.show_hospital_jobs, name='show_hospital_jobs'),
    path('create_normal_job_post', views.create_normal_job_post, name='create_normal_job_post'),
    path('sliders', views.show_carousel_slider, name='sliders'),
    path('add_sliders', views.CarouselSliderCreateView.as_view(), name='add_sliders'),
    path('slider_update/<int:pk>/', views.CarouselSliderUpdate.as_view(), name='slider_update'),
    path('slider_delete/<int:pk>/', views.CarouselSliderDelete.as_view(), name='slider_delete'),
    
    path('ad_photo_list', views.ClientAdPhotosList.as_view(), name='ad_photo_list'),
    path('ad_photos_create/', views.ClientAdPhotosCreate.as_view(), name='ad_photos_create'),
    path('ad_photos_update/<int:pk>/', views.ClientAdPhotosUpdate.as_view(), name='ad_photos_update'),
    path('ad_photos_delete/<int:pk>/', views.ClientAdPhotosDelete.as_view(), name='ad_photos_delete'),
    path('terms_and_conditions', views.TermsAndConditionsListView.as_view(), name='terms_and_conditions'),
    path('terms_and_conditions_create', views.TermsAndConditionsCreateView.as_view(), name='terms_and_conditions_create'),
    path('terms_and_conditions_update/<int:pk>/', views.TermsAndConditionsUpdateView.as_view(), name='terms_and_conditions_update'),
    path('terms_and_conditions_delete/<int:pk>/', views.TermsAndConditionsDeleteView.as_view(), name='terms_and_conditions_delete'),
    path('privacy-policy', views.privacy_policy, name='privacy-policy'),


    #===================APIS URLS==================
    path('api/job-categories/', serializerviews.JobCategoryListCreateView.as_view(), name='job-category-list'),
    path('api/job-posts-by-category/<int:category_id>/', JobPostsByCategoryAPIView.as_view(), name='job-posts-by-category'),
    path('api/job-list', JobPostCreateListView.as_view()),
    path('<int:id>', JobPostCreateListView.as_view()),
    path('api/carousel-slider', CarouselView.as_view(), name='api/carousel-slider'),
    # path('api/category/', serializerviews.show_school_jobs)
    path('api/create_job_post/', serializerviews.create_job_post, name='api_create_job_post'),
    path('api/videsh_job_list', serializerviews.videsh_job_list),
    path('api/client-interview/', serializerviews.ClientInterviewJobPostList.as_view(), name='client-interview-job-list'),
    path('api/cv-selection/', serializerviews.CVSelectionJobPostList.as_view(), name='cv-selection-job-list'),
    path('api/telephonic-interview/', serializerviews.TelephonicInterviewJobPostList.as_view(), name='telephonic-interview-job-list'),
    path('api/license-holder/', serializerviews.LicenseHolderJobPostList.as_view(), name='license-holder-job-list'),
    path('api/normal-job-posts/', serializerviews.normal_job_post_list, name='normal-job-post-list'),
    path('api/normal-job-posts/<int:pk>/', serializerviews.normal_job_post_detail, name='normal-job-post-detail'),
    path('api/desh_me_job/', serializerviews.DeshMeJobPostList.as_view(), name='desh-me-job-list'),
    path('api/hospital_me_job/', serializerviews.HosptialMeJobPostList.as_view(), name='hospital-me-job-list'),
    path('api/carousel/', serializerviews.CarouselSliderList.as_view(), name='carousel'),
    path('api/adphotos/', serializerviews.ClientAdPhotosList.as_view(), name='adphotos'),
    path('api/terms', serializerviews.TermsAndConditionsList.as_view(), name='terms'),
    
]   


































    # path('job/create/', views.create_job_post, name='create_job_post'),
    # path('create_job_post', views.CreateJobPost.as_view(), name='create_job_post'),
    # path('job_post/<int:pk>/update/', views.JobPostUpdateView.as_view(), name='job_post_update'),
    
    # path('job-list', views.job_list, name='job-list'), 
    # 
    # path('delete_post/<int:id>/', views.delete_job_post, name='delete_post'), 
    # path('category-list', views.show_job_categories, name='category-list'),
    # path('create_job_category', views.JobCategoryCreateView.as_view(), name='create_job_category'),
    # path('category/<int:pk>/update/', views.JobCategoryUpdateView.as_view(), name='category_update'),
    # path('sliders', views.show_carousel_slider, name='sliders'),
    # path('add_sliders', views.CarouselSliderCreateView.as_view(), name='add_sliders'),
    # # path('videsh-job', views.show_videsh_job, name='videsh-job'),
    # # path('desh-job', views.show_desh_job, name='desh-job'),
    # # path('school-job', views.show_school_job, name='school-job'),
    # # path('hospital-job', views.show_hospital_job, name='hospital-job'),
    # # path('resturant-job', views.show_resturant_job, name='resturant-job'),
    # # path('medical-job', views.show_medical_store, name='medical-job'),

    # # path('jobs/<int:job_category_id>/', views.show_videsh_job, name='jobs-by-category'),

