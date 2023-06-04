import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
load_dotenv()
import os
import keyring

YOUR_DOMAIN_NAME=os.getenv("YOUR_DOMAIN_NAME_JIRA")
username = os.getenv("username_JIRA")
api_token=keyring.get_password("Confluence",'')
base_url = f"https://{YOUR_DOMAIN_NAME}.atlassian.net"
auth = HTTPBasicAuth(username, api_token)
def get_pages():
    auth = HTTPBasicAuth(username,api_token)

    # Set the base URL for your Confluence instance
    # confluence_base_url = 'https://your-confluence-instance.atlassian.net'
    

    # Get the current space id
    # Chanage according to requirement
    conf_url = f'{base_url}/wiki/rest/api/content/'
    response = requests.get(conf_url, auth=auth)
    pageID = response.json()["results"][6]["id"]
    # pageID = response.json()

    return pageID
