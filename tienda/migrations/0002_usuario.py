# Generated by Django 4.2.5 on 2023-10-09 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=15)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
    ]
