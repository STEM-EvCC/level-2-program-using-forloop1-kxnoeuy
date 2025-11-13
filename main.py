mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

# Initialize counters and lists
total_missions = 0
successful_missions = 0
missions_before_2000 = []

# Iterate through all missions
for i in range(len(mission_names)):
    total_missions += 1

    # Count successful missions
    if mission_success[i]:
        successful_missions += 1

    # Check for missions launched before 2000
    if mission_years[i] < 2000:
        missions_before_2000.append(mission_names[i])

# Calculate success rate
success_rate = (successful_missions / total_missions) * 100

# Output the results
print("Total number of missions: " + str(total_missions))
print("Number of successful missions: " + str(successful_missions))
print("Success rate: " + str(success_rate))
print("Missions launched before the year 2000:")
for mission in missions_before_2000:
    print(mission)
