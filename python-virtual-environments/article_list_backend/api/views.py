from urllib import response
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse # w/11
from .models import Article # w/11
from .serializers import ArticleSerializer # w/11
from rest_framework.parsers import JSONParser # w/11
# from django.views.decorators.csrf import csrf_exempt # w/13, removed w/16
from rest_framework.decorators import api_view # w/16
from rest_framework.response import Response # w/16
from rest_framework import status # w/16

# Create your views here.

def index(request):
    return HttpResponse('<pre>{"Articles backend status": "ok"}</pre>')


# commented out @step-16
# @csrf_exempt #step-13 (and import above)... temporary solution to post with out Cross-Site Request Forgery Token https://www.django-rest-framework.org/tutorial/1-serialization/#writing-regular-django-views-using-our-serializer

@api_view(['GET', 'POST']) #step-16 (and import) - creates browsable api
def article_list(request): #step-11 (and imports above)
    if request.method == 'GET':
        # get all articles - all() returns a copy of the query set, objects means class instances
        articles = Article.objects.all()
        # pass serializer the data to turn into python native data types. to serialize a query set, add many=True (https://www.django-rest-framework.org/api-guide/serializers/#dealing-with-multiple-objects)
        serializer = ArticleSerializer(articles, many=True)
        # create a JSON-encoded response.
        # return JsonResponse(serializer.data, safe=False) # commented out @step-16
        # The safe boolean parameter defaults to True. If it’s set to False, any object can be passed for serialization (otherwise only dict instances are allowed). If safe is True and a non-dict object is passed as the first argument, a TypeError will be raised. https://docs.djangoproject.com/en/4.0/ref/request-response/#jsonresponse-objects
        return Response(serializer.data)

    elif request.method =='POST':
        # parse request into python
        # data = JSONParser().parse(request) # commented out @step-16
        # data=data is a key word argument: https://treyhunner.com/2018/04/keyword-arguments-in-python/
        # serializer = ArticleSerializer(data=data) # commented out @step-16
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return JsonResponse(serializer.data, status=201) # commented out @step-16
            # 201 means request has succeeded and has led to the creation of a resource. why isn't he returning the whole list of articles here?
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # return JsonResponse(serializer.errors, status=400) # commented out @step-16


#step-14, to see each article at http://localhost:8000/articles/<id>/
# @csrf_exempt # commented out @step-16
@api_view(['GET', 'PUT', 'DELETE'])
def article_details(request, primary_key):
    try:    # pk is key word, primary_key is argumument & path parameter in urls.py
        article = Article.objects.get(pk=primary_key)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        # return HttpResponse(status=404) # commented out @step-16

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        # return JsonResponse(serializer.data) # commented out @step-16
        return Response(serializer.data)
    elif request.method =='PUT':
         # parse request into python
        # data = JSONParser().parse(request) # commented out @step-16
        # serializer = ArticleSerializer(article, data=data) # commented out @step-16
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return JsonResponse(serializer.data, status=201) # commented out @step-16
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # return JsonResponse(serializer.errors, status=400) # commented out @step-16
    elif request.method == 'DELETE':
        article.delete() # change later to move to a deleted articles table
        return Response(status=status.HTTP_204_NO_CONTENT)
        # return HttpResponse(status=204) # 204 means no content. # commented out @step-16

# @step-12 comment this out
# def Index(request): #step-1
#     return HttpResponse("Index displays here.") # and import HttpResponse above
