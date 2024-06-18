# Generated by Django 3.1 on 2024-06-06 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(choices=[('finance', 'Finance'), ('monitoring and evaluation', 'Monitoring And Evaluation'), ('hr', 'Human Resource'), ('Community', 'Community'), ('clinical', 'Clinical'), ('research', 'Research'), ('communications', 'Communications'), ('Informatics and IT', 'Informatics and IT')], max_length=200, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='report',
            old_name='date_create',
            new_name='date_created',
        ),
        migrations.AlterField(
            model_name='report',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.department'),
        ),
        migrations.DeleteModel(
            name='Deprtment',
        ),
    ]