# Generated by Django 4.2.7 on 2023-12-06 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestforms', '0007_remove_transaction_other_cmv_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='Cryo_Measurement',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='FFP_Measurement',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='Platelets_Measurement',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='RC_Measurement',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
