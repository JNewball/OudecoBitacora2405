# Generated by Django 4.2 on 2023-05-02 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_remove_ingeniero_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='Tipo_de_identificacion',
            field=models.IntegerField(choices=[(1, 'Seleccione'), (2, 'Cedula de ciudadania'), (3, 'Cedula de extranjeria'), (4, 'NIT')], default=1),
        ),
    ]
