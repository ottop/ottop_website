# Generated by Django 4.2.4 on 2024-02-11 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_rename_category_experience_exptype'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='sort_id',
            field=models.CharField(default=0, max_length=3),
            preserve_default=False,
        ),
    ]
