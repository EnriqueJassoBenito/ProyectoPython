# Generated by Django 5.1.4 on 2025-02-25 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('matricula', models.CharField(max_length=10, unique=True)),
                ('correo', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
