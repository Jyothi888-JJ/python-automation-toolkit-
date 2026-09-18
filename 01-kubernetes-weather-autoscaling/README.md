# Auto-Scaling Kubernetes Pods Based on Weather API

This project demonstrates a simple **Python automation script** that checks the current weather using the WeatherAPI and automatically scales a Kubernetes deployment when **Heavy Rain** is detected.

## What This Script Does

1. Calls the **WeatherAPI** to get the current weather.
2. Reads the current weather condition.
3. Checks whether the condition is **Heavy Rain**.
4. If Heavy Rain is detected, it scales the Kubernetes deployment to **3 replicas**.
5. Otherwise, no scaling is performed.

## Technologies Used

* Python
* WeatherAPI
* Kubernetes
* `kubectl`
* Python `requests` module
* Python `subprocess` module

## How It Works

```text
Python Script
     ↓
WeatherAPI
     ↓
Get Current Weather
     ↓
Is it Heavy Rain?
   ↙           ↘
 Yes            No
  ↓              ↓
Scale Pods     No Scaling
to 3 Replicas
```

## Setup

### 1. Install the Python dependency

```bash
pip install requests
```

### 2. Add your WeatherAPI key

Replace:

```python
API_KEY = "YOUR_WEATHER_API_KEY"
```

with your actual WeatherAPI key.

### 3. Make sure Kubernetes is running

The script expects a Kubernetes deployment named:

```text
blogging-app
```

You can verify it with:

```bash
kubectl get deployments
```

### 4. Run the script

```bash
python weather_autoscaling.py
```

## Example Output

### Heavy Rain

```text
Weather in London is Heavy Rain
Scaling up Kubernetes pods to 3 due to heavy rain...
```

### Normal Weather

```text
Weather in London is Sunny
Weather condition normal. No scaling required.
```

## Purpose

This project demonstrates how **Python can be used to automate Kubernetes operations** by combining an external API with the `kubectl` command.
