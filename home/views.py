from django.shortcuts import render

# Create your views here.
def index(request):
    print('{}: Request Home Page!'.format(request.get_host()))
    return render(request, 'index.html', {'body_title': 'Home Page'})
