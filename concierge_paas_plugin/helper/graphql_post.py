import requests
from concierge_paas_plugin.models import Configuration

def executeQuery(query):
    retry = 3
    success = False
    attempt = 0

    configuration = Configuration.objects.get(default=True)
    while not success and attempt < retry:
        response = requests.post(configuration.end_point, headers={'Authorization': 'Token ' + configuration.token}, data=query)
        if not response.status_code == requests.codes.ok:
            attempt = attempt + 1
        else:
            success = True

    if not success:
        return None

    response = response.json()
    return response