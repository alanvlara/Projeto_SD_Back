# Generated by Django 4.2.2 on 2023-08-12 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='usuario_foto'),
        ),
    ]
