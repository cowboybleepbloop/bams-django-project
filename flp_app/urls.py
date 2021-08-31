from django.urls import path, include
from .views import BookmarkList, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.contrib.admin.views.decorators import staff_member_required
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('terms-of-service/', views.tos, name='tos'),
    path('blog/', PostListView.as_view(), name='blog'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    
    path('blog/new/', staff_member_required(PostCreateView.as_view()), name='blog-create'),
    path('blog/<int:pk>/update/', staff_member_required(PostUpdateView.as_view()), name='blog-update'),
    path('blog/<int:pk>/delete/', staff_member_required(PostDeleteView.as_view()), name='blog-delete'),
    # ^^^ only staff accounts can delete, create and update posts, this could already be done on the backend but this is another option
    path('favorite/<int:pk>', views.FavoriteView, name='favorite_post'),
    path('bookmarks/', views.BookmarkList, name='bookmarks'),
    path('blog/<int:pk>/bookmark/', views.bookmark, name='postbookmark'),
    #blog categories
    path('blog/banking/', views.banking_category, name='banking-posts'),
    path('blog/spending_and_savings/', views.spendsave_category, name='spendsave-posts'),
    path('blog/creditcards_and_loans/', views.loans_category, name='loans-posts'),
    path('blog/investment_and_retirement/', views.investment_category, name='investment-posts'),
    path('blog/tips_and_advice/', views.tips_category, name='tips-posts'),

    ####
    path('calculators/', views.calculators, name='calculators'),
    path('auto-payment-calculator/', views.auto_payment_calculator, name='auto-payment-calculator'),
    path('mortgage-calculator/', views.mortgage_calculator, name='mortgage-calculator'),
    path('car-affordability-calculator/', views.car_affordability_calculator, name='car-affordability-calculator'),
    path('home-affordability-calculator/', views.home_affordability_calculator, name='home-affordability-calculator'),
    path('student-loan-calculator/', views.student_loan_calculator, name='student-loan-calculator'),
    path('travel-cards/', views.travel_card_ranking, name='travel-cards'),
    path('student-cards/', views.student_card_ranking, name='student-cards'),
    path('rewards-cards/', views.rewards_card_ranking, name='rewards-cards'),
    path('badcredit-cards/', views.badcredit_card_ranking, name='badcredit-cards'),
    path('credit-card-ranking/', views.credit_card_rankings, name='credit-cards-ranking'),
    path('car-insurance/', views.car_insurance_ranking, name='car-insurance'),
    path('renters-insurance/', views.renters_insurance_ranking, name='renters-insurance'),
    path('student-loans/', views.student_loans_ranking, name='student-loans'),
    path('bank-accounts/', views.bank_account_ranking, name='bank-accounts'),
]
 