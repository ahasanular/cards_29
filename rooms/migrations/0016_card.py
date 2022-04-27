# Generated by Django 4.0.4 on 2022-04-23 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
        ('rooms', '0015_delete_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='card_holder', to='registration.appuser')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='card_name', to='rooms.deck')),
            ],
        ),
    ]
