import subprocess
import argparse
import tkinter as tk
from tkinter import *
from tkinter import ttk

def run_script(arg1, arg2):
    cmd = ["python", "popup.py", arg1, arg2]
    subprocess.call(cmd)

run_script('helo','world')