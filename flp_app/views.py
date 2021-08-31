from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Post, Bookmark


# Create your views here.


#function based views


def index(request):
    return render(request, 'flp_app/index.html', {'title': 'Home'} )

def privacy_policy(request):
    return render(request, 'flp_app/privacy-policy.html', {'title': 'Privacy Policy'} )

def tos(request):
    return render(request, 'flp_app/tos.html', {'title': 'Terms of Service'} )


def disclaimer(request): 
    return render(request, 'flp_app/disclaimer.html', {'title': 'Disclaimer'})

def blog(request): 
    context = { 'posts': Post.objects.all()}
    return render(request, 'flp_app/blog.html', context)

def banking_category(request): 
    context = { 'posts': Post.objects.all()}
    return render(request, 'flp_app/banking-category.html', context)

def spendsave_category(request): 
    context = { 'posts': Post.objects.all()}
    return render(request, 'flp_app/spend-save-category.html', context)

def loans_category(request): 
    context = { 'posts': Post.objects.all()}
    return render(request, 'flp_app/cc-loans-category.html', context)

def investment_category(request): 
    context = { 'posts': Post.objects.all()}
    return render(request, 'flp_app/investment-retirement-category.html', context)

def tips_category(request): 
    context = { 'posts': Post.objects.all()}
    return render(request, 'flp_app/tips-category.html', context)




def FavoriteView(request,pk):
    post = Post.objects.get(id=pk)
    favorited = False
    if post.favorite.filter(id=request.user.id).exists():
        post.favorite.remove(request.user)
        messages.success(request, f'Removed favorite') #to display the success message
        favorited = False
    else:
     post.favorite.add(request.user) 
     favorited = True
     messages.success(request, f'Added to favorites') #to display the success message
    return HttpResponseRedirect(reverse('blog-detail', args=[str(pk)]))

@login_required
def bookmark(request, pk):
    user = request.user
    post = get_object_or_404(Post, id=pk)
    
    try: 
        b, created = Bookmark.objects.get_or_create(user=user)
        if b.posts.filter(id=pk).exists():
            b.posts.remove(post)
            messages.success(request, f'Removed favorite') #to display the success message
        else:
            b.posts.add(post)
            messages.success(request, f'Added to favorites') #to display the success message
        return HttpResponseRedirect(reverse('blog-detail', args=[str(pk)]))
    except Exception as e:
        raise e

@login_required
def BookmarkList(request):
    
    bookmark_list = Bookmark.objects.get(user=request.user)

    context = {
        'bookmark_list': bookmark_list,
    }

    return render(request, 'flp_app/bookmark-list.html', context)



#calculator views
def auto_payment_calculator(request): 
    return render(request, 'flp_app/auto-payment-calculator.html', {'title': 'Auto Payment Calculator'})
def mortgage_calculator(request): 
    return render(request, 'flp_app/mortgage-calculator.html', {'title': 'Mortgage Payment Calculator'})
def car_affordability_calculator(request): 
    return render(request, 'flp_app/car-affordability-calculator.html', {'title': 'Car Affordability Calculator'})
def home_affordability_calculator(request): 
    return render(request, 'flp_app/home-affordability-calculator.html', {'title': 'Home Affordability Calculator'})
def student_loan_calculator(request): 
    return render(request, 'flp_app/student-loan-calculator.html', {'title': 'Student Loan Calculator'})
#calculator landing page
def calculators(request): 
    return render(request, 'flp_app/calculators.html', {'title': 'Calculators'})

    
#ranking views
def bank_account_ranking(request): 
    return render(request, 'flp_app/bank-account-ranking.html', {'title': 'Bank Account Ranking'})
def car_insurance_ranking(request): 
    return render(request, 'flp_app/car-insurance.html', {'title': 'Car Insurance Ranking'})
def renters_insurance_ranking(request): 
    return render(request, 'flp_app/renters-insurance.html', {'title': 'Renters Insurance Ranking'})
def student_loans_ranking(request): 
    return render(request, 'flp_app/student-loans.html', {'title': 'Student Loans Ranking'})
def travel_card_ranking(request): 
    return render(request, 'flp_app/travel-cards.html', {'title': 'Best Travel Credit Cards'})
def student_card_ranking(request): 
    return render(request, 'flp_app/student-cards.html', {'title': 'Best Student Credit Cards'})
def rewards_card_ranking(request): 
    return render(request, 'flp_app/rewards-cards.html', {'title': 'Best Rewards Credit Cards'})
def badcredit_card_ranking(request): 
    return render(request, 'flp_app/badcredit-cards.html', {'title': 'Best Bad or No Credit Cards'})
#credit card compare landing page
def credit_card_rankings(request): 
    return render(request, 'flp_app/credit-card-ranking.html', {'title': 'Compare Credit Cards'})


#class based views

class PostListView(ListView):
    model = Post
    template_name = 'flp_app/blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'


#class BankingCategoryListView(ListView):
 #   model = Post
  #  template_name = 'flp_app/banking-category.html'

   # def get_queryset(self):
    #    return Post.objects.filter(category=self.kwargs.get('pk'))


