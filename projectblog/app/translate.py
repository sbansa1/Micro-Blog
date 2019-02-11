import json
import requests
from flask_babel import _
from app import app

def translate(text,source_language,dest_langauge):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
        not app.config['MS_TRANSLATOR_KEY']:
        return _("Error: the translation service is not configured")
    auth = {"Ocp-Apim-Subscription-Key": app.config["MS_TRANSLATOR_KEY"]}
    req = requests.get('https://api.microsofttranslator.com/v2/Ajax.svc'
                     '/Translate?text={}&from={}&to={}'.format(text,source_language,dest_langauge),headers=auth)
    if req.status_code !=200:
        return _("Error: the translation service failed. ")
    return json.loads(req.content.decode('UTF-8-Sig'))

