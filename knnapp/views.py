from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status,serializers
from .serialisers import FileSerializer
import pandas as pd
import os
import knnapp.knn_algorithm
class IncredibleInputSerializer(serializers.Serializer):
    model_input = serializers.FileField()
class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)
  def post(self, request, *args, **kwargs):
    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_instance=file_serializer.save()

      file_obj=request.data["file"]

      predicted_location=knnapp.knn_algorithm.knn_algo(str(file_obj),SSID=str(request.data["remark"]))

      os.remove("./media/"+str(file_obj))
      #knnapp.knn_algorithm.knn_algo()
      #return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      print(predicted_location)

      if predicted_location== current_timetable(request.data["student_id"]):
        return HttpResponse("success", content_type="text/plain")
      else:

        return HttpResponse("wrong location", content_type="text/plain")
    else:

      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationView(APIView):
  parser_classes = (MultiPartParser, FormParser)

  def post(self, request, *args, **kwargs):
    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_instance=file_serializer.save()

      file_obj=request.data["file"]
      print(os.getcwd())
      print(str(file_obj))
      csv_data=pd.read_csv("./media/"+str(file_obj))


      predicted_location = knnapp.knn_algorithm.knn_algo(str(file_obj), SSID=str(request.data["remark"]))
      os.remove("./media/" + str(file_obj))
      return HttpResponse(predicted_location, content_type="text/plain")
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def current_timetable(studentid):
  return "Computing building"
