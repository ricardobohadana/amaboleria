# Generated by Django 3.0.8 on 2020-08-04 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200730_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='nsu',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='order_description',
            field=models.TextField(default='', max_length=1000, verbose_name='Observação'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='recheio',
            field=models.CharField(blank=True, max_length=100, verbose_name='Recheio'),
        ),
    ]
