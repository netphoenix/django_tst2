from django.urls import path, include
from .view_rest import *

# api/v1/courses

urlpatterns = [
    path(('v1/courses/'), CourseAPIView.as_view()),
]