# Generated by Django 2.2.1 on 2020-05-26 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('desc', models.CharField(blank=True, max_length=2000)),
                ('image', models.ImageField(blank=True, default='auction_images/default/default.svg', upload_to='auction_images/')),
                ('contact', models.CharField(max_length=300, null=True)),
                ('min_value', models.IntegerField()),
                ('date_added', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('final_value', models.IntegerField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=models.SET('(deleted)'), related_name='auction_winner', related_query_name='auction_winner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('phone', models.CharField(max_length=20, null=True)),
                ('date', models.DateTimeField(verbose_name='when the bid was made')),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.Auction')),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
