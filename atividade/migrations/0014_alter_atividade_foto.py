# Generated by Django 4.2.2 on 2023-08-21 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atividade', '0013_atividade_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='foto',
            field=models.ImageField(blank=True, default='atividade_default.avif', null=True, upload_to='atividade_foto'),
        ),
    ]
