from django.shortcuts import render
from .models import JobPost, JobCategory, CarouselSlider
from .forms import JobPostForm, JobCategoryForm, AddSliderForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout

# Create your views here.

def Register(request):
    if request.method=="POST":   
        username = request.POST['username']
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('/register')
        
        user = User.objects.create_user(username, email, password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return render(request, 'login.html')   
    return render(request, "job/accounts/register.html")




def Login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("job:dashboard")
        else:
            messages.error(request, "Invalid Credentials")
        return render(request, "job/accounts/login.html")
        # return render(request, 'blog.html')   
    return render(request, "job/accounts/login.html")

def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/login')



@login_required(login_url = '/login')
def dashboard(request):
    return render(request, "job/dashboard.html")


def index(request):
    return render(request, "job/base.html")


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


# def job_approve_list(request):
#     job_approve_lists = JobManager.objects.all()
#     context = {
#         'job_approve_lists':job_approve_lists
#     }
#     return render(request, "job/approve_job_list.html", context)


@login_required(login_url = '/login')
def approved_job_list(request):
    approved_job_lists = JobPost.objects.filter(is_approved=True)
    return render(request, 'job/approved_job_list.html', {
        'approved_job_lists': approved_job_lists,
    })


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













































#==================== API Views ===================#
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import JobPostSerializer

class JobPostCreateListView(generics.ListCreateAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer


class JobPostUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
