# Generated by Django 3.2.2 on 2021-05-12 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_payment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='amount_paid',
        ),
    ]
