# Generated by Django 2.0.3 on 2018-06-15 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('darts_ui', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.TextField(default='GAME: <django.db.models.fields.related.OneToOneField>', help_text='Provide a name for the game')),
                ('game_type', models.CharField(choices=[('CR', 'Cricket'), ('501', '501'), ('301', '301'), ('KR', 'Killer')], default='CR', max_length=30)),
                ('result', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_status', models.BooleanField(default=False)),
                ('game_start', models.DateTimeField(default=None)),
                ('game_end', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('player_id', models.OneToOneField(default=0, on_delete=models.SET('DELETED'), primary_key=True, serialize=False, to='darts_ui.GameResults')),
                ('player_name', models.TextField(default='Hagbard Celine')),
            ],
        ),
        migrations.AddField(
            model_name='gameresults',
            name='game_id',
            field=models.OneToOneField(default=0, on_delete=models.SET('DELETED'), to='darts_ui.Games'),
        ),
        migrations.AddField(
            model_name='gameresults',
            name='player_id',
            field=models.OneToOneField(on_delete=models.SET('DELETED'), to='darts_ui.Players'),
        ),
    ]
