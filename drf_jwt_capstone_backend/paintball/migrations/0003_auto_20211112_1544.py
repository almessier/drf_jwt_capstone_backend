# Generated by Django 3.2.8 on 2021-11-12 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paintball', '0002_auto_20211111_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='price_id',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='product_id',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
