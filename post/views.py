from django.shortcuts import render
from .models import Post
from newsletter.models import Signup
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def index(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()


    context={
        'object_list': featured,
        'latest' : latest
    }
    return render (request, 'index.html', context)

def blog(request):

    most_recent = Post.objects.order_by('-timestamp') [:3]
    post_list = Post.objects.all()
    paginator = Paginator(post_list,1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)




    context = {
        'most_recent': most_recent,
        'queryset' : paginated_queryset,
        'page_request_var' : page_request_var
    }

    return render(request, 'blog.html', context)

def post(request,id):
    return render (request, 'post.html', {})


