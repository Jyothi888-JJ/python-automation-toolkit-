# Website / Server Health Monitor with Slack Webhook Alerts

This project demonstrates a simple **Python server monitoring script** that checks whether a website or server is reachable and sends an automated alert to a **Slack channel** when an issue is detected.

## What This Script Does

1. Sends an HTTP request to the specified server URL.
2. Checks the HTTP response status code.
3. Reports the server as **UP** when it returns status code `200`.
4. Generates a warning when the server returns an error status.
5. Generates a DOWN alert when the server cannot be reached.
6. Sends the monitoring result to Slack using an **Incoming Webhook**.

## Alert Conditions

| Condition                  | Alert                    |
| -------------------------- | ------------------------ |
| HTTP `200`                 | Server is UP             |
| Other HTTP status          | Warning with status code |
| Connection/Request failure | Server is DOWN           |

## Technologies Used

* Python
* Requests
* HTTP
* Slack Incoming Webhooks

## How It Works

```text id="m2b7xa"
Server URL
     ↓
Send HTTP Request
     ↓
Check Response
     ↓
 ┌───┼──────────┐
 200  Error    Un
```
