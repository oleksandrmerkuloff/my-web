from django.urls import path

from .views import index, blog_view, post_view, contacts_view


urlpatterns = [
    path('', index, name='home'),
    path('blog/', blog_view, name='my-blog'),
    path('blog/by-tag/<str:tag>/', blog_view, name='filtered-blog'),
    path('blog/<slug:post_slug>/', post_view, name='post-view'),
    path('contacts/', contacts_view, name='my-contacts'),
]
