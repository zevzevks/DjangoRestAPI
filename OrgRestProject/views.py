from wsgiref.util import request_uri
from .models import AdultTrain
from .serializers import AdultSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .mylogger import mylogger
import datetime

#method to test rest api
@api_view(['GET','POST'])
def adult_list(request,format = None):
    print('adults/')
    if request.method == 'GET':
        adults = AdultTrain.objects.all()
        serializer = AdultSerializer(adults, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = AdultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#method to test rest api put and delete commands
@api_view(['GET','PUT','DELETE'])
def adult_detail(request,id,format = None):
    request_timesptamp = datetime.datetime.now()
    try:
        adult = AdultTrain.objects.get(pk=id)
    except AdultTrain.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        response_status=status.HTTP_200_OK
        response_timestamp = datetime.datetime.now()
        serializer = AdultSerializer(adult)        
        mylogger.restlogger(request_timesptamp,request.path,request.data,response_timestamp,response_status,serializer.data)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AdultSerializer(adult,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        adult.delete()
        return Response(status = status.HTTP_200_OK)

#method to test rest api that filters data given by request    
@api_view(['POST'])
def adult_train_db(request):
    request_timesptamp = datetime.datetime.now()
    sql_statement = "SELECT AT.RECORD_ID as RECORD_ID,AT.* FROM ADULT_TRAIN AT WHERE 1=1"
    #empty request
    if not request.data:
        response_status=status.HTTP_400_BAD_REQUEST
        response_timestamp = datetime.datetime.now()
        mylogger.restlogger(request_timesptamp,request.path,request.data,response_timestamp,response_status)
        return Response(response_status)
    
    try:
        json_request_array = request.data
        for element in json_request_array:
            element_array = list(element.values())
            sql_statement+=' AND {} = "{}"'.format(str(element_array[0]), str(element_array[1]))
            adults = AdultTrain.objects.raw(sql_statement)
    except Exception as e:
        response_status=status.HTTP_500_INTERNAL_SERVER_ERROR
        response_timestamp = datetime.datetime.now()
        mylogger.exceptionlogger(e,response_timestamp)    
        return Response(response_status)
    
    #if succesful return data
    serializer = AdultSerializer(adults, many=True)
    if  adults:
        response_status=status.HTTP_200_OK
        response_timestamp = datetime.datetime.now()
        mylogger.restlogger(request_timesptamp,request.path,request.data,response_timestamp,response_status,serializer.data)
        return Response(serializer.data,response_status)
    #if result of query empty throw 204
    else:
        response_status=status.HTTP_204_NO_CONTENT
        response_timestamp = datetime.datetime.now()
        mylogger.restlogger(request_timesptamp,request.path,request.data,response_timestamp,response_status,serializer.data)
        return Response(response_status)
