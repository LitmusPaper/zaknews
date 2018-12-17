# Generated by Django 2.0 on 2018-09-23 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Başlıq')),
                ('content', models.TextField(max_length=500, verbose_name='Yazı')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Tarix')),
            ],
            options={
                'verbose_name': 'Məqalə',
                'verbose_name_plural': 'Məqalələr',
            },
        ),
    ]
