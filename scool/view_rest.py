from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course
from django.forms.models import model_to_dict
from rest_framework import generics
from .serializers import CourseSerializer

from rest_framework.permissions import IsAuthenticated, IsAdminUser

class CourseAPIView(APIView):
    # def get(self, request):
    #     return Response({'name':'Python', 'num':'11'})
    
    # def post(self, request):
    #     return Response({'name':'js', 'num':'22'})
    
    def get(self, r):
        courses = Course.objects.all().values()
        return Response({'courses':list(courses)})
    
    def post(self, r):
        course = Course.objects.create(
            name = r.data['name'],
            course_num = r.data['num'],  
            description = r.data['descr']
        )

        return Response(
            {'course': model_to_dict(course)}
        )
    
    # def put(self,r):

# class CourseAPIView2(generics.ListAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer

class CourseAPIView2(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseAPIUpdate(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = IsAuthenticated

class  CourseAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

from rest_framework import viewsets

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    