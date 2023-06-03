import requests
from dotenv import load_dotenv
load_dotenv()
import keyring
import os

Project_ID=os.getenv("Project_ID_Gitlab")
Gitlab_Instance='https://gitlab.com/'

api_url = f"{Gitlab_Instance}/api/v4/projects/{Project_ID}/issues"
access_token = keyring.get_password("GITLAB","")

issue_title = "Issues Default"
issue_labels = ["bug"]

headers = {
    "PRIVATE-TOKEN": access_token,
}
def Gitlab_Issue(issue_title,issue_labels):
    params = {
        "title": issue_title,
        "labels": ",".join(issue_labels),
    }

    # Send the POST request to create the issue
    response = requests.post(api_url, headers=headers, params=params)
    # Check the response status code
    if response.status_code == 201:
        print("Issue created successfully!")
        return response.status_code
    else:
        print("Failed to create the issue. Status code:", response.status_code)
        print("Error message:", response)
        return response.status_code
#Gitlab_Issue("HELLO","NEW ISSUE")