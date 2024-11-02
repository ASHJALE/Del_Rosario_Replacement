# Generated by Django 5.1.2 on 2024-11-02 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0016_alter_quotation_area_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmaterial',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
