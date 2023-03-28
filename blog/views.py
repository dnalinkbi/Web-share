from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
#여기서 PostForm은 blog/forms.py에 선언한 PostForm class
from .forms import PostForm
#새 블로그 글을 작성한 다음에 post_detail 페이지로 이동하기 위함
from django.shortcuts import redirect

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


def post_new(request):
    #글을 posting하는 요청이 들어오는 경우
    if request.method == "POST":
        #폼에서 받은 데이터 PostForm으로 넘겨주기
        form = PostForm(request.POST)
        #폼에 값이 올바로 들어있는지 확인
        if form.is_valid():
            #commit=False는 넘겨진 데이터를 Post 모델에 저장하지 말라는 의미.(다음 단계에서 작성자를 추가해야하기 때문)
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            #새로 작성한 이유 post_detail 창으로 이동
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    #수정하고자 하는 글의 Post 모델 instance를 가져옴
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

#파일 업로드
def upload(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = MyModelForm()
    return render(request, 'upload.html', {'form': form})