from django.urls import path

from .views import CreatePostView

urlpatterns = [
    path("new/", CreatePostView.as_view(), name="new_post")
]
