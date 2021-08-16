from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.


#function based views
def index(request):
    return render(request, 'flp_app/index.html', {'title': 'Home'} )

def disclaimer(request): 
    return render(request, 'flp_app/disclaimer.html', {'title': 'Disclaimer'})

def blog(request): 
    context = { 'posts': Post.objects.all()}
    
    return render(request, 'flp_app/blog.html', context)


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

    

#class based views

#class CommentListView(ListView):

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


    #model = Comment

#def comment_detail(request, slug):
 #   template_name = 'comments.html'
  #  post = get_object_or_404(Post, slug=slug)
   # comments = post.comments.filter(active=True)
    #new_comment = None
    # Comment posted
    #if request.method == 'POST':
     #   comment_form = CommentForm(data=request.POST)
      #  if comment_form.is_valid():

            # Create Comment object but don't save to database yet
       #     new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
        #    new_comment.post = post
            # Save the comment to the database
         #   new_comment.save()
    #else:
     #  comment_form = CommentForm()

    #return render(request, template_name, {'post': post,
     #                                      'comments': comments,
      #                                     'new_comment': new_comment,
       #                                   'comment_form': comment_form})