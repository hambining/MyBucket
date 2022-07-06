from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post

# Create your views here.
def home(request):
    return render(request, 'index.html')

def postlist(request):
    posts = Post.objects.filter().order_by('date')
    return render(request, 'post.html', {'posts':posts})

def postcreate(request):
    # request method가 POST인 경우 -> 입력값 저장
    if request.method == 'POST' or request.method == 'FILES':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('postlist')
    # request method가 GET인 경우 -> form 입력 html 띄우기
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form':form})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(request, 'postdetail.html', {'post_detail':post_detail}, {'comment_form':comment_form})
