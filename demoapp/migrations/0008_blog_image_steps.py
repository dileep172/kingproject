# Generated by Django 4.1.5 on 2023-02-26 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0007_blog_description_steps'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image_steps',
            field=models.ImageField(default='exit', upload_to='images/'),
            preserve_default=False,
        ),
    ]
