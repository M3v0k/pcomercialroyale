# Generated by Django 2.1.3 on 2018-11-04 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('imagen', models.ImageField(null=True, upload_to='cartas', verbose_name='Imagen')),
                ('detalle', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Carta',
                'verbose_name_plural': 'Cartas',
                'ordering': ['-nivel'],
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
            ],
            options={
                'verbose_name': 'Level',
                'verbose_name_plural': 'Levels',
                'ordering': ['-creado'],
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombre')),
                ('detalle', models.CharField(help_text='Describa el tipo', max_length=60, verbose_name='Detalle')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
                'ordering': ['-nombre'],
            },
        ),
        migrations.AddField(
            model_name='carta',
            name='nivel',
            field=models.ForeignKey(help_text='Ingrese un numeros entero', on_delete=django.db.models.deletion.CASCADE, related_name='keynivel', to='royale.Level'),
        ),
        migrations.AddField(
            model_name='carta',
            name='tipos',
            field=models.ManyToManyField(related_name='keytipo', to='royale.Tipo', verbose_name='Tipo'),
        ),
    ]