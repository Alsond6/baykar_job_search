# Generated by Django 4.1.2 on 2022-10-19 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0002_alter_job_applicants_alter_job_country_and_more'),
        ('account', '0003_profile_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applications',
            name='applicant_user',
        ),
        migrations.AddField(
            model_name='applications',
            name='applied_job',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.RESTRICT, to='jobapp.job'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(),
        ),
    ]