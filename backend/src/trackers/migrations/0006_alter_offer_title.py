# Generated by Django 4.2 on 2024-06-01 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0005_alter_offer_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]