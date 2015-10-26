from django import forms
from guestbook.models import Comment

class CommentForm (forms.ModelForm):

  class Meta:
    model = Comment
