# Generated by Django 4.0.6 on 2022-07-21 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='addess_zipcode',
            new_name='address_zipcode',
        ),
    ]
