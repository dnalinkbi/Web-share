from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    #post/는 URL이 post 문자를 포함해야한다는 것을 의미
    #<int:pk>는 장고는 int값을 받아 pk라는 변수로 뷰를 전달
    #/는 다음에 /문자가 한번 더 와야한다.
    #예를들어, http://127.0.0.1:8000/post/5/ 인 경우, 장고는 post_detail 뷰를 찾아 매기변수 pk가 5인 값을 찾아 뷰로 전달
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #post_new 추가
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]