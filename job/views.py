from django.shortcuts import render
from .models import JobPost
from .forms import JobPostForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, CreateView
# Create your views here.

def dashboard(request):
    return render(request, "job/dashboard.html")


def index(request):
    return render(request, "job/base.html")


# Create
class CreateJobPost(CreateView):
    form_class = JobPostForm
    template_name = 'job/create_job_post.html'
    success_url = 'job-list'



def update_job_post(request, id):
    # job_post = get_object_or_404(JobPost, pk=id)
    if request.method == 'POST':
        job_post = JobPost.objects.get(pk=id)
        form = JobPostForm(request.POST, instance=job_post)
        if form.is_valid():
            form.save()
            return redirect('job-list')
    else:
        job_post = JobPost.objects.get(pk=id)
        form = JobPostForm(instance=job_post)
    return render(request, 'job/update_job_post.html', {'form': form, 'job_post': job_post})    


def delete_job_post(request, id):
    if request.method == 'POST':
        job_post = JobPost.objects.get(pk=id)
        job_post.delete()
        return redirect('job:job-list')



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



def approved_job_list(request):
    approved_job_list = JobPost.objects.filter(is_approved=True)
    return render(request, 'job/approved_job_list.html', {
        'approved_job_list': approved_job_list,
        
    })




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

