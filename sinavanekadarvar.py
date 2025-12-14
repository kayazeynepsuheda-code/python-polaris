from datetime import datetime, date,time,timedelta
now=datetime.now()
exam_day=datetime(2025,12,18,19,30)
rtime=exam_day-now
print(f"Remaining time: {rtime}")