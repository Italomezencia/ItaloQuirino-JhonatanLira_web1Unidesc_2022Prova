# Generated by Django 4.0.4 on 2022-06-23 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula_imo', models.CharField(max_length=100)),
                ('rua_imo', models.CharField(max_length=100)),
                ('cep_imo', models.CharField(max_length=100)),
                ('bairro_imo', models.CharField(max_length=100)),
                ('cidade_imo', models.CharField(max_length=100)),
                ('uf_imo', models.CharField(max_length=100)),
                ('tamanho_imo', models.CharField(max_length=100)),
                ('comodos_imo', models.CharField(max_length=100)),
                ('garagen_imo', models.CharField(max_length=100)),
                ('valor_imo', models.CharField(max_length=100)),
                ('tipo_imo', models.CharField(max_length=100)),
                ('status_imo', models.CharField(max_length=100)),
            ],
        ),
    ]
