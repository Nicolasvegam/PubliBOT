from googleads import ad_manager
from googleads import oauth2


# Initialize the GoogleRefreshTokenClient using the credentials you received
# in the earlier steps.
oauth2_client = oauth2.GoogleServiceAccountClient(
    'client_secret_773664483695-tp6q1ditrsl96fm0a1f6ir8sg75ftod6.apps.googleusercontent.com.json', oauth2.GetAPIScope('ad_manager'))

# Initialize the Ad Manager client.
ad_manager_client = ad_manager.AdManagerClient(oauth2_client, application_name)
