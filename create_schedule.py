from ics import Calendar, Event
from datetime import datetime, timedelta
import pytz

def create_event(day, start_time, end_time, description, tz):
    """Creates an event for the calendar."""
    event = Event()
    event.name = description
    start_datetime = datetime.strptime(f'{day} {start_time}', '%Y-%m-%d %H:%M')
    end_datetime = datetime.strptime(f'{day} {end_time}', '%Y-%m-%d %H:%M')
    # Localize the datetime objects with the specified timezone
    start_datetime = tz.localize(start_datetime)
    end_datetime = tz.localize(end_datetime)
    event.begin = start_datetime
    event.end = end_datetime
    return event

# Create a new calendar
cal = Calendar()

# Define your time zone (change 'America/New_York' to your time zone)
time_zone = pytz.timezone('America/New_York')

# Define your work week (Monday to Saturday)
work_days = [datetime(2023, 11, 27) + timedelta(days=i) for i in range(6)]  # Example week starting from 2023-11-27

# Define the time slots for your tasks
time_slots = [
    ('08:00', '10:00', 'High-priority tasks (VCA Model or Proposal Writing)'),
    ('10:00', '12:00', 'Continue high-priority work or Teaching Preparation'),
    ('13:00', '15:00', 'Work on GatorBrain or HeadNeck projects'),
    ('15:00', '17:00', 'Continue with ongoing tasks or Interpretable AI project'),
    ('18:00', '20:00', 'Resume work with less intense concentration'),
    ('20:00', '22:00', 'Wrap up and prepare for the next day')
]

# Add events to the calendar for each work day
for day in work_days:
    day_str = day.strftime('%Y-%m-%d')
    for start, end, desc in time_slots:
        event = create_event(day_str, start, end, desc, time_zone)
        cal.events.add(event)

# Save the calendar to an .ics file
file_name = 'Custom_Work_Schedule.ics'
with open(file_name, 'w') as f:
    f.writelines(cal)

print(f"Calendar file '{file_name}' created successfully.")
