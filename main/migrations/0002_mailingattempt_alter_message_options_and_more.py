# Generated by Django 5.0.3 on 2024-04-02 13:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latest_att_time', models.DateTimeField(verbose_name='время последней попытки')),
                ('status', models.BooleanField(default=False, verbose_name='статус')),
                ('server_response', models.TextField(verbose_name='ответ сервера')),
            ],
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'сообщение', 'verbose_name_plural': 'сообщения'},
        ),
        migrations.RemoveField(
            model_name='client',
            name='sending',
        ),
        migrations.AddField(
            model_name='sending',
            name='client',
            field=models.ManyToManyField(to='main.client', verbose_name='клиент'),
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(max_length=50, verbose_name='тема сообщения'),
        ),
        migrations.AlterField(
            model_name='period',
            name='day',
            field=models.IntegerField(verbose_name='дни'),
        ),
        migrations.AlterField(
            model_name='sending',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.message', verbose_name='содержание рассылки'),
        ),
        migrations.AlterField(
            model_name='sending',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.period', verbose_name='периодичность рассылки'),
        ),
        migrations.AddField(
            model_name='sending',
            name='attempt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.mailingattempt', verbose_name='попытка рассылки'),
        ),
    ]
