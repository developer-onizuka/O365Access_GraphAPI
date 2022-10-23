import json 
import requests
import msal
import traceback
import os

#Graph API configuration
graph_url = 'https://graph.microsoft.com'
tenant_id = os.environ['TENANT_ID'] 
client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
user_id = os.environ['USER_ID']

def msgraph_auth():
    authority = 'https://login.microsoftonline.com/' + tenant_id
    scope = ['https://graph.microsoft.com/.default']

    try:
        app = msal.ConfidentialClientApplication(client_id, authority = authority, client_credential = client_secret)
        access_token = app.acquire_token_for_client(scopes = scope)
        if access_token['access_token']:
            print('New access token retrieved....')
            request_headers = {'Authorization': 'Bearer ' + access_token['access_token']}
            return request_headers
        else:
            print('ERROR: No "access_token" in the result.')
    except:
        print('ERROR: Could not acquired authorization token. Check your tenant_id, client_id and client_secret.')
        traceback.print_exc()
        exit(1)

def msgraph_request(resource,request_headers):
    results = requests.get(resource, headers = request_headers).json()
    return results

def get_mail():

    q = "users/" + user_id + "/messages"
    #q = "users"

    request_headers = msgraph_auth()
    results = msgraph_request(graph_url + '/v1.0/' + q, request_headers)

    if results:
        try:
            #print(results)
            for r in results["value"]:
                print(r["receivedDateTime"], "----- subject:", r["subject"])
                #print("userPrincipalName:", r["userPrincipalName"])
        except:
            print('ERROR: No "value" in the result.')
            traceback.print_exc()
            exit(1)

get_mail()
