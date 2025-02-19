import argparse
import csv
from statistics import median
from typing import List, Dict, Optional

def process_weather_data(file_path: str) -> None:
    """
    Process weather data from a CSV file and calculate relevant statistics.

    Improvements made:
    1. Added type hints for the function parameters and return types.
        - This helps catch type-related errors at runtime and makes the code more readable.
    
    2. Added a docstring to explain the purpose of the function.
        - This makes the code more readable and helps other developers understand what the function does.
    
    3. Used a try-except block to handle any potential errors when opening and reading the CSV file.
        - This prevents the program from crashing if the file is not found or if there is an error while reading the file.
    
    4. Used list comprehensions to create lists of temperatures and humidities.
    5. Used the built-in sum, max, min, and median functions to calculate the average temperature, maximum temperature, minimum temperature, 
    median temperature, average humidity, and maximum humidity.
        - This makes the code more concise and easier to read and lessens memory usage.
    
    8. Used an if statement to check if the argument is empty.
        - This prevents the program from crashing without a specified error if the file is empty.

    Args:
        file_path (str): The path to the CSV file containing the weather data.

    Returns:
        None
    """
    weather_data: List[Dict[str, str]] = []

    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                weather_data.append(row)

        if not weather_data:
            print("No data found in the file.")
            return

        temperatures: List[float] = [float(item['temperature']) for item in weather_data]
        humidities: List[float] = [float(item['humidity']) for item in weather_data]

        avg_temp = sum(temperatures) / len(temperatures)
        avg_humidity = sum(humidities) / len(humidities)

        max_temp = max(temperatures)
        min_temp = min(temperatures)
        median_temp = median(temperatures)

        max_humidity_day = max((item for item in weather_data), key=lambda x:float(x['humidity']))['date']
        max_humidity = float(max((item['humidity'] for item in weather_data)))
        min_humidity_day = min((item for item in weather_data), key=lambda x:float(x['humidity']))['date']
        min_humidity = float(min((item['humidity'] for item in weather_data)))

        print(f"""
        +=====================================================+
        | Weather Statistics                                  |
        |                                                     |
        | Average Temperature: {avg_temp:.2f}°C")                      |
        | Average Humidity: {avg_humidity:.2f}%")                          |
        | Maximum Temperature: {max_temp:.2f}°C")                      |
        | Minimum Temperature: {min_temp:.2f}°C")                      |
        | Median Temperature: {median_temp:.2f}°C")                       |
        | Maximum Humidity: {max_humidity:.2f}% on {max_humidity_day}")            |
        | Minimum Humidity: {min_humidity:.2f}% on {min_humidity_day}")            |
        +=====================================================+
        """)

    except FileNotFoundError:
        print("The file was not found.")
    except csv.Error:
        print("An error occurred while reading the CSV file.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process weather data from a CSV file and calculate relevant statistics.")
    parser.add_argument('file_path', type=str, help="The path to the CSV file containing the weather data.")

    args = parser.parse_args()
    process_weather_data(args.file_path)
