# Generated by Django 4.2.11 on 2024-04-28 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_app', '0003_alter_customuser_active_account'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TutorRequest',
            new_name='StudentRequest',
        ),
    ]
