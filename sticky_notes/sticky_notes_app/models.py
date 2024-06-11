from django.db import models


# Assuming you have a default post with ID=1
DEFAULT_POST_ID = 1


# Post Model
class Post(models.Model):
    # Title of the post
    title = models.CharField(max_length=200)
    # Content of the post
    content = models.TextField()
    # Date and time when the post was created (auto-generated)
    created_at = models.DateTimeField(auto_now_add=True)
    # Date and time when the post was last updated (auto-generated)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Notes Model
class Notes(models.Model):
    # Title of the note
    title = models.CharField(max_length=200)
    # Content of the note
    content = models.TextField()
    # Foreign key relationship with Post model, each note belongs to a post.
    post = models.ForeignKey(Post, related_name='notes',
                             on_delete=models.CASCADE)
    # Date and time when the note was created (auto-generated)
    created_at = models.DateTimeField(auto_now_add=True)
    # Date and time when the note was last updated (auto-generated)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
