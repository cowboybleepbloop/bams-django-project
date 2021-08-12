from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('blog/', views.blog, name='blog'),
    #path('blog/', CommentListView.as_view, name='comments'),
    #path('<slug:slug>/', views.comment_detail, name='comment')
]
