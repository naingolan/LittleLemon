# Generated by Django 4.1.5 on 2023-04-04 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LittleLemonDRF", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menuitem",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
