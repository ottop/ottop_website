# Generated by Django 4.2.4 on 2024-02-11 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_remove_experience_exptype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='category',
            new_name='exptype',
        ),
    ]
