# Generated by Django 3.0.6 on 2020-05-17 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mnrelations', '0002_course_students'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]