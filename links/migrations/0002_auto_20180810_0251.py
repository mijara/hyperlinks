# Generated by Django 2.1 on 2018-08-10 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='description',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='keywords',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
    ]