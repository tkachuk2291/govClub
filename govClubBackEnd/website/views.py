from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Homepage, CourseAnnouncementCard
from .serializers import HomepageSerializer, CourseDetailSerializer


class HomepageView(APIView):
    def get(self, request):
        homepage = Homepage.objects.first()
        serializer = HomepageSerializer(homepage)
        return Response(serializer.data)


class CourseCardDetail(APIView):
    def get(self , request , slug):
        course_detail = CourseAnnouncementCard.objects.get(slug=slug).course_detail
        serializer = CourseDetailSerializer(course_detail)
        return Response(serializer.data , status=200)

# avtorskyi-kurs-z-komunikatsii/

