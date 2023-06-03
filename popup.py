import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter.font import Font
import ctypes
from JIRA_api import Create_Issue,Update_Issue
from gitlab import Gitlab_Issue
from queue import Queue
from conf_nd_link import create_conf_page

def show_popup(subject,body):
    def issue_created():
        Create_Issue(subject,body)
        print("successfully created issue")

    def update_jira_ticket():
        Update_Issue(subject,body)
        print("successfully updated issue")
    
    def create_confluence_protocol():
        create_conf_page()
                
    def create_gitlab_issue():
        body1=[body]
        Gitlab_Issue(subject,body1)
        print("Created Gitlab Issue")
    
    
    popup = tk.Toplevel()
    popup.title("Choose an Action")
    popup.configure(bg="#F0F0F0")
    popup.overrideredirect(True)  # Remove the window border
    
    label_font = Font(family="Arial", size=14, weight="bold")
    button_font = Font(family="Arial", size=12, weight="bold")
    

    def close_popup():
        popup.destroy()
        root.destroy()  # Close the entire script
    
    close_button = tk.Button(popup, text="X", command=close_popup, font=label_font, relief="solid", bd=0, bg="#F0F0F0",
                             fg="red", activebackground="#F0F0F0", activeforeground="red")
    close_button.place(x=225, y=5, anchor="ne")
    
    create_jira_btn = tk.Button(popup, text="Create Jira Ticket", command=issue_created,
                                font=button_font, relief="solid", bd=1)
    create_jira_btn.pack(pady=10)
    
    update_jira_btn = tk.Button(popup, text="Update Jira Ticket", command=update_jira_ticket,
                                font=button_font, relief="solid", bd=1)
    update_jira_btn.pack(pady=10)
    
    create_confluence_btn = tk.Button(popup, text="Create Confluence Protocol", command=create_confluence_protocol,
                                      font=button_font, relief="solid", bd=1)
    create_confluence_btn.pack(pady=10)
    
    create_gitlab_btn = tk.Button(popup, text="Create GitLab Issue", command=create_gitlab_issue,
                                  font=button_font, relief="solid", bd=1)
    create_gitlab_btn.pack(pady=10)

root = tk.Tk()
root.withdraw()

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set popup window dimensions
popup_width = 250
popup_height = 300

# Calculate the position for the bottom-right corner
pos_x = screen_width - popup_width - 10
pos_y = screen_height - popup_height - 10

# Set the position of the window
popup_geometry = f"{popup_width}x{popup_height}+{pos_x}+{pos_y}"
root.geometry(popup_geometry)
def Display_popup(queue):
    subject, body = queue.get()
    show_popup(subject,body)
    root.mainloop()
#Display_popup('hELLP','HEELA')