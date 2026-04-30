print("== Beginner Log Analyzer ===\n")

# Read the log file
with open("sample.log", "r") as file:
    lines = file.readlines()

info_count =0
warning_count = 0
error_count = 0
timestamps = []

for line in lines:
    parts = line.split()

    # Extract timestamp (first two parts)
    timestamp = parts[0] + " " + parts[1]
    timestamps.append(timestamp)

    # Count log levels
    if "INFO" in line:
        info_count +=1
    elif "WARNING" in line:
        warning_count +=1
    elif "ERROR" in line:
        error_count +=1

# Output summary
print(f"Total log entries: {len(lines)}")
print(f"INFO: {info_count}")
print(f"WARNING: {warning_count}")
print(f"ERROR: {error_count}")

print("\nFirst log entry:", timestamps[0])
print("Last log entry:", timestamps[-1])

print("\nLog analysis complete!")
