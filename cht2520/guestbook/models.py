from django.db import models

# Create your models here.

class Comment (models.Model):
  '''A comment in the guestbook.'''

  comment_left = models.CharField (max_length = 134, blank = False)

  def __unicode__ (self):
    return self.comment_left
