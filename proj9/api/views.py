from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view()
# def hello_world(request):
#     return Response({"msg":"Hello World...."})

# @api_view(['GET'])
# def hello_world(request):
#     return Response({"msg":"Hello World...."})

@api_view(['GET','POST'])
def hello_world(request):
    if request.method == "GET":
        return Response({"msg":"This is GET Response..."})

    if request.method == "POST":
        print(request.data)
    return Response({"msg":"This is Post Request...","data":request.data})