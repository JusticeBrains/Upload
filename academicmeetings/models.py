from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _

class Meeting(models.Model):
    # class Status(models.IntegerChoices):
    #     SPECIAL = 1, 'Special'
    #     REGULAR = 2, 'Regular'
    
    class STATUS(models.TextChoices):
        SPECIAL = 'SPECIAL', _('Special')
        REGULAR = 'REGULAR', _('Regular')

    description = models.CharField(max_length=255, help_text='Meeting Description')
    document = models.FileField(upload_to='meetings/documents/s/%Y/%m/%d')
    publish = models.DateTimeField(_("Published Date"),blank=True, null=True, default=timezone.now)
    status = models.CharField(verbose_name='Status', choices=STATUS.choices, max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = _('Meeting')
        verbose_name_plural = _('Meetings')
        ordering = ['-publish',]

    def __str__(self):
        return self.description
