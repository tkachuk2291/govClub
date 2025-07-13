from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Homepage
from .serializers import  HomepageSerializer


# Create your views here.

class HomepageView(APIView):
    def get(self, request):
        homepage = Homepage.objects.first()
        serializer = HomepageSerializer(homepage)
        return Response(serializer.data)
