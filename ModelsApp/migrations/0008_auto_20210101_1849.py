# Generated by Django 3.1.4 on 2021-01-01 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ModelsApp', '0007_themahatah_cars'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='themahatah',
            options={'ordering': ['cars']},
        ),
    ]
