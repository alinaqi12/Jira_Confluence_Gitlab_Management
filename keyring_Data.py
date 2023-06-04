import keyring

# Store a password in the keyring
# service_name = "JIRA"
# username = "PUT YOU JIRA USERNAME HERE LIKE: abc@gmail.com"
# API_TOKEN = "PUT YOUR JIRA API TOKEN HERE"
# keyring.set_password(service_name,username, API_TOKEN)

# service_name = "GITLAB"
# API_TOKEN = "PUT YOUR GITLAB API TOKEN HERE"
# username=""
# keyring.set_password(service_name, username,API_TOKEN )

# service_name = "Confluence"
# API_TOKEN = "PUT YOUR GITLAB API TOKEN HERE"
# username=""
# keyring.set_password(service_name, username,API_TOKEN )

service_name = "JIRA"
username = "salinaqi57@gmail.com"
API_TOKEN = "ATATT3xFfGF0zK6F6t7ygfEM2eFjn7XnSaEQ84BXGen6iMuM3TZ6ZmNeURmK72axiLQrJpJGrLb0z7RxcViqsgiO9w3HRwT8lwTTuRkCTPDWFWPWes_LqU2EC29wX5P7zxJcOpEeW5uI2psb70Yke_PnmfzZCdp60M8gpJJttcxQRulBLaJgU4Q=AA359187"
keyring.set_password(service_name,username, API_TOKEN)

service_name = "GITLAB"
API_TOKEN = "glpat-fexzj5xNVq8wsDuzxCpF"
username=""
keyring.set_password(service_name, username,API_TOKEN )

service_name = "Confluence"
API_TOKEN = "ATCTT3xFfGN0hHaXm9fu81f5G73H72o8R6gkDepMIDEj9XhHhfsnZrbjwSm7KqEedQsQgFUuLrdb8MszU47-tAJG9XZYP37yMTU9GopFmBHdI0VZBHM0TFZKLaTjF8qtoyG8yRTRnS_3-R4bo4SbD3ktfdDvSu6BfT7JU7_NWySEwxDhuQcAtSk=74C3BCC3"
username=""
keyring.set_password(service_name, username,API_TOKEN )

# Retrieve the password from the keyring
# retrieved_password = keyring.get_password(service_name, username)
# print("Retrieved password:", retrieved_password)
