# Generated by Django 5.1.6 on 2025-02-05 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0002_rename_type_complaint_service_alter_complaint_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='email',
            field=models.CharField(max_length=500),
        ),
    ]
