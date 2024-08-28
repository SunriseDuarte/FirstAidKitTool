# Generated by Django 4.2 on 2024-06-06 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventur', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventuritem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_name', models.CharField(max_length=50)),
                ('item_amount_soll', models.IntegerField()),
                ('item_amount_ist', models.IntegerField()),
                ('inv_comment', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Inventur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=50)),
                ('inventuritems', models.ManyToManyField(blank=True, related_name='inventur_item', to='inventur.inventuritem')),
            ],
        ),
    ]
