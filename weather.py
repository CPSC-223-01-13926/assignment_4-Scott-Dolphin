from calendar import month_name, day_name
import json

"""
- opens @filename in read mode and returns a dictionary of the JSON decoded contents
- Returns an empty dictionary if the @filename is not found.

@param filename: accepts the name of a file to read from
"""
def read_data(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return{}

"""
- Opens @filename in write mode and writes the dictionary data into the file encoded as JSON

@param filename: accepts the name of a file to write to
@param data: the data that will be written to the file
"""
def write_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

"""
- Returns the maximum temperature for all dictionary data where the key contains the date as YYMMDD.

@param data: the dictionary to be read from
@param date: the date of the dictionary
@key 't': temperature as integer
"""
def max_temperature(data, date):
    x = 0
    for key in data:
        if date == key[0:8]:
            if data[key]['t'] > x:
                x = data[key]['t']
    return x

def min_temperature(data, date):
    x = 999999
    for key in data:
        if date == key[0:8]:
            if  data[key]['t'] < x:
                x = data[key]['t']
    return x


def max_humidity(data, date):
    x = 0
    for key in data:
        if date == key[0:8]:
            if data[key]['h'] > x:
                x = data[key]['h']
    return x

def min_humidity(data, date):
    x = 99999
    for key in data:
        if date == key[0:8]:
            if data[key]['h'] < x:
                x = data[key]['h']
    return x

def tot_rain(data, date):
    x = 0
    for key in data:
        if date == key[0:8]:
            x += data[key]['r']
    return x

def report_daily(data, date):
    display = "========================= DAILY REPORT ========================\n"
    display = display + "Date                      Time  Temperature  Humidity  Rainfall\n"
    display = display + "====================  ========  ===========  ========  ======== \n"
    for key in data:
        if date == key[0:8]:
            m = month_name[int(date[4:6])] + " " + day_name[int(date[7:8])] + "," + str(int(date[0:4]))
            tm = key[8:10] + ":" + key[10:12] + ":" + key[12:14]
            t = data[key]['t']
            h = data[key]['h']
            r = data[key]['r']
            rain = '{:.2f}'.format(r)
    display = display + f'{m:22}{tm:8}{t:13}{h:10}{rain:10}'+ '\n'
    return display

def report_historical(data):

    display = (
        "============================== HISTORICAL REPORT ===========================\n"
    )
    display = (
        display
        + "                          Minimum      Maximum   Minumum   Maximum     Total\n"
    )
    display = (
        display
        + "Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n"
    )
    display = (
        display
        + "====================  ===========  ===========  ========  ========  ========\n"
    )

    d = ""
    for key in data:
        if d == key[0:8]:
            continue
        else:
            d = key[0:8]

            m = (
                month_name[int(d[4:6])]
                + " "
                + str(int(d[6:8]))
                + ", "
                + str(int(d[0:4]))
            )

            min_temp = min_temperature(data=data, date=d)
            max_temp = max_temperature(data=data, date=d)
            min_hum = min_humidity(data=data, date=d)
            max_hum = max_humidity(data=data, date=d)
            rain = tot_rain(data=data, date=d)
            display = (
                display
                + f"{m:20}{min_temp:13}{max_temp:13}{min_hum:10}{max_hum:10}{rain:10.2f}"
                + "\n"
            )

    return display