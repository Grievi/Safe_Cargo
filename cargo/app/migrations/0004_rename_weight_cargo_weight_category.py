# Generated by Django 3.2.8 on 2021-10-28 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211028_0506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cargo',
            old_name='weight',
            new_name='weight_category',
        ),
    ]
