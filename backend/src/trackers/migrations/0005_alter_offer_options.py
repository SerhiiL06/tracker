# Generated by Django 4.2 on 2024-05-30 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0004_alter_campaign_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='offer',
            options={'ordering': ['-created_at']},
        ),
    ]