# Generated by Django 5.1.2 on 2024-11-02 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0013_project_completion_date_project_completion_notes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='markup_percentage',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
