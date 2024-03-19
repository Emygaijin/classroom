# Generated by Django 5.0.3 on 2024-03-19 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('serial', models.AutoField(primary_key=True, serialize=False)),
                ('tutor', models.CharField(max_length=233)),
                ('description', models.CharField(max_length=1098)),
                ('image', models.ImageField(upload_to='images/')),
                ('price', models.IntegerField()),
                ('caption1', models.CharField(blank=True, max_length=233, null=True)),
                ('video1', models.FileField(upload_to='media/')),
                ('caption2', models.CharField(blank=True, max_length=233, null=True)),
                ('video2', models.FileField(upload_to='media/')),
                ('caption3', models.CharField(blank=True, max_length=233, null=True)),
                ('video3', models.FileField(upload_to='media/')),
            ],
        ),
    ]
