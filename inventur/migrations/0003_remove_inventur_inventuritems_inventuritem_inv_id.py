# Generated by Django 4.2 on 2024-06-06 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventur', '0002_inventuritem_inventur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventur',
            name='inventuritems',
        ),
        migrations.AddField(
            model_name='inventuritem',
            name='inv_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventur.inventur'),
            preserve_default=False,
        ),
    ]