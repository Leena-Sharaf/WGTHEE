# Generated by Django 3.1.1 on 2020-11-20 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20201119_2000'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CommentModel',
        ),
    ]
