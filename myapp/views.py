from django.shortcuts import render

def home(request):
    context={
        'user_name' : 'Chaouki',
        'items' :['Django', 'FastAPI', 'Flask'], 
        }
    return render(request, 'myapp/home.html', context)

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def find(request):
    return render(request, 'myapp/find.html')

def search_results(request):
    query = request.GET.get('query', '')
    # Implement your search logic here
    context = {
        'query': query,
        # 'results': results,  # Add search results to the context
    }
    return render(request, 'myapp/search_results.html', context)

def python_frameworks(request):
    return render(request, 'myapp/python_frameworks.html')

def django(request):
    return render(request, 'myapp/django.html')

def flask(request):
    return render(request, 'myapp/flask.html')

def fastapi(request):
    return render(request, 'myapp/fastapi.html')