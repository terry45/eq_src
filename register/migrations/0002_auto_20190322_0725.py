# Generated by Django 2.1.7 on 2019-03-22 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='id',
        ),
        migrations.AlterField(
            model_name='device',
            name='ins_ref',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
