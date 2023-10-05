from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import JobPost, CarouselSlider, JobCategory
from rest_framework import generics


from .serializers import CarouselSerializer, JobPostSerializer, JobCategorySerialzer


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
    
