from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes, name='routes'),
    path('home/', views.get_all_cards_by_last_study, name='home-all-cards'),
    path('home/update/<str:days>/', views.update_day, name='home-all-cards'),
    path('vocabcards/', views.get_all_vocabcards, name='all-vocabcards'),
    path('studycards/', views.get_all_studycards, name='all-study-cards'),
    path('vocabcards/create/', views.create_vocabCard, name='create-new-card'),
    path('vocabcard/<str:primary_key>/edit/', views.edit_vocab_card, name='edit-vocabcard'),
    path('vocabcard/<str:primary_key>/delete/', views.delete_vocab_card, name='delete-vocabcard'),
    path('vocabcard/<str:primary_key>/', views.get_vocabcard, name='view-vocabcard'),
    path('definition/<str:primary_key>/', views.get_definition, name='get-jisho-definition'),
]