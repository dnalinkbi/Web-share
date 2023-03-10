from django import forms

from .models import Post

#PostFrom이라는 폼을 생성. 이 폼은 forms의 ModelForm이다.
class PostForm(forms.ModelForm):
    #폼을 만들기 위해서 사용된 model은 Post라고 알려주는 것
    class Meta:
        model = Post
        #author, created_date도 가능
        fields = ('title', 'text',)