# Generated by Django 3.2.19 on 2023-07-05 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvdm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('file', models.FileField(upload_to='uploads')),
            ],
        ),
        migrations.DeleteModel(
            name='index',
        ),
    ]
