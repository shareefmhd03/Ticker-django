# Generated by Django 3.2.2 on 2021-05-25 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_product_offer_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='CouponCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_name', models.CharField(max_length=6)),
                ('price', models.IntegerField()),
                ('valid_from', models.DateField()),
                ('valid_upto', models.DateField()),
            ],
        ),
    ]
