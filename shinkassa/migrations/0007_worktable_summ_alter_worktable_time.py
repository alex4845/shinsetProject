# Generated by Django 4.2 on 2023-04-05 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shinkassa', '0006_alter_worktable_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='worktable',
            name='summ',
            field=models.IntegerField(default=0, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='worktable',
            name='time',
            field=models.DateTimeField(default='2023-04-05 10:11', editable=False),
        ),
    ]
