# Generated by Django 4.2 on 2023-04-04 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shinkassa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worktable',
            name='cost_appworks',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]
