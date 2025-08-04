# Built-in modules
import time
import csv
import os
from datetime import datetime

# External modules
import board
import busio
import adafruit_bme680  # Environmental sensor.
import adafruit_bh1750  # Light (lux) sensor.


def main():
    # Set pi board to use I2C communication.
    i2c = board.I2C()

    # Create light sensor object.
    #bh1750 = adafruit_bh1750.BH1750(i2c)

    # Create environmental sensor object.
    bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

    # Set sea level pressure (in hPa) for altitude reading.
    bme680.sea_level_pressure = 1013.25
    
    # Get current local date and time.
    current_datetime = datetime.now()

    # Round light sensor values (lux) for readability.
    #rounded_lux = round(bh1750.lux, 2)

    # Round environmental sensor values for readability.
    rounded_temp = round(bme680.temperature, 1)
    rounded_gas = round(bme680.gas, 1)
    rounded_humidity = round(bme680.humidity, 1)
    rounded_pressure = round(bme680.pressure, 1)
    rounded_altitude = round(bme680.altitude, 2)
    
    # Save rounded environmental sensor values as well as timestamp.
    data_row = [
            current_datetime,
            rounded_temp,
            rounded_gas,
            rounded_humidity,
            rounded_pressure,
            rounded_altitude
    ]
    
    # File name for data file (csv).
    csv_file = "/home/aj/Projects/project-vela/bme680_data.csv"

    # Check if file already exists.
    does_file_exist = os.path.isfile(csv_file)

    # Open the file in append mode.
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)

        # If the file is new, write the header.
        if not does_file_exist:
            writer.writerow([
                'Timestamp',
                'Temperature (C)',
                'Gas (Ohms)',
                'Humidity (%)',
                'Pressure (hPa)',
                'Altitude (m)'
            ])

        # Write the data row.
        writer.writerow(data_row)


if __name__ == "__main__":
    main()
