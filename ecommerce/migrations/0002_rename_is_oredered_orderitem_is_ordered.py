# Generated by Django 3.2.7 on 2021-10-21 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='is_oredered',
            new_name='is_ordered',
        ),
    ]