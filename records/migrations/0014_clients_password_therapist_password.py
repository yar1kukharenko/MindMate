# Generated by Django 4.2.2 on 2023-07-04 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0013_remove_clients_password_remove_therapist_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='password',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='therapist',
            name='password',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]