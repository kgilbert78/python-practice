#step-8
from rest_framework import serializers
from .models import Article

# #step-9 - less repetitive way
# https://www.django-rest-framework.org/tutorial/1-serialization/#using-modelserializers
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'description', 'link']
        # # then go to terminal at project level, run python manage.py shell, and run the step-10 (second way) stuff at the bottom of this page

# #step-9 (first way) https://www.django-rest-framework.org/api-guide/serializers/
# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     description = serializers.CharField() # no TextField in serializer class.
#     link = serializers.CharField() # no TextField in serializer class.

#     def create(self, validated_data):
#         return Article.objects.create(validated_data)
#         # # then go to terminal at project level, run python manage.py shell, and run the step-10 (first way) stuff at the bottom of this page

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('title', instance.description)




#step-10 (first way)
    # from api.models import Article
    # from api.serializers import ArticleSerializer
    # from rest_framework.renderers import JSONRenderer
    # from rest_framework.parsers import JSONParser

    # # create new article & save it:
    # a = Article(title = "serializer class", description = "Django Rest Framework Docs", link = "https://www.django-rest-framework.org/tutorial/1-serialization/")
    # a.save()

    # # "serialize" data (turn into python native data types - ie. dict)
    # serializer = ArticleSerializer(a)

    # # view data with:
    # serializer.data

    # # convert data to json and view it:
    # json = JSONRenderer().render(serializer.data)
    # json

    # # convert json back to python (dict of validated data) and check validation:
                # # https://docs.python.org/3/library/io.html, https://www.django-rest-framework.org/api-guide/serializers/#deserializing-objects
    # import io
    # stream = io.BytesIO(json)
    # data = JSONParser().parse(stream)
    # serializer = ArticleSerializer(data=data)
    # serializer.is_valid()
    # serializer.validated_data


# step-10 (second way)
#     from api.models import Article
#     from api.serializers import ArticleSerializer
    
#     serializer = ArticleSerializer()

#     # print a representation of the serializer
#     print(repr(serializer))