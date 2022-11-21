# Generated by Django 4.1.3 on 2022-11-19 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('DiseaseType', '0001_initial'),
        ('Doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialize',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='specializations', serialize=False, to='DiseaseType.diseasetype')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specializations', to='Doctor.doctor')),
            ],
            options={
                'unique_together': {('id', 'email')},
            },
        ),
    ]