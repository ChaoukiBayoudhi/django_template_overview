"""
URL configuration for django_template_overview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path

# This section defines the URL patterns for the django_template_overview project.
# The urlpatterns list is a collection of URL patterns that Django will check against the URLs that are requested.
# Each pattern is a tuple that contains a regular expression, a view function, and a name for the URL pattern.
urlpatterns = [
    # This pattern matches the URL '/admin/' and maps it to the admin site URLs.
    # The admin site is a built-in Django application that provides a web-based interface for managing models, users, and permissions.
    path("admin/", admin.site.urls),
    # This pattern matches the root URL ('') and includes the URL patterns from the 'myapp' application.
    # The 'include' function is used to include URL patterns from another URL configuration module.
    # This allows for modularization of URL configurations and makes it easier to manage complex URL structures.
    path('', include('myapp.urls')),
]
