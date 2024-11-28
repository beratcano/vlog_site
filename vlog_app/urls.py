from django.urls import path
from django.contrib.auth import views as auth_views
from .views import VlogPostCreateView,VlogPostDetailView,VlogPostUpdateView,VlogPostListView, register

urlpatterns = [
    path("", VlogPostListView.as_view(), name="vlog_list"),
    path("<int:pk>/", VlogPostDetailView.as_view(), name="vlog_detail"),
    path("new/", VlogPostCreateView.as_view(), name="vlog_create"),
    path('edit/<int:pk>/', VlogPostUpdateView.as_view(), name='vlog_edit'),
]