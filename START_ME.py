import win32com.client
import pythoncom
from concurrent.futures import ThreadPoolExecutor
import subprocess
import argparse
#from popup import Display_popup
import threading

def run_script(arg1,arg2):
    cmd = ["python", "popup.py",arg1,arg2]
    subprocess.call(cmd)
def task2(arg1, arg2):
    threading.Thread(target=run_script, args=(arg1, arg2)).start()
class OutlookHandler:
    def __init__(self):
        self.inbox = None

    def OnItemAdd(self, item):
        if item.UnRead:
            Subject = str(item.Subject)
            Body= str(item.Body)
            print("Hello, new unread mail received!")
            print("Subject:", Subject)
            print("Body:", Body)
            item.UnRead = False
            task2(Subject, Body)

            print("Popup displayed")
              # Mark the item as read

    def ProcessInbox(self):
        if self.inbox:
            items = self.inbox.Items
            latest_email = items.GetLast()
            if latest_email:
                self.OnItemAdd(latest_email)


# Create an instance of the Outlook Application object
def Start():
    # Initialize COM library
    pythoncom.CoInitialize()

    outlook = win32com.client.Dispatch("Outlook.Application")

    # Create an instance of the Outlook event handler
    event_handler = OutlookHandler()

    # Get the Inbox folder
    namespace = outlook.GetNamespace("MAPI")
    event_handler.inbox = namespace.GetDefaultFolder(6)  # 6 corresponds to the Inbox folder

    # Process existing items (Latest Email)
    event_handler.ProcessInbox()

    # Keep the script running to continue checking for new mail
    while True:
        event_handler.ProcessInbox()

# Start the script
Start()
