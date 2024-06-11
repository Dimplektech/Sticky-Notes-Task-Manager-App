
from django.urls import path
from .import views

urlpatterns = [
 
    # Post URLs

    path('', views.post_list, name='post_list'),
    path('posts/<int:id>/', views.post_details, name='post_detail'),
    path('posts/new/', views.post_new, name='post_new'),
    path('posts/<int:id>/edit/', views.post_edit, name='post_edit'),
    path('posts/<int:id>/delete/', views.post_delete, name='post_delete'),

    # Notes URLs
    path('notes/<int:post_id>/', views.note_list, name='note_list'),
    path('note/<int:id>/', views.note_details, name='note_detail'),
    path('note/new/<int:post_id>/', views.note_new, name='note_new'),
    path('note/,<int:id>/edit/', views.note_edit, name='note_edit'),
    path('note/<int:id>/delete/', views.note_delete, name='note_delete'),


]
