# Generated by Django 3.1.1 on 2020-10-08 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPerris', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalrescatado',
            name='estado',
            field=models.CharField(choices=[('rescatado', 'Rescatado'), ('disponible', 'Disponible'), ('adoptado', 'Adoptado')], max_length=70),
        ),
        migrations.AlterField(
            model_name='animalrescatado',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='animalrescatado',
            name='raza',
            field=models.CharField(max_length=80),
        ),
    ]
