from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse
from .models import Channel


# Create your views here.
def index(request):
    youtubers = Channel.objects.order_by('-total_view')[:100]
    context = {
      'list': youtubers
    }
    page_obj = paginate_query(request,youtubers, 25)   # ページネーション
    return render(request, 'streambox/index.html', {'page_obj': page_obj})


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def paginate_query(request, queryset, count):
  paginator = Paginator(queryset, count)
  page = request.GET.get('page')
  try:
    page_obj = paginator.page(page)
  except PageNotAnInteger:
    page_obj = paginator.page(1)
  except EmptyPage:
    page_obj = paginatot.page(paginator.num_pages)
  return page_obj