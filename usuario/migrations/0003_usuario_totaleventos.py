# Generated by Django 4.2.2 on 2023-08-18 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_usuario_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='totalEventos',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
