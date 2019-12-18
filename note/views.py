from django.shortcuts import render

# Create your views here.

def index(request):
    print('{}: Request Note Page!'.format(request.get_host()))
    return render(request, 'note.html', {'head_title': 'Sthtodo Note', 'body_title': 'Note Page'})
