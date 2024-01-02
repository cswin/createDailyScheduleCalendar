from icalendar import Calendar, Event, Alarm
from datetime import datetime, timedelta
import pytz

def create_event(day, start_time, end_time, description, tz, reminder_minutes=15):
    """Creates an event for the calendar and adds a reminder."""
    event = Event()
    event.add('summary', description)

    # Parse the datetime and adjust for timezone
    start_datetime = tz.localize(datetime.strptime(f'{day} {start_time}', '%Y-%m-%d %H:%M'))
    end_datetime = tz.localize(datetime.strptime(f'{day} {end_time}', '%Y-%m-%d %H:%M'))
    event.add('dtstart', start_datetime)
    event.add('dtend', end_datetime)

    # Add an alarm to the event
    alarm = Alarm()
    alarm.add("action", "DISPLAY")
    alarm.add('description', f'Reminder for {description}')
    alarm.add("trigger", timedelta(minutes=-reminder_minutes))
    event.add_component(alarm)

    return event

# Create a new calendar
cal = Calendar()

# Define your time zone
time_zone = pytz.timezone('America/New_York')

# Define your work week (Monday to Saturday)
start_date = datetime(2024, 1, 1)
work_days = [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7)]

# Define the detailed tasks for each time slot
detailed_tasks = {
    '08:00-10:00': {
        'Monday': 'VCA',
        'Tuesday': 'VCA',#Proposal Writing - Modulating Striatal-Amygdala Pathway
        'Wednesday': 'VCA',
        'Thursday': 'VCA',
        'Friday': 'VCA',
        'Saturday': 'Social Perception',
        'Sunday': 'Interpretable AI Research'
    },
    '10:15-12:00': {
        'Monday': 'GatorBrain',
        'Tuesday': 'GatorBrain',#HeadNeck Outcome
        'Wednesday': 'GatorBrain',
        'Thursday': 'GatorBrain',
        'Friday': 'GatorBrain',#Interpretable AI Research
        'Saturday': 'Social Perception',
        'Sunday': 'Interpretable AI Research'
    },
    '13:00-15:00': {
        'Monday': 'Teaching',
        'Tuesday': 'Teaching',
        'Wednesday': 'Teaching',
        'Thursday': 'Teaching',
        'Friday': 'Teaching',
        'Saturday': 'Social Perception',
        'Sunday': 'Interpretable AI Research'
    },
    '15:15-17:00': {
        'Monday': 'VCA',
        'Tuesday': 'GatorBrain',
        'Wednesday': 'VCA',
        'Thursday': 'GatorBrain',
        'Friday': 'VCA',
        'Saturday': 'Social Perception',
        'Sunday': 'Interpretable AI Research'
    },
    '18:00-20:00': {
        'Monday': 'Teaching',
        'Tuesday': 'Teaching',
        'Wednesday': 'Teaching',
        'Thursday': 'CBCT',
        'Friday': 'HeadNeck Outcome',
        'Saturday': 'Light Reading & Writing',
        'Sunday': 'Light Reading & Writing'
    },
    '20:15-22:00': {
        'Monday': 'CBCT',
        'Tuesday': 'HeadNeck Outcome',
        'Wednesday': 'CBCT',
        'Thursday': 'CBCT',
        'Friday': 'HeadNeck Outcome',
        'Saturday': 'HeadNeck Outcome',
        'Sunday': 'CBCT'
    },
    '22:15-23:45': {
        'Monday': 'CBCT',
        'Tuesday': 'HeadNeck Outcome',
        'Wednesday': 'CBCT',
        'Thursday': 'Social Perception',
        'Friday': 'Interpretable AI Research',
        'Saturday': 'HeadNeck Outcome',
        'Sunday': 'Light Reading & Writing'
    }
}
# Add events to the calendar for each time slot and work day
for day, day_str in zip(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday'], work_days):
    for time_slot, tasks in detailed_tasks.items():
        start_time, end_time = time_slot.split('-')
        description = tasks.get(day, 'General Work')
        event = create_event(day_str, start_time, end_time, description, time_zone,  reminder_minutes=15)
        cal.add_component(event)

# Save the calendar to an .ics file
file_name = 'Custom_Work_Schedule.ics'
with open(file_name, 'wb') as f:
    f.write(cal.to_ical())

print(f"Calendar file '{file_name}' created successfully.")