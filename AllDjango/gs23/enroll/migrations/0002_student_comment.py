# Generated by Django 4.0.6 on 2022-08-15 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='comment',
            field=models.CharField(default='Not Available', max_length=40),
        ),
    ]
