# Generated by Django 4.2 on 2023-06-13 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_projectlink_link_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infotext',
            name='text',
            field=models.TextField(),
        ),
    ]
