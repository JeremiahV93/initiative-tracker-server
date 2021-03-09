# Generated by Django 3.1.7 on 2021-03-06 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initiativeTrackerApi', '0005_auto_20210306_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='charisma_savingthrow',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='monster',
            name='constitution_savingthrow',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='monster',
            name='dexterity_savingthrow',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='monster',
            name='intelligence_savingthrow',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='monster',
            name='strength_savingthrow',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='monster',
            name='wisdom_savingthrow',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='monster',
            name='conditionImmunity',
            field=models.TextField(default='none'),
        ),
        migrations.AlterField(
            model_name='monster',
            name='damageImmunity',
            field=models.TextField(default='none'),
        ),
        migrations.AlterField(
            model_name='monster',
            name='damageResistance',
            field=models.TextField(default='none'),
        ),
        migrations.AlterField(
            model_name='monster',
            name='spellcaster',
            field=models.BooleanField(default=False),
        ),
    ]