import requests

def monitor_server_health(server_url, slack_webhook_url):
    try:
        response = requests.get(server_url, timeout=5)
        if response.status_code == 200:
            message = f"✅ Server {server_url} is UP and running smoothly."
        else:
            message = f"⚠️ Server {server_url} returned status code {response.status_code}."
    except Exception as e:
        message = f"🚨 Server {server_url} is DOWN! Error: {e}"

    payload = {"text": message}
    requests.post(slack_webhook_url, json=payload)

server_url = "http://localhost:8080"
slack_webhook = "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
monitor_server_health(server_url, slack_webhook)
