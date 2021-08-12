import tkinter as TK
from tkinter import Label, filedialog, Text
import os

root = TK.Tk()
apps = []

if os.path.isfile('App.txt'):
    with open('App.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=((".exe", "*.exe"), ("all files", "*.*")))

    apps.append(filename)

    for app in apps:
        label = TK.Label(frame, text=app, bg="grey")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)


canvas = TK.Canvas(root, height=500, width=500, bg="#263d42")
canvas.pack()

frame = TK.Frame(root, bg='#fff')
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1)

openFile = TK.Button(root, text="Open File",
                     padx=10, pady=5, fg="#fff", bg="#263d42", command=addApp)
openFile.pack()

runApps = TK.Button(root, text="Run Apps",
                    padx=10, pady=5, fg="#fff", bg="#263d42", command=runApps)
runApps.pack()

for app in apps:
    label = TK.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('App.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
