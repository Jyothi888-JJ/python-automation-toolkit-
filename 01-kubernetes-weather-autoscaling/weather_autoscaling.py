import requests
import subprocess

API_KEY = "YOUR_WEATHER_API_KEY"
CITY = "London"
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"

# Step 1: Fetch weather details in JSON format
response = requests.get(URL)
data = response.json()
weather = data["current"]["condition"]["text"]

print(f"Weather in {CITY} is {weather}")

# Step 2: Check condition and scale up Kubernetes pods if Heavy Rain occurs
if "Heavy Rain" in weather:
    print("Scaling up Kubernetes pods to 3 due to heavy rain...")
    subprocess.run(["kubectl", "scale", "deployment", "blogging-app", "--replicas=3"])
else:
    print("Weather condition normal. No scaling required.")
