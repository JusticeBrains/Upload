# Generated by Django 4.0.4 on 2022-04-27 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academicmeetings', '0007_remove_meeting_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='status',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Special'), (2, 'Regular')], null=True),
        ),
    ]
