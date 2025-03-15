from datetime import datetime

current_datetime = datetime.now()

datetime_without_microseconds = current_datetime.replace(microsecond=0)

# Print results
print("Original Datetime:", current_datetime)
print("Datetime Without Microseconds:", datetime_without_microseconds)