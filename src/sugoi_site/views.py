from django.shortcuts import render
 
def index(request):
    return render(request, 'sugoi_site/index.html')

def about(request):
    breadcrumb = {
      'current_page'  : 'StreamBoxについて',
      'level'         : 2,
    } 
    return render(request, 'sugoi_site/about.html', {'breadcrumb': breadcrumb})