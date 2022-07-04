# from urllib import response
# from django.shortcuts import render, HttpResponse
# from django.http import JsonResponse # w/11
from .models import Article # w/11
from .serializers import ArticleSerializer # w/11
# from rest_framework.parsers import JSONParser # w/11
# from rest_framework.decorators import api_view # w/16
from rest_framework.response import Response # w/16
from rest_framework import status, generics, mixins # status w/16, generics & mixins w/18
from rest_framework.decorators import APIView # w/17


# Create your views here.


class Index(APIView):
    def get(self, request):
        return Response({"Articles backend status": "ok"})

class ArticleList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # mixins.ListModelMixin
    def get(self, request):
        return self.list(request)

    # mixins.CreateModelMixin
    def post(self, request):
        return self.create(request)

class ArticleDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # mixins.RetrieveModelMixin 
    def get(self, request, id):
        return self.retrieve(request, id=id)

    # mixins.UpdateModelMixin 
    def put(self, request, id):
        return self.update(request, id=id)

    # mixins.DestroyModelMixin
    def delete(self, request, id):
        return self.destroy(request, id=id)



#  # Class based views, #step-17 (without mixins)
# class ArticleList(APIView): # parent class APIView creates browsable api
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True) # multiple articles
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ArticleDetails(APIView):
#     def get_object(self, id): # function to find the instance with the id passed to it by route parameter in urls.py
#         try:
#             return Article.objects.get(id=id) # need key word arguments here
#         except Article.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
    
#     def get(self, request, id):
#         article = self.get_object(id) # find instance
#         # serialize to turn (non-JSON, route param) queryset into python native data types: "serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON" https://www.django-rest-framework.org/api-guide/serializers/
#         serializer = ArticleSerializer(article)  # 1 article only here, no many=True
#         return Response(serializer.data)

#     def put(self, request, id):
#         article = self.get_object(id) # find instance
#         # pass the new data to article found, for update (overwrite)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         article = self.get_object(id) # find instance
#         article.delete() # change later to move to a deleted articles table
#         return Response(status=status.HTTP_204_NO_CONTENT) 


# Function based views:
    #step-1a
# def index(request):
#     return HttpResponse('<pre>{"Articles backend status": "ok"}</pre>')


# @api_view(['GET', 'POST']) #step-16 (and import) - creates browsable api
# def article_list(request): #step-11 (and imports above)
#     if request.method == 'GET':
#         # get all articles - all() returns a copy of the query set, objects means class instances
#         articles = Article.objects.all()
#         # pass serializer the data to turn into python native data types. to serialize a query set, add many=True (https://www.django-rest-framework.org/api-guide/serializers/#dealing-with-multiple-objects)
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method =='POST':
#         # pass serializer the data to turn into python native data types. data=request.data https://treyhunner.com/2018/04/keyword-arguments-in-python/
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED) # from "status" imported above - displays description with number
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# #step-14, to see each article at http://localhost:8000/articles/<id>/

# @api_view(['GET', 'PUT', 'DELETE'])
# def article_details(request, primary_key):
#     try:    # pk is key word, primary_key is argumument & path parameter in urls.py
#         article = Article.objects.get(pk=primary_key)
#     except Article.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#     elif request.method =='PUT':
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         article.delete() # change later to move to a deleted articles table
#         return Response(status=status.HTTP_204_NO_CONTENT)