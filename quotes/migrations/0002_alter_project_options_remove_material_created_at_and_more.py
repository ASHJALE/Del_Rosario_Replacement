# Generated by Django 5.1.2 on 2024-10-31 21:25

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='material',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='material',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='material',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='pricing',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='pricing',
            name='date',
        ),
        migrations.RemoveField(
            model_name='pricing',
            name='materials',
        ),
        migrations.RemoveField(
            model_name='pricing',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='project',
            name='approved_by_admin',
        ),
        migrations.RemoveField(
            model_name='project',
            name='approved_by_user',
        ),
        migrations.RemoveField(
            model_name='project',
            name='declined_by_admin',
        ),
        migrations.RemoveField(
            model_name='project',
            name='declined_by_user',
        ),
        migrations.RemoveField(
            model_name='project',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='name',
        ),
        migrations.RemoveField(
            model_name='project',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='status',
        ),
        migrations.RemoveField(
            model_name='projectelement',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='projectelement',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='quotation',
            name='element',
        ),
        migrations.RemoveField(
            model_name='quotation',
            name='material',
        ),
        migrations.RemoveField(
            model_name='quotation',
            name='quantity',
        ),
        migrations.AddField(
            model_name='material',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pricing',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(default='New Project', max_length=200),  # Changed default to string
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectelement',
            name='element_name',
            field=models.CharField(default='Unnamed Element', max_length=100),  # Changed to string
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectelement',
            name='quantity',
            field=models.IntegerField(default=0),  # Changed default to integer
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectelement',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),  # Already correct
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quotation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 10, 31, 21, 25, 7, 581283, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quotation',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='material',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
