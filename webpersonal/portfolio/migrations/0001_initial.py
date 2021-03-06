# Generated by Django 2.0.2 on 2018-06-10 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('image', models.ImageField(upload_to='', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modoficación')),
            ],
            options={
                'verbose_name': 'proyecto',
                'verbose_name_plural': 'proyectos',
                'ordering': ['-created'],
            },
        ),
    ]
