# Built-in modules
import time
import csv
import os
from datetime import datetime

# External modules
import board
import adafruit_bh1750


def main():
    # Set pi board to use I2C communication.
    i2c = board.I2C()

    # BH1750 is the light sensor.
    sensor = adafruit_bh1750.BH1750(i2c)
    
    # Get current local date and time.
    current_datetime = datetime.now()
    
    # Lux reading (light intensity) as well as timestamp.
    data_row = [current_datetime, sensor.lux]
    
    # File name for data file (csv).
    csv_file = "sensor_data.csv"

    # Check if file already exists.
    does_file_exist = os.path.isfile(csv_file)

    # Open the file in append mode.
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)

        # If the file is new, write the header.
        if not does_file_exist:
            writer.writerow(['Timestamp', 'LUX'])

        # Write the data row.
        writer.writerow(data_row)


if __name__ == "__main__":
    main()
