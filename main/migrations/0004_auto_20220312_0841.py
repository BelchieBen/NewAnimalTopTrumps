# Generated by Django 3.2.9 on 2022-03-12 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220311_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='players',
        ),
        migrations.AddField(
            model_name='players',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.room'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='RoomPlayers',
        ),
    ]
