"""
Write a function named `add_time` that takes in two required parameters and one optional parameter:
* a start time in the 12-hour clock format (ending in AM or PM) 
* a duration time that indicates the number of hours and minutes
* (optional) a starting day of the week, case insensitive

The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show `(next day)` after the time. If the result will be more than one day later, it should show `(n days later)` after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.
```py
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
```

Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.

RULES: https://replit.com/github/freeCodeCamp/boilerplate-time-calculator
"""


def add_time(start, duration, weekday=None):
    
    # essa sequência de chamadas e atribuições organiza os dados recebidos e realiza a soma das horas, minutos e dias
    # para isso faz uso das funções definidas mais abaixo, que funcionam como sub-rotinas
    spl_start = hour_splitter(start)
    spl_duration = hour_splitter(duration)

    minutes_sum = minutes_incrementer(spl_start[2], spl_duration[1])
    hours_sum = hour_incrementer(spl_start[0], spl_start[1], spl_duration[0], minutes_sum[0])

    final_minutes = minutes_sum[1]
    final_hours = hours_sum[1]
    final_days = hours_sum[0]

    # abaixo é realizada a formatação final da string
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


# essa função organiza strings de tempo nos dois formatos recebidos em add_time
# retorna 2 ou 3 valores, conforme a entrada lide com "start" ou "duration""
# sendo "start", o índice [0] é o AM/PM, seguido de [1]: horas e [2]:minutos
# em "duration", 0 e 1 são horas e minutos
def hour_splitter(time):
    splitted_time = []
    if "AM" in time.upper() or "PM" in time.upper():
        time, half = time.upper().split()
        # half é o AM/PM, time é a hora
        splitted_time.append(half)
    hour, minute = time.split(":")
    splitted_time.append(int(hour))
    splitted_time.append(int(minute))
    return splitted_time


# essa função faz o incremento dos minutos, devolvendo uma lista com as horas e minutos que resultam da soma de todos os minutos
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

# essa função recebe todas as horas (do horário do dia recebido por add_time, de duration, e a somatória resultante dos minutos)
# trabalha em conjunto com half para devolver uma lista com os dias decorridos e o horário do dia onde se chega

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
