# Generated by Django 4.0 on 2021-12-10 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='message_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
