from django.urls import path
# from .views import Index      # @step-12 comment this out
# from .views import index, article_list, article_details # @step-17 commented out
from .views import ArticleList, Index, ArticleDetails

#step-17 - for class based views
urlpatterns = [
    path('', Index.as_view()),
    path('articles/', ArticleList.as_view()),
    path('articles/<int:id>/', ArticleDetails.as_view()),
]


# # For function based views, commented out @step-17
# #step-12 - after this visit http://localhost:8000/articles/ in the browser to see the data, and test get request with postman or insomnia. post will receive an error - see step 13 in views
# urlpatterns = [
#     path('', index),
#     path('articles/', article_list), # 12
#     path('articles/<int:primary_key>/', article_details), #step-15 (and import above)
# ]

# @step-12 comment this out
# #step-2a (creation of this file and url patterns below)
# urlpatterns = [
#     path('', Index),
# ]