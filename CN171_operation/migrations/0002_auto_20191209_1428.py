# Generated by Django 2.2.5 on 2019-12-09 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CN171_operation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oprfinancecheckdetail',
            old_name='opr_finance_id',
            new_name='opr_finance',
        ),
        migrations.RenameField(
            model_name='oprfinancefiledetail',
            old_name='opr_finance_id',
            new_name='opr_finance',
        ),
    ]
