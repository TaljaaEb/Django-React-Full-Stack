from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer, InstrumentSerializer, CardSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.serializers import Serializer
from .models import Note, Card, Instrument

class ISerializer(Serializer):
    from rest_framework import serializers
    client_id = serializers.IntegerField(required=True, error_messages={'required': 'Custom error message'})


class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer  
    permission_classes = [AllowAny]

