import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data(date):
    response = requests.get(API_URL)
    if response.status_code == 200:
        weather_data = response.json()
        return [data for data in weather_data['list'] if data['dt_txt'].startswith(date)]
    else:
        print("Error fetching weather data from the API.")
        return None

def get_user_option():
    print("1. Get weather")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")

    try:
        option = int(input("Enter your choice: "))
        return option
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def get_date_from_user():
    date = input("Enter the date (YYYY-MM-DD): ")
    return date

def print_weather_data(data_list):
    if data_list:
        for data in data_list:
            print(f"Date: {data['dt_txt']}, Temperature: {data['main']['temp']} °C")
    else:
        print("Weather data not found for the specified date.")

def print_wind_speed_data(data_list):
    if data_list:
        for data in data_list:
            print(f"Date: {data['dt_txt']}, Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("Wind speed data not found for the specified date.")

def print_pressure_data(data_list):
    if data_list:
        for data in data_list:
            print(f"Date: {data['dt_txt']}, Pressure: {data['main']['pressure']} hPa")
    else:
        print("Pressure data not found for the specified date.")

def main():
    while True:
        option = get_user_option()

        if option == 1:
            date = get_date_from_user()
            weather_data = get_weather_data(date)
            print_weather_data(weather_data)

        elif option == 2:
            date = get_date_from_user()
            wind_data = get_weather_data(date)
            print_wind_speed_data(wind_data)

        elif option == 3:
            date = get_date_from_user()
            pressure_data = get_weather_data(date)
            print_pressure_data(pressure_data)

        elif option == 0:
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
