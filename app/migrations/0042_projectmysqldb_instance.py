# Generated by Django 2.2.11 on 2020-08-21 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_auto_20200821_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmysqldb',
            name='instance',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.MySQLInstance'),
            preserve_default=False,
        ),
    ]