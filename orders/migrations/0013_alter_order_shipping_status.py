# Generated by Django 3.2.2 on 2021-06-02 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_order_shipping_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_status',
            field=models.CharField(blank=True, default='Order Placed', max_length=20, null=True),
        ),
    ]
