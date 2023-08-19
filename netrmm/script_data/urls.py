"""
URL configuration for netrmm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [ 
    
]
# urlpatterns = [
    
#     path("new_script",views.new_script,name="new_script"),
#     path("save_script",views.save_script,name="save_script"),
#     path("save_log",views.save_log,name="save_log"),
#     path("get_scriptnames",views.get_scriptnames,name="get_scriptnames"),
#     path("get_scriptbody/<int:id>",views.get_scriptbody,name="get_scriptbody"),
#     path("delete_script/<int:id>",views.delete_script,name="delete_script"),

#     path("test",views.test,name="test")

# ]
