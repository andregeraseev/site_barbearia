# Generated by Django 4.1 on 2022-08-23 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_inicial', '0003_rename_texto_body_texto_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='body',
            name='subtitulo_body',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
