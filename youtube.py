import os
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def test():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"


    api_service_name = "youtube"
    api_version = "v3"
    with open('/home/amadrazo/projects/spotify-to-wav/client_secrets_file.json','r') as j:
        data = json.load(j)

    print(data)


    #Get Credentials and Create API Client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
       data, scopes
    )
    credentials = flow.run_console()
    youtube = googleapiclient_discovery_build(
        api_service_name,api_version,credentials=credentials
    )

    request = youtube.search().list(
        part="snippet",
        maxResults=5,
        q="Surfing"
    )

    respone = request.execute()
    print(response)


