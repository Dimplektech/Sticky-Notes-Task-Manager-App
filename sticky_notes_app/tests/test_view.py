from django.urls import reverse
from django.test import TestCase
from sticky_notes_app.models import Notes, Post


# PostsViewsTestCase


class PostsViews_Testcase(TestCase):
    def setUp(self):
        # Create a test Post object for use in the tests.
        self.post = Post.objects.create(title="Test Post",
                                        content="This is a test post.")

    def test_post_list_view(self):
        # Test the post list view.
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_list.html')

    def test_post_detail_view(self):
        # Test the post detail view.
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_create_view(self):
        # Test the post creation view.
        response = self.client.post(reverse('post_new'), {'title': 'New Post',
                                                    'content': 'New Content'})
        self.assertEqual(response.status_code, 302)  # Redirect after creation.
        # Check that the new post was created.
        new_post = Post.objects.get(title='New Post')
        self.assertEqual(new_post.content, 'New Content')

    def test_post_edit_view(self):
        # Test the post edit view.
        response = self.client.post(reverse('post_edit', args=[self.post.id]),
                                            {'title': 'Updated Post',
                                             'content': 'Updated Content'})
        self.assertEqual(response.status_code, 302)  # Redirect after update.
        # Check that the post was updated.
        updated_post = Post.objects.get(id=self.post.id)
        self.assertEqual(updated_post.title, 'Updated Post')
        self.assertEqual(updated_post.content, 'Updated Content')

    def test_post_delete_view(self):
        # Test the post delete view.
        response = self.client.post(reverse('post_delete', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after deletion.
        # Check that the post was deleted.
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())


# NotesViewsTestCase
class NotesViewsTestCase(TestCase):
    def setUp(self):
        # Create a test Post object and a test Note object for use in the
        # tests.
        self.post = Post.objects.create(title="Test Post",
                                        content="This is a test post.")
        self.note = Notes.objects.create(title="Test Note",
                                         content="This is a test note.",
                                         post=self.post)

    def test_note_list_view(self):
        # Test the note list view.
        response = self.client.get(reverse('note_list', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_notes.html')

    def test_note_detail_view(self):
        # Test the note detail view.
        response = self.client.get(reverse('note_detail', args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'note_details.html')

    def test_note_create_view(self):
        # Test the note creation view.
        response = self.client.post(reverse('note_new', args=[self.post.id]),
                                            {'title': 'New Note',
                                             'content': 'New content'})
        self.assertEqual(response.status_code, 302)  # Redirect after creation.
        # Check that the new note was created.
        new_note = Notes.objects.get(title='New Note')
        self.assertEqual(new_note.content, 'New content')
        # Ensure the note is linked to the correct post
        self.assertEqual(new_note.post, self.post)

    def test_note_edit_view(self):
        # Test the note edit view.
        response = self.client.post(reverse('note_edit', args=[self.note.id]),
                                    {'title': 'Updated Note',
                                     'content': 'Updated content'})
        self.assertEqual(response.status_code, 302)  # Redirect after update.
        # Check that the note was updated.
        updated_note = Notes.objects.get(id=self.note.id)
        self.assertEqual(updated_note.title, 'Updated Note')
        self.assertEqual(updated_note.content, 'Updated content')

    def test_note_delete_view(self):
        # Test the note delete view.
        response = self.client.post(reverse('note_delete', args=[self.note.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after deletion.
        # Check that the note was deleted.
        self.assertFalse(Notes.objects.filter(id=self.note.id).exists())


# Main entry point for running the tests
if __name__ == "__main__":
    TestCase.main()
