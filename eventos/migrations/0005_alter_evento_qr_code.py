# Generated by Django 4.2.2 on 2023-08-20 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0004_alter_evento_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='qr_code',
            field=models.URLField(blank=True, null=True),
        ),
    ]
