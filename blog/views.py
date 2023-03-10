from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.

#blog/post_list.html 템플릿 보여줌
def post_list(request):
    #posts라는 쿼리셋 생성하여 Post 정렬된 데이터를 저장.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

#만약 pk에 해당하는 post가 없으면 에러메시지를 그냥 출력하는 것이아니라 page not found 창을 출력하도록
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})