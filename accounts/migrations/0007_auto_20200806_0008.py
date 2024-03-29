# Generated by Django 3.0.8 on 2020-08-06 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200805_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='bairro',
            field=models.CharField(blank=True, max_length=50, verbose_name='Bairro'),
        ),
        migrations.AddField(
            model_name='order',
            name='cep',
            field=models.CharField(blank=True, max_length=8, verbose_name='CEP'),
        ),
        migrations.AddField(
            model_name='order',
            name='complemento',
            field=models.CharField(blank=True, max_length=50, verbose_name='Complemento'),
        ),
        migrations.AddField(
            model_name='order',
            name='endereco',
            field=models.CharField(blank=True, max_length=200, verbose_name='Endereço'),
        ),
        migrations.AddField(
            model_name='order',
            name='numero',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(auto_now=True, verbose_name='Data do Pedido'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Aguardando Pagamento', 'Aguardando Pagamento'), ('Efetuado - Confirmado', 'Efetuado - Confirmado'), ('Entregue - Finalizado', 'Entregue - Finalizado')], max_length=50),
        ),
    ]
