# Generated by Django 4.1.5 on 2023-07-28 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythonshop', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='product', to='pythonshop.category'),
        ),
    ]
