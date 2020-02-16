import datetime
import sys

from introcs.stdlib import stdio

month = int(sys.argv[1])
day = int(sys.argv[2])
cal_date = datetime.datetime(year=2020, month=month, day=day)

start_date = datetime.datetime(year=2020, month=3, day=20)
end_date = datetime.datetime(year=2020, month=6, day=20)

stdio.writeln(f"2020.{month:02}.{day:02} is {(start_date < cal_date < end_date)}")
