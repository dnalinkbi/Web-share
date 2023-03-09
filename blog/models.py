from django.conf import settings
from django.db import models
from django.utils import timezone

#Post는 모델의 이름. models는 Post가 장고 모델임을 의미한다. Post를 데이터베이스에 저장해야한다
class Post(models.Model):
    #models.ForeignKey : 다른 모델의 링크
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #models.CharField : 글자수가 제한된 텍스트 정의할때
    title = models.CharField(max_length=200)
    #models.TextField : 글자수 제한이 없는 긴 텍스트(보통 블로그 본문)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title