# Generated by Django 4.2.1 on 2023-05-30 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_projectlink_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='StuffLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thing_link', models.CharField(max_length=200)),
            ],
        ),
    ]
