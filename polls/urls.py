from django.conf.urls import url 
from . import views

app_name = 'polls' 
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^<int:pk>/',views.DetailView.as_view(),name='detail'),
    url(r'^<int:pk>/results/', views.ResultsView.as_view(),name='results'),  
    url(r'^<int:question_id>/vote/',views.vote,name='vote'),

]
