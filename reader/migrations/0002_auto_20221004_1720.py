# Generated by Django 3.2.8 on 2022-10-04 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='phone',
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.CharField(blank=True, max_length=15, verbose_name='Kursi'),
        ),
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.CharField(blank=True, max_length=255, verbose_name='Group'),
        ),
    ]
