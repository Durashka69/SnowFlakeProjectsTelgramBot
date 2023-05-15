from django.urls import path

from apps.projects.views import (
    ProjectListCreateAPIView,
    ProjectRetrieveUpdateDestroyAPIView,
    AppealListCreateAPIView,
    AppealRetrieveUpdateDestroyAPIView,
)

app_name = 'attendance'

urlpatterns = [
    path('projects/', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project-retrieve-update-destroy'),
    path('appeals/', AppealListCreateAPIView.as_view(), name='appeal-list-create'),
    path('appeals/<int:pk>/', AppealRetrieveUpdateDestroyAPIView.as_view(), name='appeal-retrieve-update-destroy'),
]
