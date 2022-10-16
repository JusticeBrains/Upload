from django.urls import path

from .views import signup, SignUpPageView

app_name = 'users'

urlpatterns = [
    path('signup/', signup, name='signup'),
    
]
