# Generated by Django 2.0.1 on 2018-01-12 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id_historico', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('data_reserva', models.DateField()),
                ('data_entrega', models.DateField()),
                ('reservado_por', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id_modelo', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('modelo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id_veiculo', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('placa', models.CharField(max_length=200)),
                ('nome', models.CharField(max_length=200)),
                ('data_fabricacao', models.DateField()),
                ('estado', models.CharField(max_length=200)),
                ('fk_modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secao_admin.Modelo')),
            ],
        ),
        migrations.AddField(
            model_name='historico',
            name='fk_veiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secao_admin.Veiculo'),
        ),
    ]
