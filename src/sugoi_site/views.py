from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.shortcuts import render
from django.http import HttpResponse
from streambox.models import Channel
from django.http import Http404


 
def index(request):
    # 変数定義
    level = ''
    page_num = request.GET.get('page')
    ranking_num = ''
    child_page = ''

    # ページネーション
    youtubers = Channel.objects.all()
    page_obj = paginate_query(request,youtubers, 25)

    
    # パンくず情報
    if page_num:
        try:
          ranking_num = int(page_num) * 25
          child_page = f'ゲーム実況者No.{ranking_num - 24} ~ No.{ranking_num}'
          level = 2
        except:
          raise Http404
    else:
        level = 1
    
    breadcrumb = {
      'current_page'  : child_page,
      'child_page'    : child_page,
      'level'         : level,
    } 
    return render(request, 'sugoi_site/index.html', {'page_obj': page_obj, 'breadcrumb': breadcrumb})

def about(request):
    breadcrumb = {
      'current_page'  : 'StreamBoxについて',
      'level'         : 2,
    } 
    return render(request, 'sugoi_site/about.html', {'breadcrumb': breadcrumb})


def paginate_query(request, queryset, count):
  paginator = Paginator(queryset, count)
  page = request.GET.get('page')

  try:
    page_obj = paginator.page(page)
  except PageNotAnInteger:
    page_obj = paginator.page(1)
  except EmptyPage:
    raise Http404
  return page_obj