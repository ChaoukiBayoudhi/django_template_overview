from django.urls import path
from .views import home, about, contact, find, python_frameworks, django, flask, fastapi, search_results

# This section defines the URL patterns for the application.
# The urlpatterns list is a collection of URL patterns that Django will check against the URLs that are requested.
# Each pattern is a tuple that contains a regular expression, a view function, and a name for the URL pattern.
urlpatterns = [
    # This pattern matches the root URL ('') and maps it to the 'home' view function.
    # The 'name' parameter assigns a unique identifier to the URL pattern, allowing it 
    # to be referenced and constructed dynamically within templates and views.
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('find/', find, name='find'),
    path('search_results/', search_results, name='search_results'),
    path('python_frameworks/', python_frameworks, name='python_frameworks'),
    path('django/', django, name='django'),
    path('flask/', flask, name='flask'),
    path('fastapi/', fastapi, name='fastapi'),
]