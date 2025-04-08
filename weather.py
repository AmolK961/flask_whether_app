import json
import requests
from flask import Flask, render_template, request, abort, Response

app = Flask(__name__)

@app.route('/forecast', methods=['GET'])
def get_weather():
    # Get the 'city' argument from the URL
    city = request.args.get('city')

    # If the 'city' argument is missing, return a 400 error
    if not city:
        abort(400, description="Missing argument: city")

    # Prepare API request parameters
    params = {
        'q': city,  # City name
        'appid': '72174ba9bd042b6d20a5f0ec5fe4de83',  # Your API key
        'units': 'metric',  # Temperature units in Celsius
    }

    # Make the API request
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    response = requests.get(url, params=params)

    # If the API request fails (non-200 status code), raise an error
    if response.status_code != 200:
        abort(response.status_code, description=f"Error fetching weather data for {city}")

    # Parse the response JSON
    weather_data = response.json()

    # Render the result in the HTML template
    return render_template('index.html', title='Weather App', data=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
