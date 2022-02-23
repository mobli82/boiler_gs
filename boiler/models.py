from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Boiler(models.Model):
    # boiler's temperatures
    boiler_temp     = models.DecimalField(decimal_places=1, max_digits=3)
    boiler_return   = models.DecimalField(decimal_places=1, max_digits=3)
    feeder          = models.DecimalField(decimal_places=1, max_digits=3)
    boiler_exhaust  = models.DecimalField(decimal_places=1, max_digits=3, default=000.0)
    boiler_status   = models.BooleanField(default=True)
    record_date     = models.DateTimeField(auto_now=True)

    # temperatures out off boiler
    cwu          = models.DecimalField(decimal_places=1, max_digits=3)
    co           = models.DecimalField(decimal_places=1, max_digits=3)
    t_outside    = models.DecimalField(decimal_places=1, max_digits=3)
    t_inside     = models.DecimalField(decimal_places=1, max_digits=3)
    t_floor      = models.DecimalField(decimal_places=1, max_digits=3)

    # statuses
    co_pomp_status      = models.BooleanField(default=False)
    cwu1_pomp_status    = models.BooleanField(default=False)
    cwu2_pomp_status    = models.BooleanField(default=False)
    cycle_pomp_status   = models.BooleanField(default=False)
    feeder_status       = models.BooleanField(default=False)
    fan_status          = models.BooleanField(default=False)
    termostat_status    = models.BooleanField(default=False)

class BurnSettings(models.Model):
    # PIEC_ZADANA
    set_boiler_temp = models.IntegerField(default=50)
    
    # RR_PRACA_PODANIE
    work_feed = models.IntegerField(default=10)
    
    # RR_PRACA_POSTOJ
    work_pause = models.IntegerField(default=60)
    
    # RR_PRACA_MOC
    work_power = models.IntegerField(default=100)
    is_changed = models.BooleanField(default=False)