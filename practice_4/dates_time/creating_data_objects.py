from datetime import datetime, date, time, timedelta, timezone
from zoneinfo import ZoneInfo
import time as time_module

# ============================================================================
# TOPIC 2: CREATING DATE OBJECTS
# ============================================================================

# Example 1: Creating a date object manually
print("\n1. Creating a date object (year, month, day)")
specific_date = date(2024, 12, 25)
print(f"Christmas 2024: {specific_date}")


# Example 2: Creating a datetime object manually
print("\n2. Creating a datetime object with date and time")
specific_datetime = datetime(2024, 12, 25, 18, 30, 45)
print(f"Christmas evening: {specific_datetime}")


# Example 3: Creating a time object manually
print("\n3. Creating a time object (hour, minute, second)")
specific_time = time(14, 30, 0)
print(f"Time: {specific_time}")


# Example 4: Creating datetime with microseconds
print("\n4. Creating datetime with microseconds")
precise_datetime = datetime(2024, 6, 15, 12, 30, 45, 123456)
print(f"Precise datetime: {precise_datetime}")


# Example 5: Creating date from timestamp
print("\n5. Creating datetime from Unix timestamp")
timestamp = 1609459200  # 2021-01-01 00:00:00
dt_from_timestamp = datetime.fromtimestamp(timestamp)
print(f"From timestamp {timestamp}: {dt_from_timestamp}")


# Example 6: Creating date from ISO format string
print("\n6. Creating datetime from ISO format string")
iso_string = "2024-06-15T14:30:00"
dt_from_iso = datetime.fromisoformat(iso_string)
print(f"From ISO string: {dt_from_iso}")


# Example 7: Creating date from string with strptime
print("\n7. Creating datetime from custom string format")
date_string = "15/06/2024"
dt_from_string = datetime.strptime(date_string, "%d/%m/%Y")
print(f"From string '15/06/2024': {dt_from_string}")


# Example 8: Creating multiple dates in a loop
print("\n8. Creating dates for a week")
start_date = date(2024, 6, 10)
for i in range(7):
    current = start_date + timedelta(days=i)
    print(f"Day {i+1}: {current}")


# Example 9: Creating datetime with timezone awareness
print("\n9. Creating timezone-aware datetime")
aware_dt = datetime(2024, 6, 15, 14, 30, 0, tzinfo=timezone.utc)
print(f"UTC aware: {aware_dt}")


# Example 10: Min and max date objects
print("\n10. Date object limits")
print(f"Minimum date: {date.min}")
print(f"Maximum date: {date.max}")