# Generated by Django 2.1.3 on 2018-11-04 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('royale', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carta',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='cartar', verbose_name='Imagen'),
        ),
    ]
