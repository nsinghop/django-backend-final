from django.urls import path
from .views import FileListCreateView, FileDeleteView

urlpatterns = [
    path('files/', FileListCreateView.as_view(), name='file-list-create'),
    path('files/<int:pk>/', FileDeleteView.as_view(), name='file-delete'),
]