from rest_framework import serializers

class Course:
    def __init__(self, name, descr) -> None:
        self.name = name
        self.desc = descr

class CourseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    descr = serializers.CharField()
    
