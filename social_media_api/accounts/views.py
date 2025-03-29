from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer, LoginSerializer, FeedSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status, generics, permissions
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class RegisterAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user =user)
            return Response({"token":token.key,"user":CustomUserSerializer(user).data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        
class LoginAPIView(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            user = authenticate(username=username,password=password)
            if not user:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
            token ,created = Token.objects.get_or_create(user=user)
            return Response({"token":token.key,"message":"authenicated user"},
                            status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]  
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        print("User:", request.user)
        user = request.user
        return Response({"user": CustomUserSerializer(user).data})

class FollowAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    
    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id =user_id)
        if user_to_follow == request.user:
            return Response({"message":"you cannot follow yourself"},status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(user_to_follow)
        return Response({"message":f"you are following {user_to_follow.username}"},status=status.HTTP_200_OK)

class UnFollowAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    
    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id =user_id)
        if user_to_unfollow == request.user:
            return Response({"message":"you cannot unfollow yourself"},status=status.HTTP_400_BAD_REQUEST)
        request.user.following.remove(user_to_unfollow)
        return Response({"message":f"you unfollowed {user_to_unfollow.username}"},status=status.HTTP_200_OK)
    
class FeedView(generics.ListAPIView):
    serializer_class = FeedSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.request.user)
        return Response(serializer.data)