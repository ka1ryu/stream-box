from django.shortcuts import render
 
def index(request):
    return render(request, 'sugoi_site/index.html', {})

def about(request):
    return render(request, 'sugoi_site/about.html', {})