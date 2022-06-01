from email import message
from pickle import APPEND
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = """
                You're done)!
            """
            return Response(message)


