"""
This Django application manages sticky notes, allowing users to create, 
view, edit, and delete both posts and notes.

Modules:
    - `models.py`: Defines the database models for posts and notes.
    - `forms.py`: Contains forms for creating and editing posts and notes.
    - `views.py`: Implements views for handling HTTP requests and rendering 
                  templates.
    - `urls.py`: Defines URL patterns for routing requests to the appropriate
                 views.
    - `tests.py`: Contains unit tests for testing the application's 
                 functionality.
    - `admin.py`: Registers models with the Django admin site for easy 
                  management.

Models:
    - `Post`: Represents a post containing a title and content.
    - `Notes`: Represents a note associated with a post, containing a title, 
               content, and a foreign key to the post it belongs to.

Views:
    - `post_list`: Renders a list of all posts.
    - `post_details`: Displays details of a specific post, including
                      associated notes.
    - `post_new`: Allows users to create a new post.
    - `post_edit`: Allows users to edit an existing post.
    - `post_delete`: Allows users to delete a post.
    - `note_list`: Renders a list of notes associated with a specific post.
    - `note_detail`: Displays details of a specific note.
    - `note_new`: Allows users to create a new note associated with a post.
    - `note_edit`: Allows users to edit an existing note.
    - `note_delete`: Allows users to delete a note.

Tests:
    - Contains unit tests for testing the views and models.

Usage:
    1. Run `python manage.py makemigrations` to create migrations.
    2. Run `python manage.py migrate` to apply migrations and create database
            tables.
    3. Use Django admin or application views to interact with posts and notes.
    4. Run `python manage.py test` to execute unit tests and verify
            application functionality.
"""

from django.shortcuts import render, get_object_or_404, redirect
from .models import Notes, Post
from .forms import NoteForm, PostForm


# Note viewsw
# View function to display the list of notes.
def note_list(request, post_id):
    #  Retrieve all notes from the database.
    # notes = Notes.objects.all()
    post = get_object_or_404(Post, id=post_id)
    notes = Notes.objects.filter(post=post)
    context = {
        'post': post,
        'notes': notes,
        'page_title': f'Notes for {post.title}'
    }
    # Render the 'view_notes.html' template with retrived notes.
    return render(request, 'view_notes.html', context)


# View function to display the deatials of specific note.
def note_details(request, id):
    # Retrieve the note with the given ID from the database,
    # or return a 404 error if not found.
    note = get_object_or_404(Notes, id=id)
    post = note.post
    context = {
        'note': note,
        'page_title': f'Note {note.title}',
        'post_id': post.id,
        'post_title': post.title
    }
    # Render the 'note_details.html' template with retrieved note.
    return render(request, 'note_details.html', context)


# Function to create new note.
def note_new(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = NoteForm(request.POST)  # Bind form with POST data.
        if form.is_valid():
            note = form.save(commit=False)  # Create a new Note instance,
            note.post = post
            # but don't save yet.
            note.save()  # Save new Note instance to the database.
            return redirect('note_detail', id=note.id)  # Redirect to the
            # detail view of the new note.
    else:
        form = NoteForm()  # Create an empty form.
        # Render the form in the template.
    return render(request, 'note_edit.html',
                  {'form': form, 'heading': f'Add New Note to {post.title}',
                   'post_id': post.id})


# View function to edit note.
def note_edit(request, id):
    note = get_object_or_404(Notes, id=id)  # Retrieve the existing Note
    post = note.post  # Assuming  each note has a foriegn key to post.
    # instance.
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)  # Bind form with POST
        # data and existing Note instance.
        if form.is_valid():
            note = form.save(commit=False)  # Update the Note instance but
            # don't save it.
            note.save()  # Save the changes to the Note instance.
            return redirect('note_detail', id=note.id)
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_edit.html',
                  {'form': form, 'heading': 'Edit Note', 'post_id': post.id})


# View function to delete specific note.
def note_delete(request, id):
    # Retrieve the note with given ID from the database,
    # or return 404 erroe if not found.
    note = get_object_or_404(Notes, id=id)
    post_id = note.post.id  # Retrieve the post_id before deleting the note.
    # Delete the retrieved note from database.
    note.delete()
    # Redirect to the note list of specific post.
    return redirect('note_list', post_id=post_id)


# Post Views

def post_list(request):
    # Retrieve all Post objects from the database.
    posts = Post.objects.all()
    # Context dictionary to pass data to the template
    context = {
        'posts': posts,
        'page_title': 'List of Posts',
    }
    # Render the 'post_list.html' template with the context data.
    return render(request, 'post_list.html', context)


def post_details(request, id):
    # Retrieve a single Post object by its ID or return a 404 error if
    # not found.
    post = get_object_or_404(Post, id=id)
    notes = post.notes.all()
    # Context dictionary to pass data to the template.
    context = {
        'page_title': post.title,
        'post': post,
        'notes': notes
    }
    # Render the 'post_detail.html' template with the context data.
    return render(request, 'post_detail.html', context)


def post_new(request):
    if request.method == "POST":
        # Bind form with POST data.
        form = PostForm(request.POST)
        if form.is_valid():
            # Create a Post object but don't save to the database yet.
            post = form.save(commit=False)
            # Set the author if the user is authenticated.
            if request.user.is_authenticated:
                post.author = request.user
                # Save the Post object to the database.
                post.save()
            # Redirect to the detail view of the newly created post.
            return redirect('post_detail', id=post.id)
    else:
        # Create an empty form instance.
        form = PostForm()
    # Render the 'post_form.html' template with the form and heading context.
    return render(request, 'post_form.html',
                  {'form': form, 'heading': 'Add New Post'})


def post_edit(request, id):
    # Retrieve the existing Post object by its ID or return a 404 error
    # if not found.
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        # Bind form with POST data and the existing Post instance.
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            # Update the Post object but don't save to the database yet.
            post = form.save(commit=False)
            # Save the updated Post object to the database.
            post.save()
            # Redirect to the detail view of the updated post.
            return redirect('post_detail', id=post.id)
    else:
        # Create a form instance with the existing Post object.
        form = PostForm(instance=post)
    # Render the 'post_form.html' template with the form and heading context.
    return render(request, 'post_form.html',
                  {'form': form, 'heading': 'Edit Post'})


def post_delete(request, id):
    # Retrieve the existing Post object by its ID or return a 404 error
    # if not found.
    post = get_object_or_404(Post, id=id)
    # Delete the Post object from the database.
    post.delete()
    # Redirect to the list view of all posts.
    return redirect('post_list')
