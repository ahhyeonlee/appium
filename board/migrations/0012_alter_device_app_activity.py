# Generated by Django 3.2.7 on 2021-10-01 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0011_remove_scenario_case_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='app_activity',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]