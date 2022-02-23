import datetime
import json
from decimal import Decimal

from django.db.models import Max
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.utils.timezone import make_aware
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib import messages

from functions import date_filter

from .forms import BurnSettingsForm
from .models import Boiler, BurnSettings

sensors = ['boiler_temp', 
            'boiler_return', 
            'feeder', 
            'temp_outside',
            'temp_inside',
            'CWU',
            'temp_floor', 
            'boiler_exhaust', 
            'CO',
            't2',
            't3',
            't4',
            't5',
            't6',
            't7',
            't8',
]
STATUS ={
    0: False,
    1: True,
    100: True
}
def seperate_boiler_temps(data):
    result = {}
    
    for key, value in zip(sensors, data):
        result[key] = value['t']
            
    return result 

@csrf_exempt
def boiler_post_temp(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        # converted str to dict
        data = eval(data)

        raw_temps = data['thermos']
        
        temps = seperate_boiler_temps(raw_temps)
        print(data)
        print('cwu1: ', data['cwu1'])
        
        # create boiler record
        boiler = Boiler.objects.create(
            boiler_temp=Decimal(temps['boiler_temp']),
            boiler_return=Decimal(temps['boiler_return']),
            feeder=Decimal(temps['feeder']),
            boiler_exhaust=Decimal(temps['boiler_exhaust']),
            
            cwu=temps['CWU'],
            co=temps['CO'],
            t_outside=temps['temp_outside'],
            t_inside=temps['temp_inside'],
            t_floor=temps['temp_floor'],
            
            co_pomp_status= STATUS[data['co']],
            cwu1_pomp_status= STATUS[data['cwu1']],
            cwu2_pomp_status= STATUS[data['cwu2']],
            cycle_pomp_status= STATUS[data['cyrk']],
            feeder_status= STATUS[data['pod']],
            fan_status= STATUS[data['wen0']],
            termostat_status= STATUS[data['ter']]
        )
        
        boiler.save()        
        return HttpResponse(data)

def bolier_monitor_view(request):
    if request.method == 'GET':
        
        # number of all records
        num_of_records = Boiler.objects.all().count()
        
        # collect last ten records
        date = Boiler.objects.values_list('record_date')[num_of_records-10:num_of_records]
        boiler_temp = Boiler.objects.values_list('boiler_temp')[num_of_records-10:num_of_records]
        boiler_return = Boiler.objects.values_list('boiler_return')[num_of_records-10:num_of_records]
        feeder = Boiler.objects.values_list('feeder')[num_of_records-10:num_of_records]
        
        dates = [x[0].strftime(format='%x %X') for x in list(date)]
        feeder = [str(x[0]) for x in list(feeder)]
        b_temps = [str(x[0]) for x in list(boiler_temp)]
        b_return = [str(x[0]) for x in list(boiler_return)]
        
        cwu = Boiler.objects.values_list('cwu')[num_of_records-10:num_of_records]
        co = Boiler.objects.values_list('co')[num_of_records-10:num_of_records]
        
        cwu_t1 = [str(x[0]) for x in list(cwu)]
        co_t = [str(x[0]) for x in list(co)]
        
        status = Boiler.objects.all().last()
        
        # print(status.co_pomp_status)
        
        devices_status = [
            status.co_pomp_status, 
            status.cwu1_pomp_status,
            status.cwu2_pomp_status,
            status.cycle_pomp_status,
            status.feeder_status,
            status.fan_status,
            status.termostat_status
        ]
        print(devices_status)
                
        data = {
            'dates': dates,
            'boiler_temp': b_temps,
            'boiler_return': b_return,
            'feeder': feeder,
            'cwu': cwu_t1,
            'co': co_t,
            'devices': devices_status 
        }
        return render(request, 'stats.html', {"data": data})
    
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        
        if date_from == '' or date_to == '':
            messages.warning(request, 'Days filter can Not be empty !!')
            return redirect('/boiler/monitor')
        
        # add try and except 
        
        year_from, month_from, day_from, hour_from, minute_from = date_filter(date_from)
        year_to, month_to, day_to, hour_to, minute_to = date_filter(date_to)
        
        start_date = datetime.datetime(year_from, month_from, day_from, hour_from, minute_from)
        end_date = datetime.datetime(year_to, month_to, day_to, hour_to, minute_to)
        
        """
            make_aware function makes a naive datetime.datetime in a given time zone aware.
        """
        start_aware = make_aware(start_date)
        end_aware = make_aware(end_date)
        
        #query string filter date 
        dates_filter = Boiler.objects.filter(record_date__gte=start_aware, record_date__lte=end_aware)
        # print(dates_filter)
        
        dates_raw, b_temps, b_return, feeder, cwu_t1, co_t, id_s = [], [], [], [], [], [], []
        
        for record in dates_filter:
            id_s.append(record.pk)
            dates_raw.append(record.record_date)
            b_temps.append(str(record.boiler_temp))
            b_return.append(str(record.boiler_return))
            feeder.append(str(record.feeder))
            cwu_t1.append(str(record.cwu))
            co_t.append(str(record.co))
        
        dates = [str(x.strftime(format='%x %X')) for x in dates_raw]
        
        status = Boiler.objects.all().last()
        
        devices_status = [
            status.co_pomp_status, 
            status.cwu1_pomp_status,
            status.cwu2_pomp_status,
            status.cycle_pomp_status,
            status.feeder_status,
            status.fan_status,
            status.termostat_status
        ]
        data = {
            'dates': dates,
            'boiler_temp': b_temps,
            'boiler_return': b_return,
            'feeder': feeder,
            'cwu': cwu_t1,
            'co': co_t,
            'devices': devices_status
        }
    
        return render(request, 'stats.html', {"data": data})
    
    return JsonResponse({'message': 'No JSON data'})

def burn_settings_view(request):
    if request.method == 'GET':
        current_settings = BurnSettings.objects.all().last()
        settings={
                'set_boiler_temp': current_settings.set_boiler_temp,
                'work_feed': current_settings.work_feed,
                'work_pause': current_settings.work_pause,
                'work_power': current_settings.work_power
            } 
            
    return render(request, 'boiler/burn_settings.html', {'settings': settings})