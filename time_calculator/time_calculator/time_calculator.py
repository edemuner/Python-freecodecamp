def add_time(start, duration, weekday=None):
    spl_start = hour_splitter(start)
    spl_duration = hour_splitter(duration)

    minutes_sum = minutes_incrementer(spl_start[2], spl_duration[1])
    hours_sum = hour_incrementer(spl_start[0], spl_start[1], spl_duration[0], minutes_sum[0])

    final_minutes = minutes_sum[1]
    final_hours = hours_sum[1]
    final_days = hours_sum[0]

    if final_hours >= 12:
        half = "PM"
        final_hours -= 12 if final_hours > 12 else 0
    else:
        half = "AM"

    if final_hours == 0: final_hours = 12

    if final_days > 0:
        newtime = f'{final_hours}:{final_minutes:02d} {half}'
        newtime += weekday_selector(weekday, final_days)
        newtime += f' (next day)' if final_days == 1 else f' ({final_days} days later)'
    else:
        newtime = f'{final_hours}:{final_minutes:02d} {half}'
        newtime += weekday_selector(weekday, final_days)

    return newtime


# essa função lida com string de tempo nos dois formatos recebidos em add_time
# retorna 2 ou 3 valores, conforme seja no formato "start" ou "duration""
# sendo "start", o índice 0 é o AM/PM, seguido de horas e minutos
# em "duration", 0 e 1 são horas e minutos
def hour_splitter(time):
    splitted_time = []
    if "AM" in time.upper() or "PM" in time.upper():
        time, half = time.upper().split()
        splitted_time.append(half)
    hour, minute = time.split(":")
    splitted_time.append(int(hour))
    splitted_time.append(int(minute))
    return splitted_time


# essa função faz o incremento dos minutos, devolvendo uma lista com as horas e minutos
def minutes_incrementer(v1, v2):
    hour = 0
    minute = v1
    for i in range(v2):
        if minute == 59:
            minute = 0
            hour += 1
            continue
        minute += 1
    return [hour, minute]


def hour_incrementer(half, hours, duration_hours, hours_from_minutes):
    days = 0
    if half == "PM":
        hours += 12
    for i in range(duration_hours):
        if hours == 24:
            hours = 0
            days += 1
        hours += 1
    for i in range(hours_from_minutes):
        hours += 1
        if hours == 24:
            hours = 0
            days += 1
    return [days, hours]


def weekday_selector(weekday, days_passed):
    if weekday is not None:
        index = 0
        week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for i in week:
            if weekday.lower() == i.lower():
                index = week.index(i)
        for i in range(days_passed):
            if index == 6:
                index = -1
            index += 1
        return f', {week[index]}'
    else:
        return ''


# print(add_time("3:30 PM", "1:35"))

# print(add_time("10:00 PM", "3:00", "Monday"))

print(add_time("11:59 PM", "24:05"))
