# Generated by Django 4.2.2 on 2024-05-18 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_message_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sending',
            options={'ordering': ('start_time',), 'permissions': [('can_view_all_sendings', 'can view all sendings'), ('can_switch_status', 'can switch status')], 'verbose_name': 'рассылка', 'verbose_name_plural': 'рассылки'},
        ),
    ]
