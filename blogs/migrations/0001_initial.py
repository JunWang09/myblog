# Generated by Django 2.1.1 on 2018-11-18 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=258)),
                ('publish_date', models.DateField()),
                ('owner', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('summary', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
