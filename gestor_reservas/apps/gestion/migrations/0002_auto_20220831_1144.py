# Generated by Django 2.2.27 on 2022-08-31 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservacion',
            name='puestos',
            field=models.IntegerField(verbose_name='Numero de puestos'),
        ),
    ]
