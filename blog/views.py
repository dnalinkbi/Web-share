from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

#blog/post_list.html 템플릿 보여줌
def post_list(request):
    #posts라는 쿼리셋 생성.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})