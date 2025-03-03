# Generated by Django 5.1 on 2025-01-06 06:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedeatail',
            name='empcode',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='EmployeeEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company1name', models.CharField(max_length=100, null=True)),
                ('comapny1desig', models.CharField(max_length=200, null=True)),
                ('company1salary', models.CharField(max_length=100, null=True)),
                ('comapny1duration', models.CharField(max_length=100, null=True)),
                ('company2name', models.CharField(max_length=100, null=True)),
                ('comapny2desig', models.CharField(max_length=200, null=True)),
                ('company2salary', models.CharField(max_length=100, null=True)),
                ('comapny2duration', models.CharField(max_length=100, null=True)),
                ('company3name', models.CharField(max_length=100, null=True)),
                ('comapny3desig', models.CharField(max_length=200, null=True)),
                ('company3salary', models.CharField(max_length=100, null=True)),
                ('comapny3duration', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
