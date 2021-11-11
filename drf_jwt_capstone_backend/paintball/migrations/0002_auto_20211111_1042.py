# Generated by Django 3.2.8 on 2021-11-11 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paintball', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='name',
            field=models.CharField(default='Paintball Here', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]