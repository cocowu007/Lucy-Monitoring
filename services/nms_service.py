import os, logging
import requests
import json
import re
import openai
from flask import render_template, request, session, jsonify
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ------------------ Config ------------------
ZABBIX_API_TOKEN = os.getenv('ZABBIX_API_TOKEN')
ZABBIX_URL = os.getenv('ZABBIX_URL')
ZABBIX_HEADERS = {"Content-Type": "application/json-rpc"}

openai.api_type = os.getenv('OPENAI_API_TYPE')
openai.azure_endpoint = os.getenv('OPENAI_AZURE_ENDPOINT')
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_version = os.getenv('OPENAI_API_VERSION')

DASHBOARDS = {
    "Nigeria": 130,
    "Afghanistan": 89,
    "Comoros": 855,
    "Ethiopia": 112,
    "Iran": 561,
    "Myanmar": 127,
    "North Korea": 735,
    "Mozambique": 126,
    "Rwanda": 738,
    "Sudan": 751,
    "Syria": 752,
    "Haiti": 118
}

INFRASTRUCTURES = ["OneICTbox", "BE6K", "OpenDNS", "UPS", "MSS-3", "VSAT", "VPN", "VOIP"]

# ------------------ OpenAI ------------------
def use_openai(system_content, user_content):
    try:
        completion = openai.chat.completions.create(
            model="gpt-4o-itm-sicu",
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content}
            ],
            temperature=0.7,
            max_tokens=800
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"OpenAI error: {e}")
        return ""

# ------------------ Helpers ------------------
def get_dashboard_info(dashboard_id):
    payload = {
        "jsonrpc": "2.0",
        "method": "dashboard.get",
        "params": {
            "output": "extend",
            "dashboardids": [dashboard_id],
            "selectPages": "extend"
        },
        "auth": ZABBIX_API_TOKEN,
        "id": 1
    }
    res = requests.post(ZABBIX_URL, headers=ZABBIX_HEADERS, json=payload)
    return res.json().get("result", [])

def get_hostid_from_widgets(widgets):
    hostids = set()
    for widget in widgets:
        for field in widget.get("fields", []):
            if field.get("name", "").startswith("hostid"):
                hostids.add(field["value"])
    return list(hostids)

def get_country_devices(dashboard_id):
    dashboard_info = get_dashboard_info(dashboard_id)
    devices = {}
    for dashboard in dashboard_info:
        for page in dashboard.get("pages", []):
            name = page.get("name")
            widgets = page.get("widgets", [])
            hostids = get_hostid_from_widgets(widgets)
            if hostids:
                devices[name] = hostids[0]  # default one host
    return devices

# ------------------ Views ------------------
def nms_landing():
    logging.info("-----------nms_landing------")
    return render_template('landing.html', dashboards=DASHBOARDS, mode='nms')

def nms_index():
    logging.info("-----------nms_index------")
    if request.method == 'GET':
        dashboard_id = request.args.get('dashboard_id')
        if dashboard_id:
            session['dashboard_id'] = dashboard_id
        devices = get_country_devices(dashboard_id)
        return render_template('index.html', country_devices=devices, mode='nms')

    if request.method == 'POST':
        data = request.get_json()
        query = data.get('query', '')
        devices = get_country_devices(session.get('dashboard_id'))
        prompt = f"User: {query}\nDevices: {devices}\nRespond appropriately."
        response = use_openai("You are a helpful NMS assistant.", prompt)
        return jsonify({"response": response})