from datetime import datetime, date, time, timedelta, timezone
from zoneinfo import ZoneInfo
import time as time_module

# ============================================================================
# TOPIC 4: CALCULATING TIME DIFFERENCES
# ============================================================================

# Example 1: Creating timedelta objects
print("\n1. Creating timedelta objects")
delta1 = timedelta(days=5)
delta2 = timedelta(hours=3)
delta3 = timedelta(minutes=30)
print(f"5 days: {delta1}")
print(f"3 hours: {delta2}")
print(f"30 minutes: {delta3}")

# Example 2: Combining timedelta components
print("\n2. Combining multiple timedelta components")
combined_delta = timedelta(days=7, hours=2, minutes=30, seconds=45)
print(f"7 days, 2 hours, 30 minutes, 45 seconds: {combined_delta}")
print(f"Total seconds: {combined_delta.total_seconds()}")

# Example 3: Subtracting dates to get timedelta
print("\n3. Calculating difference between two dates")
start_date = date(2024, 1, 1)
end_date = date(2024, 12, 31)
difference = end_date - start_date
print(f"From {start_date} to {end_date}: {difference}")
print(f"Days: {difference.days}")

# Example 4: Subtracting datetimes (more precise)
print("\n4. Calculating difference between two datetimes")
start_time = datetime(2024, 6, 15, 10, 0, 0)
end_time = datetime(2024, 6, 15, 14, 30, 45)
time_diff = end_time - start_time
print(f"From {start_time} to {end_time}:")
print(f"Total difference: {time_diff}")
print(f"Hours: {time_diff.total_seconds() / 3600}")

# Example 5: Adding time to a date
print("\n5. Adding time to a date")
today = date.today()
future_date = today + timedelta(days=30)
print(f"Today: {today}")
print(f"30 days from now: {future_date}")

# Example 6: Subtracting time from a date
print("\n6. Subtracting time from a date")
today = date.today()
past_date = today - timedelta(weeks=2)
print(f"Today: {today}")
print(f"2 weeks ago: {past_date}")

# Example 7: Calculating age from birth date
print("\n7. Calculating age from birth date")
birth_date = date(1990, 5, 15)
today = date.today()
age_delta = today - birth_date
age_years = age_delta.days // 365
print(f"Birth date: {birth_date}")
print(f"Today: {today}")
print(f"Approximate age: {age_years} years")

# Example 8: Calculating remaining days until event
print("\n8. Calculating days until next birthday")
today = date.today()
next_birthday = date(today.year, 12, 25)  # Christmas
if next_birthday < today:
    next_birthday = date(today.year + 1, 12, 25)
days_until = (next_birthday - today).days
print(f"Days until Christmas: {days_until}")

# Example 9: Working with timedelta arithmetic
print("\n9. Timedelta arithmetic")
delta1 = timedelta(days=5, hours=3)
delta2 = timedelta(days=2, hours=1)
sum_delta = delta1 + delta2
diff_delta = delta1 - delta2
print(f"Delta1: {delta1}")
print(f"Delta2: {delta2}")
print(f"Sum: {sum_delta}")
print(f"Difference: {diff_delta}")

# Example 10: Measuring execution time
print("\n10. Measuring code execution time")
start_time = datetime.now()
total = sum(range(1000000))
end_time = datetime.now()
execution_time = end_time - start_time
print(f"Sum calculation took: {execution_time.total_seconds()} seconds")