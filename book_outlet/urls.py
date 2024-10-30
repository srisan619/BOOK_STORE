from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="book-index"),
    path("<slug:slug>", views.book_detail, name="book-detail")
]
