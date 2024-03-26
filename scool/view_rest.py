from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course


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
            description = r.data['descr'],
        )

        # return Response(
        #     {'course': model}
        # )