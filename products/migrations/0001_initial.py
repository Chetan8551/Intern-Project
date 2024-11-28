# Generated by Django 5.1.1 on 2024-10-03 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_code', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('unit_price', models.FloatField()),
                ('invoice_date', models.DateTimeField()),
                ('customer_id', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
