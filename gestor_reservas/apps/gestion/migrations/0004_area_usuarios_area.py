# Generated by Django 4.1 on 2022-09-06 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_alter_reservacion_id_alter_usuarios_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Área')),
            ],
        ),
        migrations.AddField(
            model_name='usuarios',
            name='area',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='gestion.area', verbose_name='Área'),
        ),
    ]
