from django.urls import path
from .views import index, about,books 

app_name = 'home'
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('books/', books, name='books'),
]
