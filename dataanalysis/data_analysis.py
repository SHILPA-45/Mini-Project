import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load gaze data (Example data, you can save it as a CSV or send it from the frontend)
# Assuming you saved the gaze data in a CSV file from the browser (WebGazer.js can export gaze data)
gaze_data = pd.read_csv('gaze_data.csv')

# Show the first few rows of the data
print(gaze_data.head())

# Analyze the time spent on the passage
gaze_data['timestamp'] = pd.to_datetime(gaze_data['timestamp'], unit='ms')
gaze_data['time_diff'] = gaze_data['timestamp'].diff()

# Find the total time spent focusing on the passage
focus_time = gaze_data[gaze_data['x'].between(100, 500) & gaze_data['y'].between(100, 400)]['time_diff'].sum()
print(f"Total focus time: {focus_time} ms")

# Visualize gaze data
plt.figure(figsize=(10, 6))

# Plot the gaze path (x vs y coordinates)
plt.plot(gaze_data['x'], gaze_data['y'], marker='o', linestyle='-', color='r', markersize=3)
plt.title('Gaze Path')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.grid(True)
plt.show()

# Histogram of gaze coordinates (Distribution of gaze points)
plt.figure(figsize=(10, 6))
plt.hist2d(gaze_data['x'], gaze_data['y'], bins=[50, 50], cmap='Blues')
plt.colorbar(label='Frequency')
plt.title('Gaze Density')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.show()

# Focus vs distraction analysis (check if gaze is within target area)
target_area_x = [100, 500]  # example values for target area X (can vary depending on the passage's position)
target_area_y = [100, 400]  # example values for target area Y

gaze_data['is_focus'] = gaze_data.apply(
    lambda row: target_area_x[0] <= row['x'] <= target_area_x[1] and target_area_y[0] <= row['y'] <= target_area_y[1], axis=1)

# Print the percentage of time spent on focus
focus_percentage = gaze_data['is_focus'].mean() * 100
print(f"Percentage of focus: {focus_percentage:.2f}%")
