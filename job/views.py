from django.shortcuts import render
from .models import JobPost, VideshJobPost, NormalJobPost, CarouselSlider, ClientAdPhotos
from .forms import NormalJobPostForm, AddSliderForm, CarouselSliderForm, ClientAdPhotosForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from django.views.generic import CreateView, ListView,UpdateView, DeleteView
from django.urls import reverse_lazy

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
    normal_job_posts = NormalJobPost.objects.all()
    videsh_job_posts = VideshJobPost.objects.all()
    
    # Combine data from both models into a single list
    job_lists = list(normal_job_posts) + list(videsh_job_posts)
    return render(request, "job/dashboard.html", {'job_lists': job_lists})


def index(request):
    return render(request, "job/base.html")



@login_required(login_url = '/login')
def approved_job_list(request):
    approved_job_lists = JobPost.objects.filter(is_approved=True)
    return render(request, 'job/approved_job_list.html', {
        'approved_job_lists': approved_job_lists,
    })


#=======================================================================================





from django.shortcuts import render, get_object_or_404
from .models import VideshJobPost

from .forms import VideshJobPostForm

def create_job_post(request):
    if request.method == 'POST':
        form = VideshJobPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('job:videsh_job_list')  # Redirect to the job list page after creating a post
    else:
        form = VideshJobPostForm()
    return render(request, 'job/create_videsh_job_post.html', {'form': form})



def videsh_job_list(request):
    videsh_job_posts = VideshJobPost.objects.all()
    return render(request, 'job/videsh_job_list.html', {'videsh_job_posts': videsh_job_posts})

def videsh_job_detail(request, pk):
    videsh_job_posts = get_object_or_404(VideshJobPost, pk=pk)
    return render(request, 'job_detail.html', {'videsh_job_posts': videsh_job_posts})


def update_videsh_job_post(request, pk):
    videsh_job_post = get_object_or_404(VideshJobPost, pk=pk)

    if request.method == 'POST':
        form = VideshJobPostForm(request.POST, request.FILES, instance=videsh_job_post)
        if form.is_valid():
            form.save()
            return redirect('job:videsh_job_list')  # Redirect to the job list page after updating the post
    else:
        form = VideshJobPostForm(instance=videsh_job_post)
    return render(request, 'job/update_videsh_job_post.html', {'form': form})

def delete_videsh_job_post(request, pk):
    videsh_job_post = get_object_or_404(VideshJobPost, pk=pk)
    if request.method == 'POST':
        videsh_job_post.delete()
    return redirect('job:normal_job_list')




def client_interview_posts(request):
    job_posts = VideshJobPost.objects.filter(job_category='CI')
    return render(request, 'job/client_interview_posts.html', {'job_posts': job_posts})

def telephonic_interview_posts(request):
    job_posts = VideshJobPost.objects.filter(job_category='TI')
    return render(request, 'job/telephonic_interview_posts.html', {'job_posts': job_posts})


def licence_holder_posts(request):
    job_posts = VideshJobPost.objects.filter(job_category='LH')
    return render(request, 'job/license_holder_posts.html', {'job_posts': job_posts})


def cv_selection_posts(request):
    job_posts = VideshJobPost.objects.filter(job_category='CS')
    return render(request, 'job/cv_selection_posts.html', {'job_posts': job_posts})


def create_normal_job_post(request):
    if request.method == 'POST':
        form = NormalJobPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('job:normal_job_list')  # Redirect to the job list page after creating a post
    else:
        form = NormalJobPostForm()
    return render(request, 'job/create_normal_job_post.html', {'form': form})


def normal_job_list(request):
    normal_job_posts = NormalJobPost.objects.all()
    return render(request, 'job/normal_job_list.html', {'normal_job_posts': normal_job_posts})

def normal_job_detail(request, pk):
    normal_job_post = get_object_or_404(NormalJobPost, pk=pk)
    return render(request, 'normal_job_detail.html', {'normal_job_post': normal_job_post})



def update_normal_job_post(request, pk):
    normal_job_post = get_object_or_404(NormalJobPost, pk=pk)
    if request.method == 'POST':
        form = NormalJobPostForm(request.POST, request.FILES, instance=normal_job_post)
        if form.is_valid():
            form.save()
            return redirect('job:normal_job_list')  # Redirect to the job list page after updating the post
    else:
        form = NormalJobPostForm(instance=normal_job_post)
    return render(request, 'job/update_normal_job_post.html', {'form': form})


def delete_normal_job_post(request, pk):
    normal_job_post = get_object_or_404(NormalJobPost, pk=pk)
    if request.method == 'POST':
        normal_job_post.delete()
    return redirect('job:normal_job_list')


def show_hospital_jobs(request):
    hospital_jobs = NormalJobPost.objects.filter(job_category='HS')
    return render(request, 'job/hospital_jobs.html', {'hospital_jobs': hospital_jobs})




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


class CarouselSliderUpdate(UpdateView):
    model = CarouselSlider
    form_class = CarouselSliderForm
    template_name = 'job/update_carousel.html'
    success_url = reverse_lazy('job:sliders')

class CarouselSliderDelete(DeleteView):
    model = CarouselSlider
    # template_name = 'yourapp/carouselslider_confirm_delete.html'
    success_url = reverse_lazy('job:sliders')



class ClientAdPhotosList(ListView):
    model = ClientAdPhotos
    template_name = 'job/clientadphotos_list.html'
    context_object_name = 'ad_photos'


class ClientAdPhotosCreate(CreateView):
    model = ClientAdPhotos
    form_class = ClientAdPhotosForm
    template_name = 'job/clientadphotos_form.html'
    success_url = reverse_lazy('job:ad_photo_list')


class ClientAdPhotosUpdate(UpdateView):
    model = ClientAdPhotos
    form_class = ClientAdPhotosForm
    template_name = 'job/clientadphotos_form.html'
    success_url = reverse_lazy('job:ad_photo_list')

class ClientAdPhotosDelete(DeleteView):
    model = ClientAdPhotos
    template_name = 'job/clientadphotos_confirm_delete.html'
    success_url = reverse_lazy('job:ad_photo_list')