# Generated by Django 4.1.5 on 2023-01-12 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='video',
            field=models.FileField(default=False, upload_to='media/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='auther',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
