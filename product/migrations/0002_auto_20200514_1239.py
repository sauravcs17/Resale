# Generated by Django 2.2.1 on 2020-05-14 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='products/'),
        ),
    ]
