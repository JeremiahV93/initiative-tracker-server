# Generated by Django 3.1.7 on 2021-03-06 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initiativeTrackerApi', '0003_auto_20210304_0217'),
    ]

    operations = [
        migrations.AddField(
            model_name='playercharacter',
            name='alive',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='playercharacter',
            name='characterClass',
            field=models.CharField(choices=[('bab', 'Barbarian'), ('bad', 'Bard'), ('cle', 'Cleric'), ('dru', 'Druid'), ('fig', 'Fighter'), ('mon', 'Monk'), ('pal', 'Paladin'), ('ran', 'Ranger'), ('rog', 'Rogue'), ('sor', 'Sorcerer'), ('war', 'Warlock'), ('wiz', 'Wizard')], default=None, max_length=3),
        ),
    ]