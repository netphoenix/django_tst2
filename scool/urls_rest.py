from django.urls import path, include
from .view_rest import *

# api/v1/courses

urlpatterns = [
    path(('v1/courses/'), CourseAPIView.as_view()),
    path(('v2/courses/'), CourseAPIView2.as_view()),
    path(('v2/courses/<int:pk>/'), CourseAPIUpdate.as_view()),
    path(('v2/coursesdetail/<int:pk>/'), CourseAPIDetailView.as_view()),
    path(('v3/courses/'), CourseViewSet.as_view({'get':'list','post':'create'})),
    path(('v3/courses/<int:pk>/'), CourseViewSet.as_view({'get':'retrieve'})),
    path(('v3/scool-auth/'), include('rest_framework.urls')),
    
]