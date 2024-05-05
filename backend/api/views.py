from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import *

# Create your views here.
class UserView(APIView):
    class Meta:
        models = User
        fields = '__all__'

    def get(self, request, format = None):

        username = [username for username in User.objects.all()]
        return Response(username)