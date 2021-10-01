# Generated by Django 3.2.7 on 2021-10-01 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('date_of_graduation', models.DateTimeField()),
                ('date_of_employment', models.DateTimeField()),
                ('position', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('employee_code', models.CharField(blank=True, max_length=6, null=True)),
            ],
            options={
                'verbose_name_plural': 'Employee Records',
            },
        ),
        migrations.CreateModel(
            name='Supervisors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supervisor', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Supervisors',
            },
        ),
        migrations.CreateModel(
            name='UploadLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_of_upload', models.DateTimeField(auto_now_add=True)),
                ('number_of_employee_records_uploaded', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
                ('errors', models.CharField(blank=True, max_length=100, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.employee')),
            ],
            options={
                'verbose_name_plural': 'Upload logs',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='supervisors',
            field=models.ManyToManyField(blank=True, null=True, to='mainApp.Supervisors'),
        ),
    ]
