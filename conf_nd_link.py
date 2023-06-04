import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
load_dotenv()
import os
import get_pages as gp
import keyring

YOUR_DOMAIN_NAME=os.getenv("YOUR_DOMAIN_NAME_JIRA")
username = os.getenv("username_JIRA")
api_token=keyring.get_password("Confluence",'')
base_url = f"https://{YOUR_DOMAIN_NAME}.atlassian.net"
auth = HTTPBasicAuth(username, api_token)

def jira_on_conf(subject,body):

    # Set the page ID for the Confluence page you want to link from 
    #this one is hard coded
    page_id = gp.get_pages()

    # Set the URL for the Jira issue you want to link to
    # jira_issue_url = 'https://your-jira-instance.atlassian.net/browse/ABC-123'
    jira_issue_url = f'https://{YOUR_DOMAIN_NAME}.atlassian.net/browse/TECH-3'

    # Get the current page version
    url = f'{base_url}/wiki/rest/api/content/{page_id}'
    response = requests.get(url, auth=auth)
    page_version = response.json()['version']['number']
    print(page_version)

    # Create a web link on the Confluence page
    url = f'{base_url}/wiki/rest/api/content/{page_id}'
    headers = {'Content-Type': 'application/json'}
    data = {
        'version': {
            'number': page_version + 1
        },
        'body': {
            'storage': {
                'value': f'<p><a href="{jira_issue_url}">Jira Issue</a></br>Description: {body}</p>',
                'representation': 'storage'
            }
        },
        "type": "page",
        "title": subject
    }
    response = requests.put(url, auth=auth, headers=headers, json=data)
    print(response.status_code)
    # Check the response
    if response.status_code == 200:
        print('Web link created successfully')
    else:
        print(f'Error creating web link: {response.text}')


def create_conf_page(subject,body):
    # credentials

    # Get the current space id
    # Chanage according to requirement
    conf_url = f'{base_url}/wiki/api/v2/spaces'
    response = requests.get(conf_url, auth=auth)
    spaceID = response.json()['results'][1]['id']
    print("Found Space: ",spaceID)



    # url = "https://artechmania.atlassian.net/wiki/api/v2/pages"
    url = f'{base_url}/wiki/api/v2/pages'
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
        #  space id get from space using rest api
    "spaceId": spaceID,
    "status": "current",
    "title": subject,
    
    "body": {
        "representation": "storage",
        # Here we write anything to write in page 
        "value": body
    }
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )
    # print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
    jira_on_conf(subject,body)

    print(response.status_code)




#create_conf_page()
#jira_on_conf()


