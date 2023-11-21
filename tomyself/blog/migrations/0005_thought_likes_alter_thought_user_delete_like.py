# Generated by Django 4.2.6 on 2023-11-06 02:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_like_thought'),
    ]

    operations = [
        migrations.AddField(
            model_name='thought',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='thought', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='thought',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]