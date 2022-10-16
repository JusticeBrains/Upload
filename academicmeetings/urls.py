from django.urls import path
from .views import meeting_list, upload_document

app_name = 'academic_meetings'

urlpatterns = [
    path('meeting/', meeting_list, name='meeting-list'),
    path('upload/',upload_document, name='upload'),
]
