# Generated by Django 4.1 on 2022-08-23 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_inicial', '0007_contatobody'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotosbody',
            name='publicada_body',
            field=models.BooleanField(default=False),
        ),
    ]
