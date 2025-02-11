"""-----What will I learn in this project-----
- 1. Understanding the datetime Module
- 2. Working with Dates and Times
- 3. Formatting Dates and Times
- 4. Calculating Time Differences
- 5. Project 20: Event Countdown Timer
"""
# %% 1. Understanding the datetime Module
# Python's DateTime module provides classes to work with dates, times, and durations.
# We have date which represents a calendar, date, year, month, and day.
# We have time which represents time in hours, minutes and seconds.
# And we have date time, which represents both date and time.
# And we have time Delta which represents a duration of difference between two dates or times.

# %% 2. Working with Dates and Times
from datetime import datetime

current_time = datetime.now()
print("Current Date and Time:", current_time)

event_date = datetime(2025, 12, 25, 9, 0, 0)
print("Event Date and Time: ", event_date)

# %% 3. Formatting Dates and Times
from datetime import datetime

current_time = datetime.now()
formatted_time = current_time.strftime("%m-%d-%Y %H:%M:%S")
print("Formatted Time:", formatted_time)

# %% 4. Calculating Time Differences
from datetime import datetime

event_date = datetime(2025, 3, 25)
curreent_date = datetime.now()
time_difference = event_date - curreent_date
print("Days Remaining:", time_difference.days)

# %% 5. Event Countdown Timer
from datetime import datetime, timedelta
import time

# Step 1: Get Event Date and Time from User
def get_event_datetime():
    try:
        date_input = input("Enter the event date (YYYY-MM-DD HH:MM:SS): ")
        return datetime.strptime(date_input, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD HH:MM:SS format.")
        return None

# Step 2: Calculating Time Remaining
def calculate_time_remaining(event_date):
    current_datetime = datetime.now()
    time_difference = event_date - current_datetime
    return time_difference

# Step 3: Display Countdown
def display_countdown(time_left):
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"\nTime Remaining: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds", end="")

# Step 4: Main Countdown Loop
def start_countdown(event_date):
    while True:
        time_left = calculate_time_remaining(event_date)
        if time_left.total_seconds() <= 0:
            print("\nCountdown Complete!")
            break
        display_countdown(time_left)
        time.sleep(1)

# Main Program
event_datetime = get_event_datetime()
if event_datetime:
    print(f"Event set for: {event_datetime}")
    start_countdown(event_datetime)
# %%
