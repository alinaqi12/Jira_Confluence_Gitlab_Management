import requests
from requests.auth import HTTPBasicAuth
import json

def get_pages():
    auth = HTTPBasicAuth("arttechmania@gmail.com", "ATATT3xFfGF0vGeuHzmznOfX0WYkVQ4xeZMpfDL_JZSQ8PS6DtvRMF1Jpx0PUpO752tXh4mPaFOMCRIqZ4_P4IWs96WwaHPREs6zemwNVpR1l6W1-fZBiMlNWVhKQ8oas8tQHlKB96ci8CUTOxeuzFG-BRGs09Q3zwblza8npUpWCTJWN6vsw-g=D7BE4289")

    # Set the base URL for your Confluence instance
    # confluence_base_url = 'https://your-confluence-instance.atlassian.net'
    base_url = 'https://artechmania.atlassian.net'


    # Get the current space id
    # Chanage according to requirement
    conf_url = f'{base_url}/wiki/rest/api/content/'
    response = requests.get(conf_url, auth=auth)
    pageID = response.json()["results"][6]["id"]
    # pageID = response.json()

    return pageID
