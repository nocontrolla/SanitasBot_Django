# Generated by Django 4.2.3 on 2023-07-13 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0007_alter_appointment_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='state',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=20),
        ),
    ]
