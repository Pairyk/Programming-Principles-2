from datetime import datetime, date, time, timedelta, timezone
from zoneinfo import ZoneInfo
import time as time_module

# ============================================================================
# TOPIC 1: DATETIME MODULE
# ============================================================================

# Example 1: Importing and understanding datetime components
print("\n1. datetime module components")
print(f"datetime class: {datetime}")
print(f"date class: {date}")
print(f"time class: {time}")
print(f"timedelta class: {timedelta}")


# Example 2: Getting current date and time
print("\n2. Getting current date and time")
now = datetime.now()
print(f"Current datetime: {now}")
print(f"Type: {type(now)}")


# Example 3: Getting current date only
print("\n3. Getting current date")
today = date.today()
print(f"Today's date: {today}")
print(f"Type: {type(today)}")


# Example 4: Getting current time only
print("\n4. Getting current time")
current_time = datetime.now().time()
print(f"Current time: {current_time}")
print(f"Type: {type(current_time)}")


# Example 5: UTC (Coordinated Universal Time)
print("\n5. Getting current UTC datetime")
utc_now = datetime.utcnow()
print(f"UTC now: {utc_now}")


# Example 6: Accessing datetime components
print("\n6. Accessing datetime components")
now = datetime.now()
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")
print(f"Second: {now.second}")
print(f"Microsecond: {now.microsecond}")


# Example 7: Accessing date components
print("\n7. Accessing date components")
today = date.today()
print(f"Weekday (0=Monday): {today.weekday()}")
print(f"ISO Calendar: {today.isocalendar()}")


# Example 8: Accessing time components
print("\n8. Accessing time components")
current_time = datetime.now().time()
print(f"Hour: {current_time.hour}")
print(f"Minute: {current_time.minute}")
print(f"Second: {current_time.second}")