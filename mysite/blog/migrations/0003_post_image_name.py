# Generated by Django 4.2.5 on 2023-10-08 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_image_name_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]