from datetime import datetime, date, time, timedelta, timezone
from zoneinfo import ZoneInfo
import time as time_module

# ============================================================================
# TOPIC 3: DATE FORMATTING
# ============================================================================

# Example 1: Basic string representation
print("\n1. Different string representations")
now = datetime.now()
print(f"str(): {str(now)}")
print(f"repr(): {repr(now)}")
print(f"isoformat(): {now.isoformat()}")

# Example 2: Using strftime with common formats
print("\n2. Using strftime with common formats")
now = datetime.now()
print(f"Date only (YYYY-MM-DD): {now.strftime('%Y-%m-%d')}")
print(f"Time only (HH:MM:SS): {now.strftime('%H:%M:%S')}")
print(f"Full date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Example 3: Formatting with day and month names
print("\n3. Formatting with day and month names")
now = datetime.now()
print(f"Long format: {now.strftime('%A, %B %d, %Y')}")
print(f"Short format: {now.strftime('%a, %b %d, %y')}")

# Example 4: 12-hour vs 24-hour time format
print("\n4. Time format variations")
now = datetime.now()
print(f"24-hour format: {now.strftime('%H:%M:%S')}")
print(f"12-hour format: {now.strftime('%I:%M:%S %p')}")

# Example 5: Custom separators and formats
print("\n5. Custom formats with separators")
now = datetime.now()
print(f"European format: {now.strftime('%d/%m/%Y')}")
print(f"US format: {now.strftime('%m/%d/%Y')}")
print(f"Database format: {now.strftime('%Y%m%d_%H%M%S')}")

# Example 6: Week number and day of year
print("\n6. Week and day of year information")
now = datetime.now()
print(f"Week number: {now.strftime('%U')}")
print(f"Day of year: {now.strftime('%j')}")
print(f"Day of week (0=Monday): {now.strftime('%w')}")

# Example 7: Formatting with timezone info
print("\n7. Formatting with timezone")
aware_dt = datetime.now(tz=timezone.utc)
print(f"With timezone: {aware_dt.strftime('%Y-%m-%d %H:%M:%S %Z')}")

# Example 8: Multiple date objects formatted for display
print("\n8. Formatting multiple dates in a table")
dates = [date.today() + timedelta(days=i) for i in range(3)]
for d in dates:
    print(f"  {d.strftime('%A')}: {d.strftime('%B %d, %Y')}")

# Example 9: Creating formatted output for logs
print("\n9. Log-style timestamp formatting")
now = datetime.now()
log_timestamp = now.strftime('[%Y-%m-%d %H:%M:%S]')
print(f"{log_timestamp} Application started")

# Example 10: Locale-specific formatting (if available)
print("\n10. ISO format variations")
now = datetime.now()
print(f"ISO format: {now.isoformat()}")
print(f"ISO with timezone: {now.isoformat(timespec='seconds')}")