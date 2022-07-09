"""article_list_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# add include to imports above ^


urlpatterns = [ 
    path('admin/', admin.site.urls),
    #step-2b
    # display views - blank path for landing page, then include with other location of urlpatterns
    path('', include('api.urls')),
]


# FIRST WAY TO DISPLAY VIEWS, WITHOUT URLS.PY IN THE APP IT'S COMING FROM
# from django.contrib import admin
# from django.urls import path

# # import views
# from api.views import Index

# urlpatterns = [
#     path('admin/', admin.site.urls),

    #step-1b
#     # display views - blank path for landing page then name of imported file
#     path('', Index)
# ]
