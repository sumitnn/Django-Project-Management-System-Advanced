from django.shortcuts import render
from .serializer import ProjectSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import Project
# Create your views here.


class ProjectDetail(APIView):
    def get(self, request, pk, format=None):
        try:
            snippet = Project.objects.get(id=pk)
        except:
            return Response({"error": "No Data Found", "code": 0}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(snippet)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        try:
            snippet = Project.objects.get(project_id=pk)
        except:
            return Response({"error": "No Data Found", "code": 0}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProjectSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors, "code": 0}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        try:
            project = Project.objects.get(project_id=pk)
        except:
            return Response({"error": "No Data Found", "code": 0}, status=status.HTTP_404_NOT_FOUND)
        project.delete()
        return Response({"message": "Delete successfully", "code": 1}, status=status.HTTP_204_NO_CONTENT)
