# Generated by Django 4.1.7 on 2023-02-27 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(max_length=250),
        ),
    ]
