# Generated by Django 4.2 on 2023-06-13 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(),
        ),
    ]