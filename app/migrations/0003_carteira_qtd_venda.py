# Generated by Django 4.0.5 on 2022-06-25 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_aplicacao_operacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='carteira',
            name='qtd_venda',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]