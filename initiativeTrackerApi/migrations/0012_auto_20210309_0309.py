# Generated by Django 3.1.7 on 2021-03-09 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initiativeTrackerApi', '0011_auto_20210309_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monsterencounterpair',
            name='currentHealth',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='monsterencounterpair',
            name='temporaryHealth',
            field=models.IntegerField(default=0),
        ),
    ]
