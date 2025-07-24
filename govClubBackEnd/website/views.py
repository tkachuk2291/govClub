from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Homepage, CourseAnnouncementCard, Team
from .serializers import HomepageSerializer, CourseDetailSerializer, FeedbackSerializer, TeamSerializer


class HomepageView(APIView):
    def get(self, request):
        homepage = Homepage.objects.first()
        serializer = HomepageSerializer(homepage)
        return Response(serializer.data)


class CourseCardDetail(APIView):
    def get(self, request, slug):
        course_detail = CourseAnnouncementCard.objects.get(slug=slug).course_detail
        serializer = CourseDetailSerializer(course_detail)
        return Response(serializer.data, status=200)


class Feedback(APIView):
    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamView(APIView):
    def get(self, request):
        team = Team.objects.first()
        print(team , 'DDD')
        serializer = TeamSerializer(team)
        return Response(serializer.data, status=status.HTTP_200_OK)