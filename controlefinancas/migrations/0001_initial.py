# Generated by Django 3.2.18 on 2023-04-15 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.DateField(auto_now_add=True)),
                ('descricao', models.TextField()),
                ('categoria', models.CharField(choices=[('ESCOLHA', 'Escolha uma categoria'), ('AL', 'Alimentação'), ('MRD', 'Moradia'), ('TSP', 'Transporte'), ('SD', 'Saúde'), ('LZR', 'Lazer'), ('TEL', 'Telefone'), ('INT', 'Internet'), ('EDU', 'Educação')], default='ESCOLHA', max_length=10)),
                ('comprovante', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'Despesa',
                'verbose_name_plural': 'Despesas',
                'ordering': ['-data'],
            },
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.DateField(auto_now_add=True)),
                ('descricao', models.TextField()),
                ('categoria', models.CharField(choices=[('ESCOLHA', 'Escolha uma categoria'), ('SLR', 'Salario'), ('MSD', 'Mesada'), ('VDA', 'Vendas avulsa')], default='ESCOLHA', max_length=10)),
                ('comprovante', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'Receita',
                'verbose_name_plural': 'Receitas',
            },
        ),
    ]
