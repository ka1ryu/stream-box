from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.ranking, name='ranking'),
    
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]