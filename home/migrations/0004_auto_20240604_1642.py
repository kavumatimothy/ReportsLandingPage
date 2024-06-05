# Generated by Django 3.1 on 2024-06-04 14:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20240604_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='date_create',
            new_name='date_created',
        ),
        migrations.AddField(
            model_name='department',
            name='date_created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(choices=[('finance', 'finance'), ('monitoring and evaluation', 'monitoring and evaluation'), ('her', 'hr'), ('clinical', 'clinical')], max_length=200, unique=True),
        ),
    ]