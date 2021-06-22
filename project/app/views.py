from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .a import s
from rest_framework import status, viewsets


class add(APIView):
    def get(self, request):
        data = demo.objects.all().values('name', 'email', 'address', 'marks')
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        data = s(data=request.data)
        if data.is_valid():
            data.save()
            return Response("data added successfully! refresh to see changes.", status=status.HTTP_202_ACCEPTED)
        else:
            return Response("failed to add", status=status.HTTP_400_BAD_REQUEST)


class view(APIView):
    def get(self, request):
        data = demo.objects.all().values('name', 'email', 'address', 'marks')
        return Response(data, status=status.HTTP_200_OK)


class update(APIView):
    def get(self, request):
        data = demo.objects.all().values('name', 'email', 'address', 'marks')
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data['address']
        data1 = request.data['marks']
        demo.objects.filter(address=data).update(marks=data1)
        return Response("updated successfully! refresh to see changes.", status=status.HTTP_202_ACCEPTED)


class delete(APIView):
    def get(self, request):
        data = demo.objects.all().values('name', 'email', 'address', 'marks')
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data['name']
        demo.objects.filter(name=data).delete()
        return Response("deleted successfully! refresh to see changes.", status=status.HTTP_202_ACCEPTED)


class display(viewsets.ModelViewSet):
    queryset = demo.objects.all()
    serializer_class = s
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]