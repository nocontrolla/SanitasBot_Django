# Generated by Django 4.2.1 on 2023-07-01 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0003_remove_prescription_doctor_alter_prescription_dosage_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescription',
            old_name='patient',
            new_name='patient_doctor',
        ),
    ]
