# Generated by Django 4.2 on 2023-04-05 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shinkassa', '0007_worktable_summ_alter_worktable_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worktable',
            name='balance',
            field=models.IntegerField(default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='worktable',
            name='complex',
            field=models.IntegerField(default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='worktable',
            name='cost_appworks',
            field=models.IntegerField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='worktable',
            name='count_gruz',
            field=models.IntegerField(default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='worktable',
            name='demont',
            field=models.IntegerField(default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='worktable',
            name='mont',
            field=models.IntegerField(default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='worktable',
            name='sn',
            field=models.IntegerField(default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='worktable',
            name='time',
            field=models.DateTimeField(default='2023-04-05 10:40', editable=False),
        ),
        migrations.AlterField(
            model_name='worktable',
            name='ust',
            field=models.IntegerField(default=0, max_length=3),
        ),
    ]