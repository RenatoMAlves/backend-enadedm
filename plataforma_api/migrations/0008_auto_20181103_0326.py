# Generated by Django 2.1.2 on 2018-11-03 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma_api', '0007_auto_20181025_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ft_resultado',
            name='id_estado',
        ),
        migrations.RemoveField(
            model_name='ft_resultado',
            name='volume_incidencias_porcentagem',
        ),
        migrations.AddField(
            model_name='ft_resultado',
            name='porcentagem_branco_invalida',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='ft_resultado',
            name='porcentagem_erradas',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='ft_resultado',
            name='porcentagem_incidencias',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='ft_resultado',
            name='qtd_branco_invalidas',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ft_resultado',
            name='qtd_certas',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ft_resultado',
            name='qtd_erradas',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ft_resultado',
            name='qtd_questoes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ft_resultado',
            name='porcentagem_certas',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ft_resultado',
            name='volume_incidencias',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Dim_estado',
        ),
    ]