# Generated by Django 2.1.3 on 2018-11-20 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6)),
                ('codigo', models.CharField(max_length=5)),
                ('descricao', models.TextField()),
            ],
        ),
    ]
