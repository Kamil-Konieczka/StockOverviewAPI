# Generated by Django 3.0.6 on 2020-05-10 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preserial_stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectname',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Project name'),
        ),
        migrations.AlterField(
            model_name='singleproductsnumber',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Single product '),
        ),
    ]