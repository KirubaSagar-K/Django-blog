from django.urls import path
from . import views
from .views import postlist, postdetail, postcreate, postupdate, postdelete


urlpatterns = [
    path('', postlist.as_view(), name='blog-home'),
    path('post/<int:pk>/', postdetail.as_view(), name='post-detail'),
    path('post/new/', postcreate.as_view(), name='post-create'),
    path('post/<int:pk>/update', postupdate.as_view(), name='post-update'),
    path('post/<int:pk>/delete', postdelete.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about')
]