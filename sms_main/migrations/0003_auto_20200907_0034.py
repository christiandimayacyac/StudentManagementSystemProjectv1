# Generated by Django 3.1 on 2020-09-07 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms_main', '0002_auto_20200904_0815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stafffeedback',
            old_name='student_id',
            new_name='staff_id',
        ),
    ]
