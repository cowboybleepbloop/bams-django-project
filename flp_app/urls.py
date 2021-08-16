from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.contrib.admin.views.decorators import staff_member_required
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('blog/', PostListView.as_view(), name='blog'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('blog/new/', staff_member_required(PostCreateView.as_view()), name='blog-create'),
    path('blog/<int:pk>/update/', staff_member_required(PostUpdateView.as_view()), name='blog-update'),
    path('blog/<int:pk>/delete/', staff_member_required(PostDeleteView.as_view()), name='blog-delete'),
    # ^^^ only staff accounts can delete, create and update posts, this could already be done on the backend but this is another option
    path('calculators/', views.calculators, name='calculators'),
    path('auto-payment-calculator/', views.auto_payment_calculator, name='auto-payment-calculator'),
    path('mortgage-calculator/', views.mortgage_calculator, name='mortgage-calculator'),
    path('car-affordability-calculator/', views.car_affordability_calculator, name='car-affordability-calculator'),
    path('home-affordability-calculator/', views.home_affordability_calculator, name='home-affordability-calculator'),
    path('student-loan-calculator/', views.student_loan_calculator, name='student-loan-calculator'),
    #path('blog/', CommentListView.as_view, name='comments'),
    #path('<slug:slug>/', views.comment_detail, name='comment')
]
