# Generated by Django 4.1.3 on 2022-12-08 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_delete_user_storageunit_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storageunit',
            name='available',
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='fullname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='zipcode',
            field=models.CharField(max_length=5),
        ),
    ]