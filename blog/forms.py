from django import forms
from .models import Post, Comment

class PostForm1(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

    def save(self, commit=True):
        post = Post(title= self.cleaned_data['title'], content=self.cleaned_data['content'])
        if commit:
            post.save()
        return post


class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =['title', 'content', 'image']