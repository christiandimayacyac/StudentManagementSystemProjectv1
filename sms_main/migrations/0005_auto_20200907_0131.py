# Generated by Django 3.1 on 2020-09-07 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sms_main', '0004_auto_20200907_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavereportstaff',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_main.staff'),
        ),
        migrations.AlterField(
            model_name='studentnotification',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_main.staff'),
        ),
    ]
