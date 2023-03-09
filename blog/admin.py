from django.contrib import admin
from .models import Post

#관리자 페이지에서 보기위한 모델 등록
admin.site.register(Post)