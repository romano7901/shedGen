import pandas as pd
import datetime
import json


maxDaysShedule = 60
shedule_all = []
shedule_resource = []

# Generate quotes for all days by week masks and time intervals
def generateRecourceQuote(maxDaysShedule, maskWP, maskWN, duration,timeAvail, timeUnavail, comment):
    dateAvail = []
    dateUnavail = []

    startDate = datetime.datetime.now()
    toDate = startDate + datetime.timedelta(days=maxDaysShedule)
    # generate appointment dates
    dateAvail = pd.bdate_range(startDate, toDate, freq='C', weekmask=maskWP, holidays=None).strftime("%Y-%m-%dT%H:%M:%S.000Z").tolist()
    dateUnavail = pd.bdate_range(startDate, toDate, freq='C', weekmask=maskWN, holidays=None).strftime("%Y-%m-%dT%H:%M:%S.000Z").tolist()


    for da in dateAvail:

        time_quotes = []
        # print(da)
        for i in timeAvail:
            genDayQuote(i[0][0], i[1][0], duration, True, '', time_quotes)
        if da in dateUnavail:
            for j in timeUnavail: genDayQuote(j[0][0], j[1][0], 0, False, comment, time_quotes)
        #print(time_quotes)
        shedule_resource_date = {
            'sheduleDate': da,
            'time_quotes': time_quotes
        }
        shedule_resource.append(shedule_resource_date)

# Generate  time intervals
def genDayQuote(timeStart, timeEnd, duration, avail, comment , time_quotes):
    time_slot = {}
    if avail:
        frqnc = str(duration) + 'min'
        timeList = pd.date_range(timeStart, timeEnd, freq=frqnc).strftime('%H:%M').tolist()
        for i in  range(len(timeList)-1):
            time_slot = {'timeFrom': timeList[i], 'timeTo': timeList[i+1], 'apointment': avail, 'quoteStatus': 'Принимает', 'patients':[]}
            time_quotes.append(time_slot)
    else:
        time_slot = {'timeFrom': timeStart, 'timeTo':timeEnd, 'apointment': avail,'quoteStatus': comment, 'patients': []}
        time_quotes.append(time_slot)

#   Григорьева Г.Г.Терапевт
maskWP = '1111100'
maskWN = '1111100'
timeAvail = [(['10:00'], ['14:00']), (['15:00'], ['20:00'])]
timeUnavail = [(['14:00'], ['15:00'])]
comment = 'Врач не работает'
duration = 30
shedule_resource = []
generateRecourceQuote(maxDaysShedule, maskWP, maskWN, duration, timeAvail, timeUnavail, comment)
shedule_resource_main = {
    'resourceId': 1234567,
    'doctorId': 667660,
    'doctorName': 'Григорьева Г.Г.',
    'specialityId': 54321,
    'specialityName': 'Терапевт',
    'lpuId': 56391,
    'lpuName': 'ГП № 128',
    'lpuFromTime': '10:00',
    'lpuToTime': '20:00',
    'cabNum': '110',
    'sheduleList': shedule_resource}

shedule_all.append(shedule_resource_main)

#   Константинова-Щедрина А.А.Офтальмолог
maskWP = '0111110'
maskWN = '0100000'
timeAvail = [(['09:00'], ['21:00'])]
timeUnavail = [(['09:00'], ['12:00'])]
comment = 'Не принимает'
duration = 30
shedule_resource = []
generateRecourceQuote(maxDaysShedule, maskWP, maskWN, duration,timeAvail, timeUnavail, comment)
shedule_resource_main = {
    'resourceId': 5554567,
    'doctorId': 6655660,
    'doctorName': 'Константинова-Щедрина А.А.',
    'specialityId': 55667788,
    'specialityName': 'Офтальмолог',
    'lpuId': 56391,
    'lpuName': 'ГП № 128',
    'lpuFromTime': '09:00',
    'lpuToTime': '21:00',
    'cabNum': '150',
    'sheduleList': shedule_resource}

shedule_all.append(shedule_resource_main)


with open('shedule_new.json', 'w') as f:
    json_data = json.dumps(shedule_all)
    f.write(json_data)


