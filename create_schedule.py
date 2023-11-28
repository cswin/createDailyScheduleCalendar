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
start_date = datetime(2023, 11, 28)
work_days = [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(6)]


# Define the detailed tasks for each time slot
detailed_tasks = {
    '08:00-10:00': {
        'Monday': 'VCA Model Development ',
        'Tuesday': 'Proposal Writing - Modulating Striatal-Amygdala Pathway',
        'Wednesday': 'VCA Model Development ',
        'Thursday': 'Proposal Writing - Modulating Striatal-Amygdala Pathway',
        'Friday': 'Teaching Preparation  - Content Review and Interactive Elements',
        'Saturday': 'GatorBrain Project '
    },
    '10:00-12:00': {
        'Monday': 'GatorBrain Project - Research and Collaboration Meetings',
        'Tuesday': 'HeadNeck Outcome ',
        'Wednesday': 'GatorBrain Project ',
        'Thursday': 'HeadNeck Outcome - Data Analysis and Report Drafting',
        'Friday': 'Interpretable AI Research - Literature Review and Testing',
        'Saturday': 'HeadNeck CBCT - Development'
    },
    '13:00-15:00': {
        'Monday': 'Teaching Preparation - Content Review and Interactive Elements',
        'Tuesday': 'VCA Model Development',
        'Wednesday': 'Teaching Preparation - Content Review and Interactive Elements',
        'Thursday': 'VCA Model Development',
        'Friday': 'HeadNeck CBCT - Development',
        'Saturday': 'Writing Proposal - Modulating Striatal-Amygdala Pathway'
    },
    '15:00-17:00': {
        'Monday': 'Proposal Writing - Modulating Striatal-Amygdala Pathway',
        'Tuesday': 'Interpretable AI - Algorithm Development',
        'Wednesday': 'Proposal Writing - Modulating Striatal-Amygdala Pathway',
        'Thursday': 'Interpretable AI - Algorithm Development',
        'Friday': 'HeadNeck Outcome',
        'Saturday': 'Teaching Preparation - Finalizing & Recording'
    },
    '18:00-20:00': {
        'Monday': 'Administrative Tasks and Light Research',
        'Tuesday': 'Administrative Tasks and Light Research',
        'Wednesday': 'HeadNeck CBCT - Development',
        'Thursday': 'Administrative Tasks and Light Research',
        'Friday': 'Administrative Tasks and Light Research',
        'Saturday': 'Administrative Tasks and Light Research'
    },
    '20:00-22:00': {
        'Monday': 'Review Day’s Progress and Plan Next Day',
        'Tuesday': 'Review Day’s Progress and Plan Next Day',
        'Wednesday': 'Review Day’s Progress and Plan Next Day',
        'Thursday': 'GatorBrain Project',
        'Friday': 'Review Day’s Progress and Plan Next Day',
        'Saturday': 'Review Day’s Progress and Plan Next Day'
    }
}
# Add events to the calendar for each time slot and work day
for day, day_str in zip(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], work_days):
    for time_slot, tasks in detailed_tasks.items():
        start_time, end_time = time_slot.split('-')
        description = tasks.get(day, 'General Work')
        event = create_event(day_str, start_time, end_time, description, time_zone)
        cal.add_component(event)

# Save the calendar to an .ics file
file_name = 'Custom_Work_Schedule.ics'
with open(file_name, 'wb') as f:
    f.write(cal.to_ical())

print(f"Calendar file '{file_name}' created successfully.")