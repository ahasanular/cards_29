# Generated by Django 4.0.4 on 2022-04-19 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_1', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='person_1', to=settings.AUTH_USER_MODEL)),
                ('person_2', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='person_2', to=settings.AUTH_USER_MODEL)),
                ('person_3', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='person_3', to=settings.AUTH_USER_MODEL)),
                ('person_4', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='person_4', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
