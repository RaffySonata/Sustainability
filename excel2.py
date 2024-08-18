import pandas as pd
import datetime as dt

# Define the start and end dates
start_date = dt.datetime(2024, 8, 8)
end_date = dt.datetime(2024, 9, 3)

# Define the exclusion dates
exclusion_dates = pd.date_range(start="2024-08-19", end="2024-08-24").tolist() + pd.date_range(start="2024-09-03", end="2024-09-05").tolist()

# Create a date range excluding the specified dates
all_dates = pd.date_range(start=start_date, end=end_date).tolist()
valid_dates = [date for date in all_dates if date not in exclusion_dates]

# Generate a detailed schedule based on the study plan
schedule = []

# Week 1-4: Fundamentals and Course Familiarization
for week in range(4):
    for day in valid_dates:
        if day.weekday() == 0:  # Monday
            schedule.append((day, "10:00-12:00", "Microeconomics - MIT YouTube Lecture"))
            schedule.append((day, "14:00-16:00", "Econometrics - Wooldridge Chapter 1/3"))
        elif day.weekday() == 1:  # Tuesday
            schedule.append((day, "10:00-12:00", "Macroeconomics - MIT YouTube Lecture"))
            schedule.append((day, "14:00-16:00", "Python - Introduction to Python/numpy"))
        elif day.weekday() == 2:  # Wednesday
            schedule.append((day, "10:00-12:00", "Microeconomics - MIT YouTube Lecture"))
            schedule.append((day, "14:00-16:00", "Econometrics - Wooldridge Chapter 2/4"))
        elif day.weekday() == 3:  # Thursday
            schedule.append((day, "10:00-12:00", "Macroeconomics - MIT YouTube Lecture"))
            schedule.append((day, "14:00-16:00", "Python - numpy/pandas"))
            schedule.append((day, "16:00-18:00", "Microeconomics - Review/Case Studies"))
            schedule.append((day, "18:00-20:00", "Econometrics - Problem Sets"))
        elif day.weekday() == 4:  # Friday
            schedule.append((day, "10:00-12:00", "Microeconomics - Reading/Discussion"))
            schedule.append((day, "14:00-16:00", "Econometrics - Discussion/Software"))
        elif day.weekday() == 5:  # Saturday
            schedule.append((day, "10:00-12:00", "Macroeconomics - Reading/Discussion"))
            schedule.append((day, "13:00-16:00", "Python - Exercises/Projects"))

# Convert to DataFrame
schedule_df = pd.DataFrame(schedule, columns=["Date", "Time", "Task"])

import ace_tools as tools; tools.display_dataframe_to_user(name="Study Schedule", dataframe=schedule_df)

# Save to an Excel file
file_path = "/mnt/data/study_schedule.xlsx"
schedule_df.to_excel(file_path, index=False)

file_path
