# Generated by Django 4.2.2 on 2023-08-20 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_evento_qr_code_evento_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='eventos_foto'),
        ),
    ]
