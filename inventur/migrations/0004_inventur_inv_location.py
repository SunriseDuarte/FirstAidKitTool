# Generated by Django 4.2 on 2024-06-06 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventur', '0003_remove_inventur_inventuritems_inventuritem_inv_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventur',
            name='inv_location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventur.location'),
            preserve_default=False,
        ),
    ]