from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, "job/dashboard.html")


def index(request):
    return render(request, "job/base.html")


def job_list(request):
    job_lists = JobPost.objects.all()
    context = {
        'job_lists':job_lists
    }
    return render(request, "job/job_list.html", context)

#==================== API Views ===================#
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import JobPost
from .serializers import JobPostSerializer

@api_view(['GET'])
def job_post_list(request):
    job_posts = JobPost.objects.all()
    serializer = JobPostSerializer(job_posts, many=True)
    return Response(serializer.data)


class JobPostListCreateView(generics.ListCreateAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer


