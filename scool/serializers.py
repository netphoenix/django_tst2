from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'course_num', 'description']

# from rest_framework.renderers import JSONRenderer

# class Course:
#     def __init__(self, name, descr) -> None:
#         self.name = name
#         self.desc = descr

# class CourseSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     descr = serializers.CharField()
    
# model = Course('dfdfgdfg','fgdfgd')
# model_sr = CourseSerializer(model)
# json = JSONRenderer().render(model_sr.data)

# model_sr.is_valid()