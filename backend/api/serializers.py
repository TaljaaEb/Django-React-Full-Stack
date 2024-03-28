from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note, Card, Instrument, IRecord


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user

class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IRecord
        extra_kwargs = {"reply": {"read_only": True}}
        error_messages = {"required": {"read_only": True}}
#        model = Instrument
#        fields = ["id", "action", "reply", "order"]
#        extra_kwargs = {"reply": {"read_only": True}}

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ["id", "cnumber", "expire_on", "cvv"]
        extra_kwargs = {"cvv": {"read_only": True}}