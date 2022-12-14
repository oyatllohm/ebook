# Generated by Django 4.0.5 on 2022-10-08 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('desc', models.TextField(blank=True, verbose_name='Category xaqida')),
                ('image', models.ImageField(blank=True, upload_to='Category_photo', verbose_name='Category rasmi')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('desc', models.TextField(blank=True, verbose_name='kitob xaqida')),
                ('image', models.ImageField(blank=True, upload_to='kitob_photo', verbose_name='kitob rasmi')),
                ('file', models.FileField(upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.category')),
            ],
        ),
    ]
