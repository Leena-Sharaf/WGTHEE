# Generated by Django 2.2.11 on 2020-04-12 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200412_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='song_image',
            field=models.ImageField(default='images\\youtube1.png', upload_to='images'),
        ),
    ]
