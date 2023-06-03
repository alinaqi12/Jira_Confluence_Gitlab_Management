import requests
from requests.auth import HTTPBasicAuth
import json
import get_pages as gp


def create_conf_page():
    # credentials
    base_url = "https://artechmania.atlassian.net"

    auth = HTTPBasicAuth("arttechmania@gmail.com", "ATATT3xFfGF0vGeuHzmznOfX0WYkVQ4xeZMpfDL_JZSQ8PS6DtvRMF1Jpx0PUpO752tXh4mPaFOMCRIqZ4_P4IWs96WwaHPREs6zemwNVpR1l6W1-fZBiMlNWVhKQ8oas8tQHlKB96ci8CUTOxeuzFG-BRGs09Q3zwblza8npUpWCTJWN6vsw-g=D7BE4289")

    # Get the current space id
    # Chanage according to requirement
    conf_url = f'{base_url}/wiki/api/v2/spaces'
    response = requests.get(conf_url, auth=auth)
    spaceID = response.json()['results'][1]['id']
    print(spaceID)



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
    "title": "This page is using python code on vscode made by iname",
    
    "body": {
        "representation": "storage",
        # Here we write anything to write in page 
        "value": "ok hogya g ali bhai masti na kr"
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
    print(response.status_code)


def jira_on_conf():

    auth = HTTPBasicAuth("arttechmania@gmail.com", "ATATT3xFfGF0vGeuHzmznOfX0WYkVQ4xeZMpfDL_JZSQ8PS6DtvRMF1Jpx0PUpO752tXh4mPaFOMCRIqZ4_P4IWs96WwaHPREs6zemwNVpR1l6W1-fZBiMlNWVhKQ8oas8tQHlKB96ci8CUTOxeuzFG-BRGs09Q3zwblza8npUpWCTJWN6vsw-g=D7BE4289")

    base_url = 'https://artechmania.atlassian.net'

    # Set the page ID for the Confluence page you want to link from 
    #this one is hard coded
    page_id = gp.get_pages()

    # Set the URL for the Jira issue you want to link to
    # jira_issue_url = 'https://your-jira-instance.atlassian.net/browse/ABC-123'
    jira_issue_url = 'https://artechmania.atlassian.net/browse/TECH-3'

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
                'value': f'<p><a href="{jira_issue_url}">Jira Issue</a></p>',
                'representation': 'storage'
            }
        },
        "type": "page",
        "title": "This page is using python code on vscode made by iname"
    }
    response = requests.put(url, auth=auth, headers=headers, json=data)
    print(response.status_code)
    # Check the response
    if response.status_code == 200:
        print('Web link created successfully')
    else:
        print(f'Error creating web link: {response.text}')



#create_conf_page()
#jira_on_conf()


