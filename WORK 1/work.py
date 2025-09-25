# Project 123: Emergency Room Triage

import array

# -------------------------------
# 1. Integers
# -------------------------------
# Suppose these represent patient waiting times in minutes
waiting_times = [15, 30, 45, 10, 25]

total = sum(waiting_times)
average = total / len(waiting_times)
minimum = min(waiting_times)
maximum = max(waiting_times)

print("=== Integers ===")
print(f"Total waiting time: {total}")
print(f"Average waiting time: {average}")
print(f"Minimum waiting time: {minimum}")
print(f"Maximum waiting time: {maximum}\n")

# -------------------------------
# 2. Strings (Formatted Report)
# -------------------------------
report = (
    f"Emergency Room Triage Report:\n"
    f"Total Patients: {len(waiting_times)}\n"
    f"Total Waiting Time: {total} minutes\n"
    f"Average Waiting Time: {average:.2f} minutes\n"
)
print("=== Strings ===")
print(report)

# -------------------------------
# 3. Booleans (Threshold Condition)
# -------------------------------
threshold = 20
if average > threshold and maximum > 40:
    status = "Above Standard"
else:
    status = "Below Standard"

print("=== Booleans ===")
print(f"Status: {status}\n")

# -------------------------------
# 4. Lists
# -------------------------------
patients = ["Alice", "Bob", "Charlie", "Diana"]
print("=== Lists ===")
print("Original list:", patients)

# Add a new element
patients.append("Ethan")

# Remove one based on a condition (remove if name starts with 'C')
patients = [p for p in patients if not p.startswith("C")]

# Sort the list
patients.sort()

print("Modified list:", patients, "\n")

# -------------------------------
# 5. Arrays
# -------------------------------
# Store subset of waiting times in an array
arr_waiting = array.array("i", [15, 30, 45])

arr_sum = sum(arr_waiting)
list_sum = sum(waiting_times)

print("=== Arrays ===")
print("Array contents:", arr_waiting)
print(f"Array sum: {arr_sum}")
print(f"List sum: {list_sum}\n")

# -------------------------------
# 6. Dictionaries
# -------------------------------
triage_records = [
    {"id": 1, "name": "Alice", "value": 15},
    {"id": 2, "name": "Bob", "value": 30},
    {"id": 3, "name": "Charlie", "value": 45},
]

print("=== Dictionaries ===")
print("Original records:", triage_records)

# Update one record
triage_records[1]["value"] = 35  # Update Bob's waiting time

# Delete another record (Charlie)
triage_records = [rec for rec in triage_records if rec["id"] != 3]

# Compute total of 'value'
total_value = sum(rec["value"] for rec in triage_records)

print("Updated records:", triage_records)
print("Total of 'value' field:", total_value)
