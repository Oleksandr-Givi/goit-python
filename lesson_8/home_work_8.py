from datetime import datetime, date
import calendar


def next_week_congratulate(users):

    m = []
    t = []
    w = []
    th = []
    f = []

    next_week = []
    present_day = datetime(year=2022, month=4, day=15) #datetime.now()
    week_day = present_day.weekday()
    num = calendar.monthrange(present_day.year, present_day.month)
    num_1 = num[1]
    if week_day == 0:
        n = -2
    else:
        n = 6- week_day-1

    for i in range(7):
        if present_day.day + i + n <= num_1:
            next_week.append(datetime(year = present_day.year, month = present_day.month,
        day = (present_day.day+i+n)))
        else:
            
           next_week.append(datetime(year = present_day.year, month = present_day.month + 1,
        day = (present_day.day+i+n-num_1)))
    
    for data in next_week:
        days = data.day
        mon = data.month
        for person in users:
            days_person = person['birthday'].day
            month_person = person['birthday'].month
            if mon == month_person and days == days_person:
                if data.weekday() == 5 or data.weekday() == 6 or data.weekday() == 0:
                    m += [person['name']]
                elif data.weekday() == 1:
                    t += [person['name']]
                elif data.weekday() == 2:
                    w += [person['name']]
                elif data.weekday() == 3:
                    th += [person['name']]
                elif data.weekday() == 4:
                    f += [person['name']]

    if len(m)>0:
        print("Monday:", ', '.join(m))
    if len(t)>0:
        print("Tuesday:", ', '.join(t))
    if len(w)>0:
        print("Wednesday:", ', '.join(w))
    if len(th)>0:
        print("Thursday:", ', '.join(th))
    if len(f)>0:
        print("Friday:", ', '.join(f))
    


users = [
        {"name":"Alex", "birthday":datetime(year=1980, month=5, day=1)},
        {"name":"Olya", "birthday":datetime(year=1983, month=4, day=20)},
        {"name":"Misha", "birthday":datetime(year=1985, month=4, day=16)},
        {"name":"Givi", "birthday":datetime(year=1990, month=4, day=17)},
        {"name":"Marry", "birthday":datetime(year=1995, month=4, day=18)},
        {"name":"Luda", "birthday":datetime(year=2000, month=4, day=19)},
        {"name":"Tanya", "birthday":datetime(year=2005, month=4, day=21)},
        {"name":"Anna", "birthday":datetime(year=2011, month=4, day=22)}
    ]

   
    
next_week_congratulate(users)