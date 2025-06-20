# Generated by Django 3.2.20 on 2025-06-13 19:54

import api.models.order_model
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(default='Unkown', max_length=250)),
                ('amount', models.IntegerField(default=1)),
                ('current_state', models.CharField(default='Pending', max_length=100)),
                ('state_log', models.JSONField(default=api.models.order_model.initial_state)),
                ('active_ticket', models.IntegerField(default=-1)),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='api.product')),
            ],
        ),
    ]
