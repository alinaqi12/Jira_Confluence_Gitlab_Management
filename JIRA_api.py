import requests
from dotenv import load_dotenv
load_dotenv()
import os
import keyring

YOUR_DOMAIN_NAME=os.getenv("YOUR_DOMAIN_NAME_JIRA")
username = os.getenv("username_JIRA")

api_token=keyring.get_password("JIRA",username)
api_url_ISSUE= f'https://{YOUR_DOMAIN_NAME}.atlassian.net/rest/api/2/issue/'
api_url3_GET_ISSUES=f"https://{YOUR_DOMAIN_NAME}.atlassian.net/rest/api/2/search?jql=ORDER%20BY%20Created&maxResults=200"
Project_Key=os.getenv("Project_Key_JIRA")
issuetype_Name=os.getenv("issuetype_Name_JIRA")

headers = {
    'Accept': '*/*',
    'Content-Type': 'application/json'
    }

def Create_Issue(summary='Default Summary',description='Default Description',issuetype_name=issuetype_Name):
# Payload for creating a new issue
    payload = {
        "fields": {
        "project":
        {
            "key": Project_Key
        }
        ,
        "summary": summary,
        "description": description,
        "issuetype": {
            "name": issuetype_name
        }
    }
    }

    try:
        # Send a POST request to create a new issue
        response = requests.post(api_url_ISSUE, auth=(username, api_token), headers=headers, json=payload)

        # Check the response status code
        if response.status_code == 201 :
            issue_key = response.json().get('key')
            print('New issue created successfully. Key:', issue_key)
        else:
            print('Failed to create issue. Status Code:', response.status_code)
            print('Response:')

    except requests.exceptions.RequestException as e:
        print('An error occurred:', e)
    
def Update_Issue(summary='Default Summary',description='Default Description'):
    # Payload for creating a new issue
    Res = requests.get(api_url3_GET_ISSUES,headers=headers,auth=(username, api_token))
    data=Res.json()
    Res1=data['issues']
    Temp_Dict=[]
    issue_key=''
    for index, item in enumerate(Res1):
        Key=item['key']
        id=item['id']
        summary1=item['fields']['summary']
        Temp_Dict.append({"Key":Key,'id':id,'summary':summary1})
        #print(summary)
        summary.replace(' ','')
        summary.lower()
        
        summary1.replace(' ','')
        summary1.lower()
        if summary==summary1:
            ID=id
            issue_key=id
        
    payload = {
        "fields": {
        "description": description
    }
    }
    if issue_key=='':
        KeyOfIssue=Create_Issue(summary,description,issuetype_name=issuetype_Name)
        print("No Previous issue found, Created New issue with id : ", KeyOfIssue)
    try:
        # Send a POST request to create a new issue
        response = requests.put((api_url_ISSUE+issue_key), auth=(username, api_token), headers=headers, json=payload)

        # Check the response status code
        if response.status_code == 201 :
            issue_key = response.json().get('key')
            print('Issue Updated successfully. Key:', issue_key)
        else:
            print('Status Code:', response.status_code)
            print('Response:')

    except requests.exceptions.RequestException as e:
        print('An error occurred:', e)

