# Generated by Django 5.1.1 on 2024-11-28 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_servicerequest_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='customer_name',
            field=models.CharField(default='Unknown', max_length=255),
        ),
    ]
