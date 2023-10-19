from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import ClientAdPhotos, JobPost, CarouselSlider, JobCategory, VideshJobPost, NormalJobPost, Terms_and_conditions
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from .serializers import CarouselSerializer, CarouselSliderSerializer, ClientAdPhotosSerializer, JobPostSerializer, JobCategorySerialzer, TermsAndConditionsSerializer, VideshJobPostSerializer, NormalJobPostSerializer


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
        videsh_jobs = VideshJobPost.objects.filter(is_active=True, is_approved=True)
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
    queryset = VideshJobPost.objects.filter(job_category='CI', is_active=True, is_approved=True)
    serializer_class = VideshJobPostSerializer

class CVSelectionJobPostList(generics.ListAPIView):
    queryset = VideshJobPost.objects.filter(job_category='CS', is_active=True, is_approved=True)
    serializer_class = VideshJobPostSerializer

class TelephonicInterviewJobPostList(generics.ListAPIView):
    queryset = VideshJobPost.objects.filter(job_category='TI', is_active=True, is_approved=True)
    serializer_class = VideshJobPostSerializer

class LicenseHolderJobPostList(generics.ListAPIView):
    queryset = VideshJobPost.objects.filter(job_category='LH', is_active=True, is_approved=True)
    serializer_class = VideshJobPostSerializer



@csrf_exempt
# @api_view(['GET', 'POST'])
def normal_job_post_list(request):
    if request.method == 'GET':
        job_posts = NormalJobPost.objects.filter(is_active=True, is_approved=True)
        serializer = NormalJobPostSerializer(job_posts, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NormalJobPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def normal_job_post_detail(request, pk):
    try:
        job_post = NormalJobPost.objects.get(pk=pk)
    except NormalJobPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NormalJobPostSerializer(job_post)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        serializer = NormalJobPostSerializer(job_post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        job_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class DeshMeJobPostList(generics.ListAPIView):
    queryset = NormalJobPost.objects.filter(job_category='DS', is_active=True, is_approved=True)
    serializer_class = NormalJobPostSerializer

class HosptialMeJobPostList(generics.ListAPIView):
    queryset = NormalJobPost.objects.filter(job_category='HS', is_active=True, is_approved=True)
    serializer_class = NormalJobPostSerializer



class CarouselSliderList(generics.ListAPIView):
    queryset = CarouselSlider.objects.filter(is_active=True)
    serializer_class = CarouselSliderSerializer



class ClientAdPhotosList(generics.ListAPIView):
    queryset = ClientAdPhotos.objects.filter(is_active=True)
    serializer_class = ClientAdPhotosSerializer


class TermsAndConditionsList(generics.ListAPIView):
    queryset = Terms_and_conditions.objects.all()
    serializer_class = TermsAndConditionsSerializer