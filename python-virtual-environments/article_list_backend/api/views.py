from urllib import response
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse # w/11
from .models import Article # w/11
from .serializers import ArticleSerializer # w/11
from rest_framework.parsers import JSONParser # w/11
from rest_framework.decorators import api_view # w/16
from rest_framework.response import Response # w/16
from rest_framework import status # w/16

# Create your views here.

def index(request):
    return HttpResponse('<pre>{"Articles backend status": "ok"}</pre>')


@api_view(['GET', 'POST']) #step-16 (and import) - creates browsable api
def article_list(request): #step-11 (and imports above)
    if request.method == 'GET':
        # get all articles - all() returns a copy of the query set, objects means class instances
        articles = Article.objects.all()
        # pass serializer the data to turn into python native data types. to serialize a query set, add many=True (https://www.django-rest-framework.org/api-guide/serializers/#dealing-with-multiple-objects)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        # pass serializer the data to turn into python native data types. data=request.data https://treyhunner.com/2018/04/keyword-arguments-in-python/
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # from "status" imported above - displays description with number
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#step-14, to see each article at http://localhost:8000/articles/<id>/

@api_view(['GET', 'PUT', 'DELETE'])
def article_details(request, primary_key):
    try:    # pk is key word, primary_key is argumument & path parameter in urls.py
        article = Article.objects.get(pk=primary_key)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete() # change later to move to a deleted articles table
        return Response(status=status.HTTP_204_NO_CONTENT)
