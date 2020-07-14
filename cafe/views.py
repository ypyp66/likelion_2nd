from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import editPost
from .form import CafePost

# Create your views here.
def blog(request):
    return render(request, 'blog.html')
    
def home(request):
    editpost = editPost.objects
    return render(request, 'home.html', {'editPost': editpost})

def newPost(request):
    # 1. 입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = CafePost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')  
    # 2. 빈 페이지를 띄워주는 기능 -> GET
    else:
        form = CafePost()
        return render(request, 'new.html',{'form': form })

def detail(request, post_id):
    post_detail = get_object_or_404(editPost, pk=post_id)
    return render(request, 'detail.html', {'detailpost': post_detail})
