from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import JobPost, CarouselSlider, JobCategory, VideshJobPost
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from .serializers import CarouselSerializer, JobPostSerializer, JobCategorySerialzer, VideshJobPostSerializer


class JobCategoryListCreateView(generics.ListCreateAPIView):
    queryset = JobCategory.objects.all()
    serializer_class = JobCategorySerialzer



class JobPostCreateListView(generics.ListCreateAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer


class JobPostUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer



class CarouselView(generics.ListAPIView):
    queryset = CarouselSlider.objects.all()
    serializer_class = CarouselSerializer


class JobPostsByCategoryAPIView(ListAPIView):
    serializer_class = JobPostSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return JobPost.objects.filter(job_category=category_id)
    



@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def create_job_post(request):
    if request.method == 'POST':
        serializer = JobPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser


@csrf_exempt
def videsh_job_list(request):
    if request.method == 'GET':
        videsh_jobs = VideshJobPost.objects.all()
        serializer = VideshJobPostSerializer(videsh_jobs, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VideshJobPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

class ClientInterviewJobPostList(generics.ListAPIView):
    queryset = VideshJobPost.objects.filter(job_category='CI')
    serializer_class = VideshJobPostSerializer

class CVSelectionJobPostList(generics.ListAPIView):
    queryset = VideshJobPost.objects.filter(job_category='CS')
    serializer_class = VideshJobPostSerializer

class TelephonicInterviewJobPostList(generics.ListAPIView):
    queryset = VideshJobPost.objects.filter(job_category='TI')
    serializer_class = VideshJobPostSerializer

class LicenseHolderJobPostList(generics.ListAPIView):
    queryset = VideshJobPost.objects.filter(job_category='LH')
    serializer_class = VideshJobPostSerializer