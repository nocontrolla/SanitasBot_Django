# Generated by Django 4.2.1 on 2023-07-13 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_alter_appointment_doctor_alter_appointment_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
