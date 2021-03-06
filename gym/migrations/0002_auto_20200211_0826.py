# Generated by Django 3.0.3 on 2020-02-10 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20200211_0826'),
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GymLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Exercise Date')),
                ('sets', models.IntegerField()),
                ('reps', models.IntegerField()),
                ('exercise_id', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Users')),
            ],
        ),
        migrations.DeleteModel(
            name='Log',
        ),
    ]
