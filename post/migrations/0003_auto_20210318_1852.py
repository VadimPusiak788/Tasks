# Generated by Django 3.1.7 on 2021-03-18 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post_coment',
            new_name='post_comment',
        ),
    ]