# Generated by Django 3.1.4 on 2021-01-07 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Weblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('data', models.JSONField(null=True)),
            ],
        ),
    ]
