# Generated by Django 4.2.4 on 2024-02-11 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_experiencecategory_sort_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencecategory',
            name='sort_id',
            field=models.CharField(default=0, max_length=3),
            preserve_default=False,
        ),
    ]