import utime

def get_timetable_day(start_dates):
    """
    For STC's timetable, it will use the start_dates information to determine the timetable day number for the current day (0-indexed).
    """
    now = utime.localtime()
    current_date = now[0:3]  # (year, month, day)
    current_sec = utime.mktime(now)
    print("Today's date",current_date)
    
    # Find most recent start date
    last_start_day = None
    last_start_cycle = 0
    
    for date_key in sorted(start_dates.keys(), reverse=True):
        term_start = utime.mktime(date_key + (0, 0, 0, 0, 0))
        if term_start <= current_sec:
            last_start_day = date_key
            last_start_cycle = start_dates[date_key]
            break
    
    if last_start_day is None:
        return 0  # Default to Day 0 if before all terms
    
    print("Last start day",last_start_day,"day number",last_start_cycle)
    
    # Calculate elapsed school days (excluding weekends)
    elapsed_days = 0
    day_sec = utime.mktime(last_start_day + (16, 0, 0, 0, 0)) # 4pm switch to the next day
    
    while day_sec < current_sec:
        weekday = utime.localtime(day_sec)[6]  # 0=Mon, 6=Sun
        if weekday < 5:  # Monday-Friday
            elapsed_days += 1
        day_sec += 86400  # Add one day
    print("Elapsed days:",elapsed_days)
    # Calculate current cycle day (0-9)
    return (last_start_cycle + elapsed_days) % 10

