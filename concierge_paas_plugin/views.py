import requests
from django.contrib.auth.decorators import login_required
from .models import Configuration

@login_required
def create(request, id, name, email):
    configuration = Configuration.objects.get(default=True)
    authorizationHeader = request.META.get('HTTP_AUTHORIZATION', '')

    # ToDo replace this with messages over Kafka system for notification
    if configuration.trigger is True:
        attempt = 0
        retrys = 3
        success = False

        query = {'query': 'mutation{createProfile(gcId: "' + str(id) + '", name: "' + name + '", email:"' +
                          email + '"){gcID, name, email}}'}

        while not success and attempt < retrys:
            response = requests.post(configuration.end_point, authorizationHeader, data=query)
            if not response.status_code == requests.codes.ok:
                attempt = attempt + 1
            else:
                success = True
        if not success:
            # Write this to log eventually
            raise Exception('Error setting user data / Server Response ' + str(response.status_code))

@login_required
def queryprofile(request, userId):
    # Get rest of information from Profile as a Service
    query = {
        'query': 'query{profiles(gcID: "' + str(userId) + '"){name, email, avatar, mobilePhone, officePhone}}'}
    print(query)
    authorizationHeader = request.META.get('HTTP_AUTHORIZATION', '')
    return ProfileHelper.executeQuery(authorizationHeader, query)

class ProfileHelper():
    @staticmethod
    def executeQuery(authorizationHeader, query):
        retry = 3
        success = False
        attempt = 0

        configuration = Configuration.objects.get(default=True)
        while not success and attempt < retry:
            response = requests.post(configuration.end_point, authorizationHeader, data=query)
            print(response)
            if not response.status_code == requests.codes.ok:
                attempt = attempt + 1
            else:
                success = True

        if not success:
            return None

        response = response.json()
        return response