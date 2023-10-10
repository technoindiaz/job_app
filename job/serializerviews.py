from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import JobPost, CarouselSlider, JobCategory
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
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
    



@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def create_job_post(request):
    if request.method == 'POST':
        serializer = JobPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)