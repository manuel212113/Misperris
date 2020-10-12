# Generated by Django 3.1.1 on 2020-10-08 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalRescatado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=20)),
                ('raza', models.CharField(max_length=9)),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(choices=[('rescatado', 'Rescatado'), ('disponible', 'Disponible'), ('adoptado', 'Adoptado')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudAdopcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('rut', models.CharField(max_length=9)),
                ('nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=10)),
                ('region', models.TextField()),
                ('comuna', models.TextField()),
                ('tipo_vivienda', models.TextField()),
            ],
        ),
    ]
