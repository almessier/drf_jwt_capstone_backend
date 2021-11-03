# Generated by Django 3.2.8 on 2021-11-03 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='middle_name',
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='123 E Pine Dr', max_length=250),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default=0, max_length=10),
        ),
    ]