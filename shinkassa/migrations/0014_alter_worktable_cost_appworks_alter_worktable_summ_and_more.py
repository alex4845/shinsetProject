# Generated by Django 4.2 on 2023-04-05 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shinkassa', '0013_remove_worktable_count_tl_remove_worktable_tl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worktable',
            name='cost_appworks',
            field=models.FloatField(blank=True, default=0, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='worktable',
            name='summ',
            field=models.FloatField(blank=True, default=0, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='worktable',
            name='time',
            field=models.DateTimeField(default='2023-04-05 13:09', editable=False),
        ),
    ]
