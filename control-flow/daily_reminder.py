task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process the task using match case
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unspecified priority. Please review."

# Adjust message if the task is time-sensitive
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if priority == "low":
        message += ". Consider completing it when you have free time."

# Output the final reminder
print(message)
