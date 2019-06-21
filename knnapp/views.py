from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status,serializers
from .serialisers import FileSerializer
import pandas as pd
import os
class IncredibleInputSerializer(serializers.Serializer):
    model_input = serializers.FileField()
class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)
  def post(self, request, *args, **kwargs):
    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_instance=file_serializer.save()

      file_obj=request.data["file"]
      print(os.getcwd())
      csv_data=pd.read_csv("./media/"+str(file_obj))
      print(csv_data.head())
      os.remove("./media/"+str(file_obj))
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)