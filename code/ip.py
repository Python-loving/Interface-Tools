import time
import os
import requests
from api import api_ip

def ipchoix(ip, label):
    try:
        myreq = requests.get(
            f"https://geo.ipify.org/api/v2/country,city,vpn"
            f"?apiKey={api_ip}&ipAddress={ip}"
        )

        data = myreq.json()

        result = (
            f"IP: {data['ip']}\n"
            f"Pays: {data['location']['country']}\n"
            f"Ville: {data['location']['city']}\n"
            f"ISP: {data['isp']}"
        )

        label.config(text=result)

    except Exception as e:
        label.config(text=f"Error: {e}")