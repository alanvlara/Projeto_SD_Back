# Generated by Django 4.2.2 on 2023-08-19 23:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventos', '0002_evento_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='eventos'),
        ),
        migrations.AddField(
            model_name='evento',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]