# Generated by Django 4.0.5 on 2022-06-16 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_packets_monthlypayment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
