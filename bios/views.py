from django.shortcuts import render
from django.http import HttpResponse
from bios.models import Author

# Create your views here.
def index(request):
    authors = Author.objects.get_queryset()
    context = {}
    context['authors'] = authors
    response = render(request, "bios/index.html", context)
    return response

def individual(request):
    author = Author.objects.get_queryset().filter(request.POST['author'])
    context = {}
    context['author'] = author
    return render(request, 'bios/author.html', context)
