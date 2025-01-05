from django.shortcuts import render
from .serializers import RegisterSerializer, LoginSerializer, ChatSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Chat

# Register user and create JWT tokens
@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "message": "You've been registered"
            }, status=HTTP_201_CREATED
        )
    else:
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

# Login API to provide JWT tokens
@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)
        print(user)
        print(request.data)

        if user is not None:
            # Generate both access and refresh tokens
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "user": username,
                    "access_token": str(refresh.access_token),
                    "refresh_token": str(refresh),
                }, status=HTTP_200_OK
            )
        else:
            return Response(
                {
                    "message": "Invalid credentials"
                }, status=HTTP_401_UNAUTHORIZED
            )
    else:
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

# Chat View to process user messages and deduct tokens
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def chatView(request):
    user = request.user
    message = request.data.get('message')

    if not message:
        return Response({"error": "Message required"}, status=HTTP_400_BAD_REQUEST)

    if user.tokens < 100:
        return Response({"error": "Insufficient tokens"}, status=HTTP_400_BAD_REQUEST)

    user.tokens -= 100  # Deduct tokens
    user.save()

    # Simulate an AI response (dummy response)
    ai_response = "Dummy response based on your message"
    chat = Chat.objects.create(user=user, message=message, response=ai_response)
    serializer = ChatSerializer(chat)

    return Response(serializer.data, status=HTTP_200_OK)

# Token Balance API to return the user's current token balance
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def token_balance(request):
    """
    API endpoint to return the user's current token balance.
    """
    user = request.user
    return Response({"tokens": user.tokens}, status=HTTP_200_OK)
