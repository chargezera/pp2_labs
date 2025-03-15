from datetime import datetime

date1 = datetime(2025, 3, 7, 12, 0, 0)  # Example date 1
date2 = datetime(2025, 3, 5, 10, 30, 0)  # Example date 2

difference = abs((date1 - date2).total_seconds())

print("Difference in seconds:", difference)