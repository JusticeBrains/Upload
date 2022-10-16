from django.forms import ModelForm
from .models import Meeting

class MeetingModelForm(ModelForm):
    class Meta:
        model = Meeting
        fields = ['description', 'document',]