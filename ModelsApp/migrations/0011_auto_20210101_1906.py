# Generated by Django 3.1.4 on 2021-01-01 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModelsApp', '0010_themahatah_detatime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='themahatah',
            name='detaTime',
            field=models.DateField(),
        ),
    ]