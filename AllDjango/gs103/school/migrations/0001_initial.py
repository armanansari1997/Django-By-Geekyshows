# Generated by Django 4.0.6 on 2022-08-28 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExamCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('examcenter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='school.examcenter')),
                ('name', models.CharField(max_length=70)),
                ('roll', models.IntegerField()),
            ],
            bases=('school.examcenter',),
        ),
    ]