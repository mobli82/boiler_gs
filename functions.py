def date_filter(date):
    if date is None or type(date) is not str:
        raise 'Date value is None'
    
    date = date.replace('T', '-')
    date = date.replace(':', '-')
    
    date_list = date.split('-')
    print(date_list)
    year, month, day, hour, minute = date_list[0], date_list[1], date_list[2], date_list[3], date_list[4]
    
    return int(year), int(month), int(day), int(hour), int(minute) 