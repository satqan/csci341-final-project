# Generated by Django 4.1.3 on 2022-11-19 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Disease', '0001_initial'),
        ('Country', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_enc_date', models.DateField()),
                ('cname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discovers', to='Country.country')),
                ('disease_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discovers', to='Disease.disease')),
            ],
            options={
                'unique_together': {('cname', 'disease_code')},
            },
        ),
    ]