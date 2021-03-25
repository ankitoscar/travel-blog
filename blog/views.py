from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def page_2(request):
    return render(request, 'blog/page-2.html')