# Part 1: Average Calculator
def calculate_average(data):
    return sum(data) / len(data)

# Run on sample data
values = [72, 55, 101, 90]
average = calculate_average(values)
print("Average PM2.5 value:", average)

# Part 2: Stations List & Display
stations = [
    ["A1", 62],
    ["B2", 105],
    ["C3", 88]
]

# Print each station on its own line
for station in stations:
    print(f"{station[0]} → {station[1]}")

# Part 3: Status Reporter
def report_status(stations, threshold):
    for station in stations:
        name, pm25 = station
        if pm25 > threshold:
            status = "ALERT"
        else:
            status = "OK"
        print(f"{name}: {pm25} μg/m³ - {status}")

# Call with threshold 100
report_status(stations, 100)
