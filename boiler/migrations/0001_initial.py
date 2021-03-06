# Generated by Django 4.0 on 2022-01-21 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boiler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boiler_temp', models.DecimalField(decimal_places=1, max_digits=3)),
                ('boiler_return', models.DecimalField(decimal_places=1, max_digits=3)),
                ('feeder', models.DecimalField(decimal_places=1, max_digits=3)),
                ('boiler_exhaust', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('boiler_status', models.BooleanField(default=True)),
                ('record_date', models.DateTimeField(auto_now=True)),
                ('cwu', models.DecimalField(decimal_places=1, max_digits=3)),
                ('co', models.DecimalField(decimal_places=1, max_digits=3)),
                ('t_outside', models.DecimalField(decimal_places=1, max_digits=3)),
                ('t_inside', models.DecimalField(decimal_places=1, max_digits=3)),
                ('t_floor', models.DecimalField(decimal_places=1, max_digits=3)),
                ('co_pomp_status', models.BooleanField(default=False)),
                ('cwu1_pomp_status', models.BooleanField(default=False)),
                ('cwu2_pomp_status', models.BooleanField(default=False)),
                ('cycle_pomp_status', models.BooleanField(default=False)),
                ('feeder_status', models.BooleanField(default=False)),
                ('fan_status', models.BooleanField(default=False)),
                ('termostat_status', models.BooleanField(default=False)),
            ],
        ),
    ]
