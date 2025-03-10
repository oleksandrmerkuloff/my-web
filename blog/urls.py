from django.urls import path

from .views import index, blog_view, post_view, contacts_view


urlpatterns = [
    path('', index, name='home'),
    path('blog/', blog_view, name='my-blog'),
    path('blog/<int:post_pk>/', post_view, name='post-view'),
    path('contacts/', contacts_view, name='my-contacts'),
]
