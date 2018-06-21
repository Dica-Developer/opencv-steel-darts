# Generated by Django 2.0.3 on 2018-06-21 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('darts_ui', '0005_auto_20180621_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='throws',
            field=models.ForeignKey(blank=True, help_text='Throws for this game', null=True, on_delete=django.db.models.deletion.SET_NULL, to='darts_ui.Throw'),
        ),
    ]
