# Generated by Django 4.2.4 on 2024-02-11 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0031_projectcategory_project_projecttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='SourceLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
