# Generated by Django 4.2.2 on 2023-08-15 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atividade', '0002_atividade_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='esporte',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
