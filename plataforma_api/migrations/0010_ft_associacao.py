# Generated by Django 2.1.2 on 2019-05-25 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma_api', '0009_auto_20181107_0052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ft_associacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antecedente', models.CharField(max_length=100)),
                ('consequente', models.CharField(max_length=50)),
                ('suporte', models.FloatField(default=0)),
                ('confianca', models.FloatField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('ano', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='id_ano_id', to='plataforma_api.Dim_ano')),
                ('id_curso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='id_curso_id', to='plataforma_api.Dim_curso')),
            ],
        ),
    ]