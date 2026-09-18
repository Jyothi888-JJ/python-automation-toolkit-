Weather-Based Autoscaler Script
This repository contains a Python script that continuously checks the current weather conditions for a specified city using the WeatherAPI service. If severe weather (e.g., Heavy Rain) is detected, it automatically scales up a Kubernetes deployment to handle potential surges in traffic or load.

📋 Features
Weather Data Fetching: Integrates with WeatherAPI to fetch real-time weather conditions in JSON format.

Automated Scaling: Uses Python's subprocess module to execute kubectl commands.

Dynamic Capacity Management: Automatically adjusts Kubernetes deployment replicas based on defined weather triggers.

🛠️ Prerequisites
Before running the script, ensure you have the following installed and configured:

Python 3.x

requests Library: Install via pip:

Bash
pip install requests
kubectl CLI: Installed and configured with context access to your target Kubernetes cluster.

WeatherAPI Key: A free or paid API key from WeatherAPI.

⚙️ Configuration & Setup
Clone the repository:

Bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Configure Variables:
Open main.py (or your script file) and replace the placeholder values:

Set API_KEY to your valid WeatherAPI key.

Set CITY to your target location.

Ensure the deployment name (blogging-app) matches your target Kubernetes deployment.

Python
API_KEY = "YOUR_ACTUAL_WEATHER_API_KEY"
CITY = "London"
🚀 Usage
Run the script directly from your terminal:

Bash
python main.py
Script Workflow:
Normal Conditions: If the weather condition does not contain "Heavy Rain", the script outputs a normal weather log and exits without changing cluster state.

Heavy Rain Detected: If "Heavy Rain" is present in the weather payload, the script runs:

Bash
kubectl scale deployment blogging-app --replicas=3
