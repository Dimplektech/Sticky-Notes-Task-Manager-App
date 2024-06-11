from django.test import TestCase
from sticky_notes_app.models import Notes, Post


class NotesModelTestCase(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Test Post",
                                        content="This is a test post.")
        self.note = Notes.objects.create(title="Test Note",
                                         content="This is a test note.",
                                         post=self.post)

    def test_note_content(self):
        note = Notes.objects.get(title="Test Note")
        self.assertEqual(note.content, "This is a test note.")
        # Ensure the note is linked to the correct post
        self.assertEqual(note.post, self.post)


class PostModelTestCase(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Test Post",
                                        content="This is a test post.")
        self.note = Notes.objects.create(title="Test Note",
                                         content="This is a test note.",
                                         post=self.post)

    def test_post_content(self):
        post = Post.objects.get(title="Test Post")
        self.assertEqual(post.content, "This is a test post.")
        # Ensure the post has the correct number of notes
        self.assertEqual(post.notes.count(), 1)
        self.assertEqual(post.notes.first(), self.note)
