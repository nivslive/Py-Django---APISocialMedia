# Generated by Django 4.1.7 on 2023-03-25 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trend', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Trends',
            new_name='Trend',
        ),
        migrations.AlterModelTable(
            name='trend',
            table='trend',
        ),
    ]
