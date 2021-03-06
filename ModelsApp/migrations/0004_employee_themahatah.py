# Generated by Django 3.1.4 on 2020-12-30 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ModelsApp', '0003_auto_20201230_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_employee', models.CharField(blank=True, max_length=50, null=True)),
                ('address_employee', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_employee', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TheMahatah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(blank=True, max_length=40, null=True)),
                ('manager_mahatah', models.CharField(blank=True, max_length=40, null=True)),
                ('number_employees', models.ManyToManyField(to='ModelsApp.Employee')),
                ('number_mahatah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelsApp.onemodels', verbose_name='number_mahatah')),
            ],
        ),
    ]
