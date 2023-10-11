from django.shortcuts import render
from .models import JobPost, JobCategory, CarouselSlider, VideshJobPost, NormalJobPost
from .forms import JobPostForm, JobCategoryForm, AddSliderForm, NormalJobPostForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout


@login_required(login_url = '/login')
def show_job_categories(request):
    job_categories = JobCategory.objects.all()
    context = {
        'job_categories': job_categories
    }
    return render(request, "job/job_category_list.html", context)



class JobCategoryCreateView(CreateView):
    form_class = JobCategoryForm
    model = JobCategory
    template_name = "job/add_job_category.html"
    success_url = 'category-list'


class JobCategoryUpdateView(UpdateView):
    form_class = JobCategoryForm
    model = JobCategory
    template_name = "job/update_job_category.html"
    success_url = reverse_lazy('job:category-list')



def show_carousel_slider(request):
    sliders = CarouselSlider.objects.all()
    context = {
        'sliders':sliders
    }
    return render(request, "job/carousel_sliders.html", context)


class CarouselSliderCreateView(CreateView):
    form_class = AddSliderForm
    model = CarouselSlider
    template_name = "job/add_sliders.html"
    success_url = reverse_lazy('job:sliders')



def show_videsh_job(request, job_category_id):
    job_category = JobCategory.objects.get(pk=job_category_id)
    print(f"job_category_id: {job_category_id}")
    print(f"job_category: {job_category}")
    job_posts = JobPost.objects.filter(job_category=job_category_id)   
    print(f"job_posts: {job_posts}") 
    context = {
        'job_category': job_category,
        'job_posts': job_posts,
    }
    return render(request, "job/videsh_job_list.html", context)


def show_desh_job(request, job_category_id):
    job_category = JobCategory.objects.get(pk=job_category_id)
    print(f"job_category_id: {job_category_id}")
    print(f"job_category: {job_category}")
    job_posts = JobPost.objects.filter(job_category=job_category_id)   
    print(f"job_posts: {job_posts}") 
    context = {
        'job_category': job_category,
        'job_posts': job_posts,
    }
    return render(request, "job/desh_job.html", context)


def show_school_job(request, job_category_id):
    job_category = JobCategory.objects.get(pk=job_category_id)
    job_posts = JobPost.objects.filter(job_category=job_category_id)   
    print(f"job_posts: {job_posts}") 
    context = {
        'job_category': job_category,
        'job_posts': job_posts,
    }
    return render(request, "job/school_job.html", context)


def show_hospital_job(request, job_category_id):
    job_category = JobCategory.objects.get(pk=job_category_id)
    job_posts = JobPost.objects.filter(job_category=job_category_id)   
    context = {
        'job_category': job_category,
        'job_posts': job_posts,
    }
    return render(request, "job/hospital_job.html", context)


def show_resturant_job(request, job_category_id):
    job_category = JobCategory.objects.get(pk=job_category_id)
    job_posts = JobPost.objects.filter(job_category=job_category_id)    
    context = {
        'job_category': job_category,
        'job_posts': job_posts,
    }
    return render(request, "job/resturant_job.html", context)


def show_medical_store(request, job_category_id):
    job_category = JobCategory.objects.get(pk=job_category_id)
    # print(f"job_category_id: {job_category_id}")
    # print(f"job_category: {job_category}")
    job_posts = JobPost.objects.filter(job_category=job_category_id)   
    # print(f"job_posts: {job_posts}") 
    context = {
        'job_category': job_category,
        'job_posts': job_posts,
    }
    return render(request, "job/medical_store.html", context)


def show_telephonic_job(request, job_category_id):
    job_category = JobCategory.objects.get(pk=job_category_id)
    print(f"job_category_id: {job_category_id}")
    print(f"job_category: {job_category}")
    job_posts = JobPost.objects.filter(job_category=job_category_id)   
    print(f"job_posts: {job_posts}") 
    context = {
        'job_category': job_category,
        'job_posts': job_posts,
    }
    return render(request, "job/", context)



def show_license_holder_job(request, job_category_id):
    job_category = JobCategory.objects.get(pk=job_category_id)
    print(f"job_category_id: {job_category_id}")
    print(f"job_category: {job_category}")
    job_posts = JobPost.objects.filter(job_category=job_category_id)   
    print(f"job_posts: {job_posts}") 
    context = {
        'job_category': job_category,
        'job_posts': job_posts,
    }
    return render(request, "job/desh_job.html", context)





# Create
class CreateJobPost(CreateView):
    form_class = JobPostForm
    template_name = 'job/create_job_post.html'
    success_url = 'job-list'


class JobPostUpdateView(UpdateView):
    form_class = JobPostForm
    model = JobPost
    template_name = "job/update_job_post.html"
    success_url = reverse_lazy('job:job-list')



# def update_job_post(request, id):
#     # job_post = get_object_or_404(JobPost, pk=id)
#     if request.method == 'POST':
#         job_post = JobPost.objects.get(pk=id)
#         form = JobPostForm(request.POST, instance=job_post)
#         if form.is_valid():
#             form.save()
#             return redirect('job-list')
#     else:
#         job_post = JobPost.objects.get(pk=id)
#         form = JobPostForm(instance=job_post)
#     return render(request, 'job/update_job_post.html', {'form': form, 'job_post': job_post})    

@login_required(login_url = '/login')
def delete_job_post(request, id):
    if request.method == 'POST':
        job_post = JobPost.objects.get(pk=id)
        job_post.delete()
        return redirect('job:job-list')


@login_required(login_url = '/login')
def job_list(request):
    job_lists = JobPost.objects.all()
    context = {
        'job_lists':job_lists
    }
    return render(request, "job/job_list.html", context)
