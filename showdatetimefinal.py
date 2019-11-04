from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%d-%m-%Y")
print("--------------------------------")
print("|                              |")
print("| Current Date is ", current_date, " |")
print("| Current Time =", current_time, "     |")
print("|                              |")

print("--------------------------------")
