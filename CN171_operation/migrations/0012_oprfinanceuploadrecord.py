# Generated by Django 2.2.5 on 2020-01-08 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CN171_operation', '0011_auto_20200102_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='OprFinanceUploadRecord',
            fields=[
                ('opr_finance_upload_id', models.AutoField(primary_key=True, serialize=False, verbose_name='文件上传记录id')),
                ('opr_finance_upload_status', models.CharField(max_length=8, verbose_name='文件上传状态')),
                ('opr_finance_upload_time', models.DateTimeField(blank=True, null=True, verbose_name='文件上传时间')),
                ('opr_finance_upload_list', models.TextField(verbose_name='上传文件清单')),
            ],
            options={
                'verbose_name': 'CMIOT账务文件上传记录表',
                'verbose_name_plural': 'CMIOT账务文件上传记录表',
                'db_table': 'opr_finance_uploadrecord',
                'ordering': ['-opr_finance_upload_id'],
            },
        ),
    ]
