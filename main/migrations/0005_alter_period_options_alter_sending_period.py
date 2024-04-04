# Generated by Django 5.0.3 on 2024-04-04 14:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_client_options_alter_message_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='period',
            options={'verbose_name': 'периодичность', 'verbose_name_plural': 'периодичности'},
        ),
        migrations.AlterField(
            model_name='sending',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.period', verbose_name='периодичность рассылки'),
        ),
    ]