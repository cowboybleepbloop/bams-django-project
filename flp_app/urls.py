from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('blog/', views.blog, name='blog'),
    path('calculators/', views.calculators, name='calculators'),
    path('auto-payment-calculator/', views.auto_payment_calculator, name='auto-payment-calculator'),
    path('mortgage-calculator/', views.mortgage_calculator, name='mortgage-calculator'),
    path('car-affordability-calculator/', views.car_affordability_calculator, name='car-affordability-calculator'),
    path('home-affordability-calculator/', views.home_affordability_calculator, name='home-affordability-calculator'),
    path('student-loan-calculator/', views.student_loan_calculator, name='student-loan-calculator'),
    #path('blog/', CommentListView.as_view, name='comments'),
    #path('<slug:slug>/', views.comment_detail, name='comment')
]
