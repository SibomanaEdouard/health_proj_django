# Generated by Django 5.1.1 on 2024-11-16 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='patient',
        ),
    ]