# Generated by Django 4.0.4 on 2022-04-27 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_regular',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_special',
        ),
    ]
