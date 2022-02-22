from urllib import response
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse # w/11
from .models import Article # w/11
from .serializers import ArticleSerializer # w/11
from rest_framework.parsers import JSONParser # w/11
from django.views.decorators.csrf import csrf_exempt # w/13

# Create your views here.

@csrf_exempt #step-13 (and import above)... temporary solution to post with out Cross-Site Request Forgery Token https://www.django-rest-framework.org/tutorial/1-serialization/#writing-regular-django-views-using-our-serializer
def article_list(request): #step-11 (and imports above)
    if request.method == 'GET':
        # get all articles - all() returns a copy of the query set, objects means class instances
        articles = Article.objects.all()
        # pass serializer the data to turn into python native data types. to serialize a query set, add many=True (https://www.django-rest-framework.org/api-guide/serializers/#dealing-with-multiple-objects)
        serializer = ArticleSerializer(articles, many=True)
        # create a JSON-encoded response.
        return JsonResponse(serializer.data, safe=False)
        # The safe boolean parameter defaults to True. If it’s set to False, any object can be passed for serialization (otherwise only dict instances are allowed). If safe is True and a non-dict object is passed as the first argument, a TypeError will be raised. https://docs.djangoproject.com/en/4.0/ref/request-response/#jsonresponse-objects

    elif request.method =='POST':
        # parse request into python
        data = JSONParser().parse(request)

        serializer = ArticleSerializer(data=data) 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
            # 201 means request has succeeded and has led to the creation of a resource. why isn't he returning the whole list of articles here?
        else:
            return JsonResponse(serializer.errors, status=400)


#step-14, to see each article at http://localhost:8000/articles/<id>/
@csrf_exempt
def article_details(request, pk): # primary key
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)
    elif request.method =='PUT':
         # parse request into python
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data) 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        article.delete() # change later to move to a deleted articles table
        return HttpResponse(status=204) # 204 means no content.

# @step-12 comment this out
# def Index(request): #step-1
#     return HttpResponse("Index displays here.") # and import HttpResponse above
