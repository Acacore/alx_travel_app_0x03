from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.decorators import action
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import filters

from django.contrib.auth import get_user_model

User = get_user_model()


class SignUpViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = SignUpSerializer


class LoginViewset(viewsets.ViewSet):
    permission_classes = [AllowAny]
    
    @action(detail=False, methods=['post'])
    def login(self, request):
        serializers = LoginSerializer(data=request.data, context={"request":request})
        serializers.is_valid(raise_exception=True)
        user = serializers.validated_data['user']
        login(request, user)
        return Response({"status":"login in"}, status=status.HTTP_200_OK)
    
class HomePageView(viewsets.ViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]

     
class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return onlly the message created by the authenticated user
        user = self.request.user
        return self.queryset.filter(user=user)
    
    def perform_create(self, serializer):
        # Automatically set the user field to the authenticated
        serializer.save(user=self.request.user)


class ListingViewset(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return onlly the message created by the authenticated user
        user = self.request.user
        return self.queryset.filter(user=user)
    
    def perform_create(self, serializer):
        # Automatically set the user field to the authenticated
        serializer.save(host=self.request.user)  
 

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return onlly the message created by the authenticated user
        user = self.request.user
        return self.queryset.filter(id=user.id)
    
    def perform_create(self, serializer):
        # Automatically set the user field to the authenticated
        serializer.save(guest=self.request.user)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return onlly the message created by the authenticated user
        user = self.request.user
        return self.queryset.filter(user=user)
    
    def perform_create(self, serializer):
        # Automatically set the user field to the authenticated
        serializer.save(user=self.request.user)
