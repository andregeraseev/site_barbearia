# Generated by Django 4.1 on 2022-08-23 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_inicial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Body',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('texto', models.TextField()),
            ],
        ),
    ]
