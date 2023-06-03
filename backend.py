import win32com.client
import pythoncom
import threading
from queue import Queue

from popup import Display_popup

# Define event handlers
queue = Queue()

class OutlookHandler:
    def __init__(self):
        self.inbox = None

    def OnItemAdd(self, item):
        if item.UnRead:
            Subject = str(item.Subject)
            Body= str(item.Body)
            def task2():
                Display_popup(Subject, Body)
            queue.put((Subject, Body))

            print("Hello, new unread mail received!")
            print("Subject:", Subject)
            print("Body:", Body)

            # Start a new thread to display the popup
            thread2 = threading.Thread(target=Display_popup, name="Thread 2", args=(queue,))
            thread2.start()

            print("Popup displayed")
            item.UnRead = False  # Mark the item as read

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