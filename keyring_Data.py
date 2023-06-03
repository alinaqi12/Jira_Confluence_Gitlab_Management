import keyring

# Store a password in the keyring
service_name = "JIRA"
username = "PUT YOU JIRA USERNAME HERE LIKE: abc@gmail.com"
API_TOKEN = "PUT YOUR JIRA API TOKEN HERE"
keyring.set_password(service_name,username, API_TOKEN)

service_name = "GITLAB"
API_TOKEN = "PUT YOUR GITLAB API TOKEN HERE"
username=""
keyring.set_password(service_name, username,API_TOKEN )

# Retrieve the password from the keyring
# retrieved_password = keyring.get_password(service_name, username)
# print("Retrieved password:", retrieved_password)
