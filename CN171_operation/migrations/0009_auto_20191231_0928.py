# Generated by Django 2.2.5 on 2019-12-31 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CN171_operation', '0008_auto_20191231_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='oprfinance',
            name='opr_ar_invoice_prorate',
            field=models.IntegerField(blank=True, null=True, verbose_name='分摊'),
        ),
        migrations.AddField(
            model_name='oprfinance',
            name='opr_unifypayment',
            field=models.IntegerField(blank=True, null=True, verbose_name='个人代付'),
        ),
        migrations.AlterField(
            model_name='oprfinance',
            name='opr_ar_adjustment',
            field=models.IntegerField(blank=True, null=True, verbose_name='调账'),
        ),
        migrations.AlterField(
            model_name='oprfinance',
            name='opr_ar_apply_detail',
            field=models.IntegerField(blank=True, null=True, verbose_name='销账'),
        ),
        migrations.AlterField(
            model_name='oprfinance',
            name='opr_ar_hunglog',
            field=models.IntegerField(blank=True, null=True, verbose_name='解挂账'),
        ),
        migrations.AlterField(
            model_name='oprfinance',
            name='opr_ar_invoice_detail',
            field=models.IntegerField(blank=True, null=True, verbose_name='账单'),
        ),
        migrations.AlterField(
            model_name='oprfinance',
            name='opr_ar_invoice_detail_owe',
            field=models.IntegerField(blank=True, null=True, verbose_name='欠费'),
        ),
        migrations.AlterField(
            model_name='oprfinance',
            name='opr_ar_transfer',
            field=models.IntegerField(blank=True, null=True, verbose_name='转账'),
        ),
        migrations.AlterField(
            model_name='oprfinance',
            name='opr_ar_writeoff',
            field=models.IntegerField(blank=True, null=True, verbose_name='呆坏账'),
        ),
        migrations.AlterField(
            model_name='oprfinance',
            name='opr_bb_bill_charge_bonus',
            field=models.IntegerField(blank=True, null=True, verbose_name='赠费'),
        ),
        migrations.AlterField(
            model_name='oprfinance',
            name='opr_bc_acct',
            field=models.IntegerField(blank=True, null=True, verbose_name='账户'),
        ),
        migrations.AlterField(
            model_name='oprfinance',
            name='opr_cm_acct_balance',
            field=models.IntegerField(blank=True, null=True, verbose_name='余额'),
        ),
        migrations.AlterField(
            model_name='oprfinance',
            name='opr_payment',
            field=models.IntegerField(blank=True, null=True, verbose_name='缴费'),
        ),
    ]
