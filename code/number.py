import requests
from api import api_number

def numberchoix(number, label):
    try:
        myreq = requests.get(
            f"http://apilayer.net/api/validate"
            f"?access_key={api_number}&number={number}"
        )

        data = myreq.json()

        result = (
            f"Numéro : {number}\n"
            f"Pays : {data.get('country_name', 'Inconnu')}\n"
            f"Format local : {data.get('local_format', 'Inconnu')}\n"
            f"Format international : {data.get('international_format', 'Inconnu')}\n"
            f"Opérateur : {data.get('carrier', 'Inconnu')}"
        )

        label.config(text=result)

    except Exception as e:
        label.config(text=f"Erreur : {e}")