# Generated by Django 3.2.2 on 2021-05-26 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_rename_referal_account_referral'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='default.jpeg', null=True, upload_to='profile_images'),
        ),
    ]
