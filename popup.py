import tkinter as tk
from tkinter.font import Font
from JIRA_api import Create_Issue,Update_Issue
from gitlab import Gitlab_Issue
from conf_nd_link import create_conf_page
import sys




root = tk.Tk()
root.withdraw()

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set popup window dimensions
popup_width = 380
popup_height = 380

# Calculate the position for the bottom-right corner
pos_x = screen_width - popup_width - 10
pos_y = screen_height - popup_height - 10
# print(pos_x,pos_y)
# print(screen_width,screen_height)
# # Set the position of the window
#popup_geometry = f"{popup_width}x{popup_height}+{pos_x}+{pos_y}"
popup_geometry = f"{popup_width}x{popup_height}+{pos_x}+{pos_y}"
# print(popup_geometry)
root.geometry(popup_geometry)

popup_thread = None  # Global variable to hold the popup thread


def show_popup(subject, body):
    

    def issue_created():
        Create_Issue(subject, body)
        # print("successfully created issue")

    def update_jira_ticket():
        Update_Issue(subject, body)
        # print("successfully updated issue")

    def create_confluence_protocol():
        create_conf_page(subject,body)
        #pass

    def create_gitlab_issue():
        body1 = [body]
        Gitlab_Issue(subject, body1)
        # print("Created Gitlab Issue")

    popup = tk.Toplevel(root)
    popup.title("Choose What to do? ")
    popup.configure(bg="#009BE8")

    label_font = Font(family="Arial", size=14, weight="bold")
    button_font = Font(family="Arial", size=12, weight="bold")

    def close_popup():
        popup.destroy()
        #quit_thread()
        root.destroy()  # Close the entire script

    close_button = tk.Button(
        popup,
        text="X",
        command=close_popup,
        font=label_font,
        relief="solid",
        
        bd=0,
        bg="#009BE8",
        fg="red",
        activebackground="#009BE8",
        activeforeground="red",
    )
    close_button.place(x=225, y=0, anchor="ne")

    create_jira_btn = tk.Button(
        popup,
                bg="#009BE8",
        fg="white",
        activebackground="#009BE8",
        activeforeground="blue",
        text="Create Jira Ticket",
        command=issue_created,
        highlightthickness=0,
        font=button_font,
        relief="solid",
        bd=0
    )
    create_jira_btn.pack(pady=10)

    update_jira_btn = tk.Button(
        popup,    
        bg="#009BE8",
        fg="white",
        activebackground="#009BE8",
        activeforeground="blue",
        text="Update Jira Ticket",
        command=update_jira_ticket,
        font=button_font,
        relief="solid",
        bd=0,
    )
    update_jira_btn.pack(pady=10)

    create_confluence_btn = tk.Button(
        popup,
        bg="#009BE8",
        fg="white",
        activebackground="#009BE8",
        activeforeground="blue",
        text="Create Confluence Protocol",
        command=create_confluence_protocol,
        font=button_font,
        relief="solid",
        bd=0,
    )
    create_confluence_btn.pack(pady=10)

    create_gitlab_btn = tk.Button(
        popup,
        bg="#009BE8",
        fg="white",
        activebackground="#009BE8",
        activeforeground="blue",
        text="Create GitLab Issue",
        command=create_gitlab_issue,
        font=button_font,
        relief="solid",
        bd=0,
    )
    create_gitlab_btn.pack(pady=10)
    #print("HELLO")
    root.mainloop()    


def Display_popup(subject, body):
    global popup_thread

    def task():
        show_popup(subject, body)
        
    task()
    #root.after(0, task)


def quit_thread():
    global popup_thread

    if popup_thread is not None and popup_thread.is_alive():
        popup_thread.join()  # Wait for the thread to finish
        popup_thread = None  # Reset the popup thread


subject=sys.argv[1]
description=sys.argv[2]
#print(subject,description)
Display_popup(subject,description)