from django.shortcuts import render

# Create your views here.

from guestbook.forms import CommentForm
from guestbook.models import Comment

def add_comment (request):
  '''Add a new comment.'''

  if request.method == 'POST':
    form = CommentForm (request.POST)

    if form.is_valid ():
      form.save (commit = True)
    else:
      print form.errors

  else:
    form = CommentForm ()

  context = { 'comments' : Comment.objects.all (), 'form' : form }

  return render (request, 'guestbook/add_comment.html', context)
