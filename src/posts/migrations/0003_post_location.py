# Generated by Django 3.1.4 on 2020-12-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.TextField(default='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d424146.1026392451!2d150.65179666970943!3d-33.847356724710885!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b129838f39a743f%3A0x3017d681632a850!2sSydney%20NSW!5e0!3m2!1sen!2sau!4v1607782680258!5m2!1sen!2sau'),
        ),
    ]
