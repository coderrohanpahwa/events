# Generated by Django 3.1.2 on 2020-10-17 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20201017_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercreation',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='usercreation',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usercreation',
            name='otp',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='usercreation',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usercreation',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]