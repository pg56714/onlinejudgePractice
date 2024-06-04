def check_school_time(hh, mm):
    start_hour, start_minute = 7, 30
    end_hour, end_minute = 17, 0

    now_minutes = hh * 60 + mm
    start_minutes = start_hour * 60 + start_minute
    end_minutes = end_hour * 60 + end_minute

    if start_minutes <= now_minutes < end_minutes:
        return 1
    else:
        return 0


hh, mm = map(int, input().split())

print(check_school_time(hh, mm))
