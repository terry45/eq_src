# Generated by Django 2.1.7 on 2019-03-22 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('register', '0002_auto_20190322_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='register.EquipmentModel'),
        ),
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]