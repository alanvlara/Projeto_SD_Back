# Generated by Django 4.2.2 on 2023-09-18 00:44

import atividade.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atividade', '0018_alter_atividade_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='foto',
            field=models.ImageField(blank=True, default='padroes/atividade-default.jpg', null=True, upload_to=atividade.models.get_upload_path_atividade),
        ),
    ]