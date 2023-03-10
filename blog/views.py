from django.shortcuts import render

# Create your views here.

#blog/post_list.html 템플릿 보여줌
def post_list(request):
    return render(request, 'blog/post_list.html', {})