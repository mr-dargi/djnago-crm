# Generated by Django 4.2.7 on 2023-12-23 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("crm", "0007_delete_contactlist"),
    ]

    operations = [
        migrations.AddField(
            model_name="project_procedure",
            name="support",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="supports",
                to=settings.AUTH_USER_MODEL,
                verbose_name="پشتیبانی",
            ),
        ),
    ]