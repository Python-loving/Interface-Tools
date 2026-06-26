import requests
from sites import sites

def fulluser_name(username, label):
    try:
        result = ""

        for site, url in sites.items():
            full_url = url.format(username)

            myreq = requests.get(full_url)

            if myreq.status_code == 200:
                result += f"Trouvé sur {site} : {full_url}\n"
            else:
                result += f"Rien trouvé sur {site}\n"

        label.config(text=result)

    except Exception as e:
        label.config(text=f"Error: {e}")