# Generated by Django 4.2.1 on 2023-07-13 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_alter_appointment_date_alter_appointment_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient',
            field=models.CharField(max_length=255),
        ),
    ]
