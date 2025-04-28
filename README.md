# Lucy Monitoring Assistant (Unified Version)

Lucy Monitoring Assistant is an intelligent monitoring assistant designed to provide real-time insights into:
- IoT infrastructure (via ThingsBoard)
- Network infrastructure (via Zabbix)

This unified version merges Lucy IoT and Lucy NMS into a single Flask application, allowing users to select the monitoring mode (IoT or Network) dynamically.

## Features

- Landing page with mode selection (IoT or NMS)
- Dynamic dashboard/country selection 
- Chat-style assistant with OpenAI GPT integration
- IoT monitoring via ThingsBoard REST API
- Network monitoring via Zabbix JSON-RPC API
- Modular project structure
- Separate service and view layers

## Project Structure
Lucy-Monitoring/
|├── app.py                  # Unified Flask entry point
|├── services/                # Business logic modules
|   |├── iot_service.py         # IoT mode backend logic
|   └── nms_service.py         # NMS mode backend logic
|├── views/                   # Flask Blueprint views
|   |├── iot_views.py          # IoT mode routes
|   └── nms_views.py          # NMS mode routes
|├── templates/              # Jinja2 templates
|   |├── landing.html          # Shared landing page
|   └── index.html             # Shared index page
|├── static/
|   |└── images/             # Logo and dashboard images
|├── dashboards/              # IoT dashboards data (data.json)
|├── requirements.txt        # Python dependencies
|├── .env                    # Environment settings
|└── README.md

## Setup

1. Clone Repository

git clone https://github.com/cocowu007/Lucy-Monitoring.git
cd lucy-monitoring

2. Create and Activate Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
```

3. Install Dependencies
```
pip install -r requirements.txt
```

4. Environment Configuration

Create a .env file in the root directory as indicated in the repo

## Running
```
python app.py
```
The app will be available at:
```
http://127.0.0.1:5001
```

## Usage Flow

- Visit Home Page: Select either IoT Monitoring or Network Monitoring.
- Landing Page: Choose a site (IoT) or country (NMS) from the list.
- Chat Interface: Ask natural language questions about devices, telemetry, alarms, network issues, etc.

OpenAI GPT will smartly assist you based on the selected monitoring mode.

## Notes

- Ensure ThingsBoard and Zabbix instances are reachable.
- For IoT mode, a valid dashboards/data.json must be available or generated.
- For NMS mode, make sure your Zabbix token is valid and not expired.