# Generated by Django 5.0.1 on 2024-01-24 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_client_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(choices=[('Wagner', 'Wagner'), ('Desert Ortho', 'Desert Ortho'), ('Georiga Eye Institute', 'Georiga Eye Institute')], max_length=100),
        ),
    ]
