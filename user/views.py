from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.postgres.search import SearchVector
from rest_framework.pagination import PageNumberPagination
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class TokenRefreshView(TokenRefreshView):
    pass
class UserSearchView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        query = self.request.query_params.get('q')
        if query:
            return User.objects.annotate(
                search=SearchVector('username', 'email')
            ).filter(search=query)
        return User.objects.none()
class FriendRequestView(APIView):
    def post(self, request, *args, **kwargs):
            pass

    def patch(self, request, *args, **kwargs):
        # Accept or reject friend request
        pass