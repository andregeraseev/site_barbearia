# Generated by Django 4.1 on 2022-08-23 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_inicial', '0006_agendebody'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContatoBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_contato', models.CharField(max_length=100)),
                ('subtitulo_contato', models.CharField(max_length=100)),
                ('cidade_contato', models.CharField(max_length=100)),
                ('telefone_contato', models.CharField(max_length=20)),
                ('email_contato', models.EmailField(max_length=254)),
            ],
        ),
    ]