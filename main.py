import pandas as pd
import datetime
import json
import io
import numpy as np

maxDaysShedule = 60
shedule_resource = []

def generateRecourceQuote(maxDaysShedule, maskWP, maskWN, duration,timeAvail, timeUnavail, comment):
    dateAvail = []
    dateUnavail = []
    startDate = datetime.datetime.now()
    toDate = startDate + datetime.timedelta(days=maxDaysShedule)
    # generate appointment dates
    dateAvail = pd.bdate_range(startDate, toDate, freq='C', weekmask=maskWP, holidays=None).strftime("%Y-%m-%dT%H:%M:%S.000Z").tolist()
    dateUnavail = pd.bdate_range(startDate, toDate, freq='C', weekmask=maskWN, holidays=None).strftime("%Y-%m-%dT%H:%M:%S.000Z").tolist()


    for da in dateAvail:
        print(da)
        for i in timeAvail:
            genDayQuote(i[0][0], i[1][0], duration, True, '')
        if da in dateUnavail:
            for j in timeUnavail: genDayQuote(j[0][0], j[1][0], 0, False, comment)


def genDayQuote(timeFrom, timeTo, duration, avail, comment):
    if duration > 0:
        frqnc = str(duration) + 'min'
        print(pd.date_range(timeFrom, timeTo, freq=frqnc, closed='left').strftime('%H:%M').tolist())
    else: print(f'{timeFrom} - {timeTo} - {comment}')
  #  time_quote = pd.date_range(timeFrom, timeTo, freq=frqnc).strftime('%H:%M').tolist()
#   shedule_resource.append({'sheduleDate': dayS})
#   shedule_resource.append({'timeQuotes': time_quote})


startDate = datetime.datetime.now()
toDate = startDate + datetime.timedelta(days=62)

# business days list for shedule
dateRange = pd.bdate_range(startDate, toDate, freq='C', weekmask='1100000', holidays=None)
dateRangeList = dateRange.strftime("%Y-%m-%dT%H:%M:%S.000Z").tolist()

shedule = {
    'resourceId': 1234567,
    'doctorId': 667660,
    'doctorName': 'Григорьева Г.Г.',
    'specialityId': 54321,
    'specialityName': 'Терапевт',
    'lpuId': 56391,
    'lpuName': 'ГП № 128',
    'lpuFromTime': '10:00',
    'lpuToTime': '20:00',
    'cabNum': '110'}


with open('shedule_new.json', 'w') as f:
    json_data = json.dumps(shedule)
    f.write(json_data)

#   Григорьева Г.Г.Терапевт
maskWP = '1101000'
maskWN = '1000000'
timeAvail = [(['10:00'], ['14:00']), (['15:00'], ['20:00'])]
timeUnavail = [(['14:00'], ['15:00'])]
comment = 'Врач не работает'
duration = 30
generateRecourceQuote(maxDaysShedule, maskWP, maskWN, duration,timeAvail, timeUnavail, comment)

#   Константинова-Щедрина А.А.Офтальмолог
maskWP = '0111110'
maskWN = '0100000'
timeAvail = [(['09:00'], ['21:00'])]
timeUnavail = [(['09:00'], ['21:00'])]
comment = 'Врач не принимает'
duration = 30
generateRecourceQuote(maxDaysShedule, maskWP, maskWN, duration,timeAvail, timeUnavail, comment)


