from datetime import datetime, date, time, timedelta, timezone
from zoneinfo import ZoneInfo
import time as time_module

# ============================================================================
# TOPIC 5: WORKING WITH TIMEZONES
# ============================================================================

# Example 1: UTC timezone
print("\n1. Working with UTC timezone")
utc_time = datetime.now(tz=timezone.utc)
print(f"Current UTC time: {utc_time}")
print(f"Timezone info: {utc_time.tzinfo}")

# Example 2: Fixed offset timezone (UTC+5:30)
print("\n2. Creating fixed offset timezone")
ist = timezone(timedelta(hours=5, minutes=30))  # India Standard Time
ist_time = datetime.now(tz=ist)
print(f"IST time: {ist_time}")

# Example 3: Fixed offset timezone (UTC-5:00)
print("\n3. Creating different fixed offset timezone")
est = timezone(timedelta(hours=-5))  # Eastern Standard Time
est_time = datetime.now(tz=est)
print(f"EST time: {est_time}")

# Example 4: Using ZoneInfo for named timezones
print("\n4. Using named timezones with ZoneInfo")
try:
    ny_tz = ZoneInfo("America/New_York")
    ny_time = datetime.now(tz=ny_tz)
    print(f"New York time: {ny_time}")
except:
    print("ZoneInfo not available in this environment")

# Example 5: Using multiple named timezones
print("\n5. Time in different cities")
try:
    timezones = {
        "New York": "America/New_York",
        "London": "Europe/London",
        "Tokyo": "Asia/Tokyo",
        "Sydney": "Australia/Sydney"
    }
    for city, tz_name in timezones.items():
        tz = ZoneInfo(tz_name)
        local_time = datetime.now(tz=tz)
        print(f"{city}: {local_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
except:
    print("ZoneInfo not fully available")

# Example 6: Converting between timezones
print("\n6. Converting time from one timezone to another")
utc_time = datetime(2024, 6, 15, 12, 0, 0, tzinfo=timezone.utc)
print(f"UTC time: {utc_time}")

ist = timezone(timedelta(hours=5, minutes=30))
ist_time = utc_time.astimezone(ist)
print(f"Converted to IST: {ist_time}")

# Example 7: Aware vs naive datetime
print("\n7. Aware vs naive datetime objects")
naive_dt = datetime(2024, 6, 15, 14, 30, 0)
aware_dt = datetime(2024, 6, 15, 14, 30, 0, tzinfo=timezone.utc)
print(f"Naive datetime: {naive_dt}")
print(f"Naive tzinfo: {naive_dt.tzinfo}")
print(f"Aware datetime: {aware_dt}")
print(f"Aware tzinfo: {aware_dt.tzinfo}")

# Example 8: Making naive datetime timezone-aware
print("\n8. Converting naive to aware datetime")
naive_dt = datetime.now()
print(f"Naive: {naive_dt}")

aware_dt = naive_dt.replace(tzinfo=timezone.utc)
print(f"Made aware (UTC): {aware_dt}")

# Example 9: Getting timezone offset
print("\n9. Getting timezone offset information")
aware_dt = datetime.now(tz=timezone.utc)
offset = aware_dt.utcoffset()
print(f"UTC offset: {offset}")

ist = timezone(timedelta(hours=5, minutes=30))
ist_dt = datetime.now(tz=ist)
print(f"IST offset: {ist_dt.utcoffset()}")

# Example 10: DST (Daylight Saving Time) handling
print("\n10. Timezone information and DST")
try:
    ny_tz = ZoneInfo("America/New_York")
    summer = datetime(2024, 7, 15, 12, 0, tzinfo=ny_tz)
    winter = datetime(2024, 1, 15, 12, 0, tzinfo=ny_tz)
    print(f"Summer (July): {summer.strftime('%Y-%m-%d %H:%M %Z %z')}")
    print(f"Winter (January): {winter.strftime('%Y-%m-%d %H:%M %Z %z')}")
except:
    print("ZoneInfo not available for DST demonstration")