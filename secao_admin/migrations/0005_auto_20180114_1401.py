# Generated by Django 2.0.1 on 2018-01-14 14:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secao_admin', '0004_auto_20180113_2013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='veiculo',
            new_name='veiculos',
        ),
        migrations.AlterField(
            model_name='historico',
            name='data_devolucao',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2018, 1, 14, 14, 0, 56, 950003), null=None),
        ),
        migrations.AlterField(
            model_name='historico',
            name='data_reserva',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2018, 1, 14, 14, 0, 56, 949978), null=None),
        ),
        migrations.AlterField(
            model_name='reservas',
            name='data_devolucao',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2018, 1, 14, 14, 0, 56, 949455), null=None),
        ),
        migrations.AlterField(
            model_name='reservas',
            name='data_reserva',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2018, 1, 14, 14, 0, 56, 949427), null=None),
        ),
    ]
