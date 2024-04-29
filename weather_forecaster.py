class WeatherDataFetcher:
    
       
    def fetch_weather_data(self, city):
        # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {city}...")
        # Simulated data based on city
        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
        }
        return weather_data[city]


class WeatherDataParser:
    def parse_weather_data(self, data, city):
        # Function to parse weather data
        if not data:
            return "Weather data not available"
        # city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"


class WeatherForecastDisplay:
    def display_weather(self, city, detailed=False):
        fetcher = WeatherDataFetcher()
        parser = WeatherDataParser()
        data = fetcher.fetch_weather_data(city)
        # print(data)
        if not data:
            print(f"Weather data not available for {city}")
            return
        if detailed:
            forecast = parser.parse_weather_data(data, city)
        else:
            forecast = f"Weather in {city}: {data['temperature']} degrees, {data['condition']}"
        print(forecast)


class WeatherApp:
    def main(self):
        display = WeatherForecastDisplay()
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            detailed_forecast = detailed == 'yes'
            display.display_weather(city, detailed_forecast)


