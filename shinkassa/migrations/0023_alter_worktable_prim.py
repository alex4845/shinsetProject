# Generated by Django 4.1.3 on 2023-04-07 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shinkassa', '0022_alter_worktable_balance_alter_worktable_complex_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worktable',
            name='prim',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
