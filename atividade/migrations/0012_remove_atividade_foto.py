# Generated by Django 4.2.2 on 2023-08-20 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atividade', '0011_atividade_titulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atividade',
            name='foto',
        ),
    ]