# Generated by Django 5.0.6 on 2024-06-13 11:10

import account.utility
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_number', models.CharField(default=account.utility.generate_account_number, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('pin', models.CharField(max_length=4)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('account_type', models.CharField(choices=[('S', 'SAVINGS'), ('C', 'CURRENT'), ('D', 'DOM')], default='S', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('DEB', 'DEBIT'), ('CRE', 'CREDIT'), ('TRA', 'TRANSFER')], default='CRE', max_length=3)),
                ('transaction_time', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('description', models.TextField()),
                ('transaction_status', models.CharField(choices=[('S', 'SUCCESSFUL'), ('F', 'FAILED'), ('P', 'PENDING')], default='S', max_length=1)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
    ]
