# Generated by Django 3.2.18 on 2023-04-15 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlefinancas', '0003_alter_despesa_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='receita',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
