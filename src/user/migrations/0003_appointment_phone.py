# Generated by Django 4.0 on 2021-12-10 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_appointment_message_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='phone',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]