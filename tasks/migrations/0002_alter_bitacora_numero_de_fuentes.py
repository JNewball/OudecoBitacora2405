# Generated by Django 4.2 on 2023-04-04 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bitacora',
            name='Numero_de_fuentes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
