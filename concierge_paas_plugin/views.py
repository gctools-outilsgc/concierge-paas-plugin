import requests
from .models import Configuration

class Profile():
    @staticmethod
    def create(id, name, email):
        configuration = Configuration.objects.get(default=True)
        # ToDo replace this with messages over Kafka system for notification
        if configuration.trigger is True:
            attempt = 0
            retrys = 3
            success = False

            query = {'query': 'mutation{createProfile(gcId: "' + str(id) + '", name: "' + name + '", email:"' +
                              email + '"){gcID, name, email}}'}

            while not success and attempt < retrys:
                response = requests.post(configuration.end_point, headers={'Authorization': 'Token ' + configuration.token},
                                    data=query)
                if not response.status_code == requests.codes.ok:
                    attempt = attempt + 1
                else:
                    success = True
            if not success:
                # Write this to log eventually
                raise Exception('Error setting user data / Server Response ' + str(response.status_code))