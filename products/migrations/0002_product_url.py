# Generated by Django 2.2 on 2020-08-15 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
