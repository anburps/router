from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from app.models import Blog, GetToken
from app.serializers import BlogSerializer, GetTokenSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication,BasicAuthentication
from django.contrib.auth import authenticate, logout
from rest_framework.permissions import IsAuthenticated


class BlogModelViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes  = [IsAuthenticated]
    lookup_field = "pk"

class GenerateToken(APIView):
    authentication_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class Logout(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response({"message": "Logout success"},status=status.HTTP_204_NO_CONTENT)
