# Generated by Django 4.2.1 on 2023-05-30 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_stufflink_thing_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_link', models.CharField(max_length=200)),
                ('contact_text', models.CharField(max_length=200)),
            ],
        ),
    ]
