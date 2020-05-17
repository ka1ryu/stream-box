from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse
from .models import Channel


# Create your views here.
def ranking(request):
    # 変数定義
    level = ''
    page_num = request.GET.get('page')
    ranking_num = ''
    child_page = ''

    # ページネーション
    youtubers = Channel.objects.order_by('-total_view')[:100]
    page_obj = paginate_query(request,youtubers, 25)
    
    # パンくず情報
    if page_num:
        ranking_num = int(page_num) * 25
        child_page = f'{ranking_num - 24}位 ~ {ranking_num}位'
        level = 3
    else:
        level = 2
    
    breadcrumb = {
      'current_page'  : 'おすすめのゲーム実況者ランキング',
      'child_page'    : child_page,
      'level'         : level,
    } 
    return render(request, 'streambox/ranking.html', {'page_obj': page_obj, 'breadcrumb': breadcrumb})


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
    page_obj = paginator.page(paginator.num_pages)
  return page_obj