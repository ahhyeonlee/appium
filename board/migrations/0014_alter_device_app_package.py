# Generated by Django 3.2.7 on 2021-10-01 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0013_auto_20211001_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='app_package',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
    ]