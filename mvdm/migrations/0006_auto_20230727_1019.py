# Generated by Django 3.2.19 on 2023-07-27 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvdm', '0005_remove_orderdetail_stripe_payment_intent'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='total_sales',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='total_sales_amount',
            field=models.IntegerField(default=0),
        ),
    ]
