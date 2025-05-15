from django.urls import path

from blog.views.post_view import home_hello, PostDetail


urlpatterns = [
    path('', home_hello, name='home'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
