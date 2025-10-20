from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer

class CourseList(APIView):
    def get(self, request):
        queryset = Course.objects.all().order_by("code")
        data = CourseSerializer(queryset, many=True).data
        return Response(data)