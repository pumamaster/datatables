# Generated by Django 5.0.4 on 2024-04-08 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDatatables', '0003_alter_articulo_activo'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='publicado',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='evento',
            name='publicado',
            field=models.BooleanField(default=0),
        ),
    ]
