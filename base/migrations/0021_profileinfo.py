# Generated by Django 4.2.1 on 2023-05-30 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_alter_experience_exptype'),
    ]

    operations = [
        migrations.AddField(
            model_name = "profileinfo",
            name = 'image',
            field = models.ImageField(null=True,blank=True)
        ),
    ]
