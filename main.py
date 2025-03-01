# Python program to calculate the number of days it takes for the frog to escape the pit

def days_to_escape(depth, climb, slide):
    days = 0
    current_height = 0

    while current_height < depth:
        days += 1
        current_height += climb  # Frog climbs up during the day
        
        if current_height >= depth:
            break  # The frog escapes before sliding back
        
        current_height -= slide  # Frog slides back at night

    return days

# Parameters for the problem
depth = 30  # depth of the pit in meters
climb = 3   # meters climbed each day
slide = 2   # meters slid back each night

# Calculating the number of days
days_required = days_to_escape(depth, climb, slide)
print(f"The number of days it takes for the frog to escape is {days_required}.")
