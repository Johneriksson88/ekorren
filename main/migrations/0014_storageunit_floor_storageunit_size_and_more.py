# Generated by Django 4.1.3 on 2022-12-14 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_customer_orgnr_alter_customer_personnr'),
    ]

    operations = [
        migrations.AddField(
            model_name='storageunit',
            name='floor',
            field=models.CharField(choices=[('1st', '1st'), ('2nd', '2nd')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storageunit',
            name='size',
            field=models.CharField(choices=[('5 m2', '5 m2'), ('6 m2', '6 m2'), ('10 m2', '10 m2'), ('12 m2', '12 m2')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='storageunit',
            name='type',
            field=models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], max_length=100),
        ),
    ]