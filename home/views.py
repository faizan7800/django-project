from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def contact(request):
    return HttpResponse("This is Contact page")