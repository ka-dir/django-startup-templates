# Generated by Django 4.2.1 on 2023-05-10 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=32, null=True)),
                ('code', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'verbose_name': 'County',
                'verbose_name_plural': 'Counties',
            },
        ),
        migrations.CreateModel(
            name='Directorate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=128, null=True)),
                ('code', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=128, null=True)),
                ('code', models.IntegerField(blank=True, default=0, null=True)),
                ('entitlement', models.IntegerField(blank=True, default=0, null=True)),
                ('max_to_take', models.IntegerField(blank=True, default=0, null=True)),
                ('carry_over_limit', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=32, null=True)),
                ('code', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReportingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=32, null=True)),
                ('code', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SystemDesignation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=128, null=True)),
                ('code', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SystemDesignationMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reporting_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reporting_to', to='setups.systemdesignation')),
                ('reporting_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setups.reportingtype')),
                ('system_designation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setups.systemdesignation')),
            ],
        ),
        migrations.CreateModel(
            name='SubCounty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=32, null=True)),
                ('code', models.IntegerField(blank=True, default=0, null=True)),
                ('county', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='setups.county')),
            ],
            options={
                'verbose_name': 'SubCounty',
                'verbose_name_plural': 'SubCounties',
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=255, null=True)),
                ('code', models.BigIntegerField(blank=True, default=0, null=True)),
                ('sub_county', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='setups.subcounty')),
            ],
        ),
        migrations.CreateModel(
            name='QuarterSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('quarter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='setups.quarter')),
            ],
        ),
        migrations.CreateModel(
            name='HrDesignation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=128, null=True)),
                ('code', models.IntegerField(blank=True, default=0, null=True)),
                ('system_designation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setups.systemdesignation')),
            ],
        ),
        migrations.CreateModel(
            name='DirectorateDivision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=128, null=True)),
                ('code', models.IntegerField(blank=True, default=0, null=True)),
                ('directorate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='setups.directorate')),
            ],
        ),
    ]
