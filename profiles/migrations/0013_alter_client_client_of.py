# Generated by Django 3.2.4 on 2021-06-09 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_auto_20210609_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_of',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='profiles.profile'),
        ),
    ]
