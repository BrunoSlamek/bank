# Generated by Django 4.0.5 on 2022-06-25 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_carteira_qtd_venda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carteira',
            name='qtd_aplicacoes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='carteira',
            name='qtd_venda',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='carteira',
            name='saldo',
            field=models.IntegerField(default=0),
        ),
    ]