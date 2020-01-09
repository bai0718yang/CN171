# Generated by Django 2.2.5 on 2020-01-02 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CN171_operation', '0009_auto_20191231_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='OprFinanceReco',
            fields=[
                ('opr_finance_reco_id', models.AutoField(primary_key=True, serialize=False, verbose_name='稽核记录id')),
                ('opr_finance_reco_result', models.CharField(max_length=8, verbose_name='稽核结果')),
                ('opr_finance_reco_time', models.DateTimeField(blank=True, null=True, verbose_name='稽核操作时间')),
                ('opr_finance_reco_file', models.CharField(max_length=32, verbose_name='稽核结果文件')),
                ('opr_finance_reco_filedir', models.CharField(blank=True, max_length=128, null=True, verbose_name='稽核结果文件存储地址')),
                ('opr_finance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reco', to='CN171_operation.OprFinance')),
            ],
            options={
                'verbose_name': 'CMIOT账务稽核表',
                'verbose_name_plural': 'CMIOT账务稽核表',
                'db_table': 'opr_finance_reco',
                'ordering': ['-opr_finance_reco_id'],
            },
        ),
    ]
