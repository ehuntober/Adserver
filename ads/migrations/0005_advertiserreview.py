# Generated by Django 4.2 on 2023-04-28 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_ad_click_count_ad_impression_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertiserReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('comment', models.TextField()),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='ads.ad')),
            ],
        ),
    ]
