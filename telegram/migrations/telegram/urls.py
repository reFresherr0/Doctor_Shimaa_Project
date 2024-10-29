from django.urls import path
from . import views




app_name = 'telegram_app'

urlpatterns = [
    # URL pattern with channel username and user ID as parameters
    path('messages/<str:channel_username>/', views.get_user_messages, name='get_user_messages'),
    path('get_articles/', view= views.get_articles.as_view(), name='get_articles'),
    path('get_articles_by_reviewer_id/<int:reviewer_id>', view= views.get_articles_by_reviewer_id.as_view(), name='get_articles_by_reviewer_id'),
    path('get_articles_detail/<int:id>/', view= views.get_articles_detail.as_view(), name='articles_detail'),
    path('get_categories/', view= views.get_categories.as_view(), name='get_categories'),
    path('get_categories_detail/<int:id>/', view= views.get_categories_detail.as_view(), name='categories_detail'),
    path('get_books/', view= views.get_books.as_view(), name='get_books'),
    path('get_books_detail/<int:id>/', view= views.get_books_detail.as_view(), name='books_detail'),
    path('articles_hitcount/<int:pk>/', view= views.ArticleCountHitDetailView.as_view(), name='articles_hitcount'),

]