from datetime import datetime, timedelta

current_date = datetime.today()

new_date = current_date - timedelta(days=5)

print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("Date After Subtracting 5 Days:", new_date.strftime("%Y-%m-%d"))