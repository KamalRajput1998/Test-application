# Generated by Django 4.2.7 on 2023-12-08 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestforms', '0008_alter_transaction_cryo_measurement_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='DateTimeRequired',
            field=models.DateTimeField(null=True),
        ),
    ]
