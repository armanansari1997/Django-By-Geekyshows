# Generated by Django 4.0.6 on 2022-08-29 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='page_publish_date',
            new_name='post_publish_date',
        ),
    ]