# Generated by Django 4.1 on 2023-05-10 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setups', '0002_county_directorate_leavetype_quarter_region_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='system_designation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='setups.systemdesignation'),
        ),
    ]
