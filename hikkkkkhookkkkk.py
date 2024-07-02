import tkinter as tk
from tkinter import *
from tkinter import messagebox, PhotoImage, Label, Button
from tkinter import Canvas, Tk
import os
import pandas as pd

from PIL import Image, ImageTk
from PyQt5 import QtCore, QtGui, QtWidgets


import Data.static_partition as sp
import Data.dynamic_firstfit as df
import Data.dynamic_bestfit as db
import pandas as pd
import itertools
import json
import sys
import fcn
import os
import re


default_entry = 5
default_partition_count = 3
usrfile_name = 'Untitled'
global pick
pick = 'fcfs'


file = open('usr_preferences.json')
data = json.load(file)

Theme = data['Theme']
Recent_Files = data['Recent Files']
Style = data['Style']

file.close()


# Helper function to load images safely
def load_image(image_path):
    try:
        return PhotoImage(file=image_path)
    except Exception as e:
        print(f"Error: {e}")
        return None

# Get the current directory
try:
    currentDirectory = os.getcwd()
except:
    print("Error: Cannot find the Current Directory.")

root = tk.Tk()
root.title("Single Contiguous Memory Management")
root.resizable(width=False, height=False)
root.geometry("950x750")

# Load images
windowbg = load_image("windowbg.png")
if windowbg:
    windowbg_label = Label(root, image=windowbg)
    windowbg_label.place(x=0, y=0, relwidth=1, relheight=1)

image_1 = load_image("sizebtnbg.png")
image_2 = load_image("sizebtnbg1.png")
image_3 = load_image("frontlogo.png")
image_4 = load_image("entrytopper1.png")
image_5 = load_image("entrytopper.png")
image_6 = load_image("info.png")
image_7 = load_image("homebtn.png")
image_8 = load_image("groupname.png")
image_9 = load_image("STATICTOPPER.png")

BUTTONOPT1 = load_image('HEADERB1.png')
BUTTONOPT2 = load_image('HEADERB2.png')
BUTTONOPT3 = load_image('HEADERB3.png')
BUTTONOPT4 = load_image('HEADERB4.png')
BUTTONSPEC1 = load_image('SPEC1.png')
BUTTONSPEC2 = load_image('SPEC2.png')
BUTTONSPEC3 = load_image('SPEC3.png')
BUTTONSPEC4 = load_image('SPEC4.png')

class mainUI:
    def __init__(self):
        self.basicWidgetList = []

    def __init__(self, mainscreen, app):
        self.app = app

    def go_back(self):
        self.back_button.place_forget()
        self.clearWidgets()

    def clearWidgets(self):
        for widget in self.basicWidgetList:
            widget.destroy()
        self.basicWidgetList = []

    def os_size_value(self):
        for widget in self.basicWidgetList:
            self.basicWidgetList = []

    def memory_size_value(self):
        for widget in self.basicWidgetList:
            self.basicWidgetList = []



    def mainscreen(self):
        self.clearWidgets()

        if image_3:
            self.mainscreenlogo = Label(root, image=image_3, borderwidth="0", highlightthickness="0", relief="flat", activebackground="black", background="black")
            self.mainscreenlogo.place(x=0, y=0)
            self.basicWidgetList.append(self.mainscreenlogo)

        self.bg1LBL = Label(root, bg="black")
        self.bg1LBL.place(x=0, y=0)
        self.basicWidgetList.append(self.bg1LBL)

        if BUTTONOPT2:
            self.LOGOBUTTON1 = Button(root, image=BUTTONOPT2, command=self.mainInput1_window, bg="#f77f00", relief="sunken")
            self.LOGOBUTTON1.place(x=40, y=500)
            self.basicWidgetList.append(self.LOGOBUTTON1)

        if BUTTONOPT3:
            self.LOGOBUTTON2 = Button(root, image=BUTTONOPT3, command=self.staticmainInput1_window, bg="#f77f00", relief="sunken")
            self.LOGOBUTTON2.place(x=330, y=500)
            self.basicWidgetList.append(self.LOGOBUTTON2)

        if BUTTONOPT4:
            self.LOGOBUTTON3 = Button(root, image=BUTTONOPT4, command=self.mainscreen1,bg="#f77f00", relief="sunken")
            self.LOGOBUTTON3.place(x=610, y=500)
            self.basicWidgetList.append(self.LOGOBUTTON3)

        if image_6:
            self.LOGOBUTTON5 = Button(root, image=image_6, command=self.Batmassonic_screen, bg="#f77f00", relief="sunken")
            self.LOGOBUTTON5.place(x=20, y=20)
            self.basicWidgetList.append(self.LOGOBUTTON5)

    def mainscreen1(self):
        self.clearWidgets()
        self.basicWidgetList = []

        self.bg1LBL1 = Label(root, bg="black")
        self.bg1LBL1.place(x=0, y=0)
        self.basicWidgetList.append(self.bg1LBL1)

        if image_5:
            self.LOGOBUTTONA = Label(root, image=image_5, bg="#f77f00", relief="sunken")
            self.LOGOBUTTONA.place(x=0, y=0)
            self.basicWidgetList.append(self.LOGOBUTTONA)

        if BUTTONOPT1:
            self.LOGOBUTTON7 = Button(root, image=BUTTONOPT1, bg="#f77f00",
                                      relief="sunken")
            self.LOGOBUTTON7.place(x=0, y=100)
            self.basicWidgetList.append(self.LOGOBUTTON7)

        if BUTTONSPEC1:
            self.LOGOBUTTON8 = Button(root, image=BUTTONSPEC1, bg="#f77f00", relief="sunken")
            self.LOGOBUTTON8.place(x=160, y=250)
            self.basicWidgetList.append(self.LOGOBUTTON8)

        if BUTTONSPEC2:
            self.LOGOBUTTON9 = Button(root, image=BUTTONSPEC2, bg="#f77f00", relief="sunken")
            self.LOGOBUTTON9.place(x=520, y=250)
            self.basicWidgetList.append(self.LOGOBUTTON9)

        if BUTTONSPEC3:
            self.LOGOBUTTON10 = Button(root, image=BUTTONSPEC3, bg="#f77f00", relief="sunken")
            self.LOGOBUTTON10.place(x=160, y=400)
            self.basicWidgetList.append(self.LOGOBUTTON10)

        if BUTTONSPEC4:
            self.LOGOBUTTON11 = Button(root, image=BUTTONSPEC4, bg="#f77f00", relief="sunken")
            self.LOGOBUTTON11.place(x=520, y=400)
            self.basicWidgetList.append(self.LOGOBUTTON11)

        self.back_button = Button(root, text="Back", command = self.mainscreen,
            font =('Poppins', 18, 'bold'), fg = 'white', width=20, bg = '#4b3621', height = 2, borderwidth = 4, relief = 'sunken')

        self.back_button.place(x = 300, y = 560)
        self.basicWidgetList.append(self.back_button)


    def mainInput1_window(self):
        self.clearWidgets()
        self.basicWidgetList = []

        self.entry_frame = Frame(root, bg="black")
        self.entry_frame.place(x=50, y=110)
        self.basicWidgetList.append(self.entry_frame)

        # Adding a picture to the input screen
        self.header = Button(root, image=image_4, bg="#000000", relief="flat", borderwidth=0)
        self.header.place(x=0, y=0)
        self.basicWidgetList.append(self.header)

        self.os_sizeLBL = Label(root, text="OS Size", font=('Poppins', 18, 'bold'), bg="#d3a075", height=2, width=19, borderwidth=4, relief="raised")
        self.os_sizeLBL.place(x=90, y=180)
        self.basicWidgetList.append(self.os_sizeLBL)

        self.entry_os_size = Entry(root, font=('Poppins', 30, 'bold'), justify="center", width=18)
        self.entry_os_size.place(x=390, y=180)
        self.basicWidgetList.append(self.entry_os_size)

        self.memory_sizeLBL = Label(root, text="Memory Size", font=('Poppins', 18, 'bold'), bg="#ecd3bf", height=2, width=19, borderwidth=4, relief="raised")
        self.memory_sizeLBL.place(x=90, y=250)
        self.basicWidgetList.append(self.memory_sizeLBL)

        self.entry_memory_size = Entry(root, font=('Poppins', 30, 'bold'), justify="center", width = 18)
        self.entry_memory_size.place(x=390, y=250)
        self.basicWidgetList.append(self.entry_memory_size)

        self.job_numLBL = Label(root, text="Number of Jobs", font=('Poppins', 18, 'bold'), bg="#eec894", height=2, width=19, borderwidth=4, relief="raised")
        self.job_numLBL.place(x=90, y=320)
        self.basicWidgetList.append(self.job_numLBL)

        self.entry_job_num = Entry(root, font=('Poppins', 30, 'bold'), justify="center", width = 18)
        self.entry_job_num.place(x=390, y=320)
        self.basicWidgetList.append(self.entry_job_num)

        self.job_entries = []
        self.job_frame = Frame(self.entry_frame, bg="black")
        self.job_frame.grid(row=6, columnspan=5)
        self.basicWidgetList.append(self.job_frame)

        self.set_jobs_button = Button(root, text="Set Jobs", command=self.create_job_entries, font=('Poppins', 18, 'bold'), width=20, bg="#b8804c", height=2, borderwidth=4, relief="sunken")
        self.set_jobs_button.place(x=330, y=450)
        self.basicWidgetList.append(self.set_jobs_button)

        self.back_button = Button(root, text="Back", command = self.mainscreen,
            font =('Poppins', 18, 'bold'), fg = 'white', width=20, bg = '#4b3621', height = 2, borderwidth = 4, relief = 'sunken')

        self.back_button.place(x = 328, y = 550)
        self.basicWidgetList.append(self.back_button)

    def hide_initial_inputs(self):
        self.os_sizeLBL.place_forget()
        self.entry_os_size.place_forget()
        self.memory_sizeLBL.place_forget()
        self.entry_memory_size.place_forget()
        self.job_numLBL.place_forget()
        self.entry_job_num.place_forget()
        self.set_jobs_button.place_forget()
        self.header.place_forget()

    def create_job_entries(self):
        try:
            num_jobs = int(self.entry_job_num.get())
            for widget in self.job_frame.winfo_children():
                widget.destroy()
            self.job_entries.clear()

            self.hide_initial_inputs()


            for i in range(num_jobs):
                entry_job_size = Entry(self.job_frame, font=('Poppins', 10, 'bold'), justify="center", width=15)
                entry_job_size.grid(row=i, column=2, padx=20)
                Label(self.job_frame, text=f"Job {i + 1}", font=('Poppins', 10, 'bold'), bg="#000000", fg="#FFFFFF", width=9, relief="flat").grid(row=i, column=0)
                Label(self.job_frame, text=f"Job Size:", font=('Poppins', 9, 'bold'), bg="#D3A075", width=12, relief="groove").grid(row=i, column=1, padx=0)  # Add space on the right side

                entry_arrival = Entry(self.job_frame, font=('Poppins', 10, 'bold'), justify="center", width=15)
                entry_arrival.grid(row=i, column=4, padx=20)
                Label(self.job_frame, text=f" Arrival Time (ms):", font=('Poppins', 9, 'bold'), bg="#ECD3BF", width=15, relief="groove").grid(row=i, column=3, padx=0)  # Add space on the left side

                entry_runtime = Entry(self.job_frame, font=('Poppins', 10, 'bold'), justify="center", width=15)
                entry_runtime.grid(row=i, column=6, padx=20)
                Label(self.job_frame, text=f"Run Time (ms):", font=('Poppins', 9, 'bold'), bg="#EEC894", width=15, relief="groove").grid(row=i, column=5, padx=0)  # Add space on the left side

                self.job_entries.append((entry_job_size, entry_arrival, entry_runtime))
            # Create Compute Wait Times button after job entries are created
            self.compute_button = Button(root, text="Show Summary Table and Memory Map", command=self.summarytable, font=('Poppins', 18, 'bold'), width=30, bg="#b8804c", height=1, borderwidth=4, relief="sunken")
            self.compute_button.place(x=260, y=30)
            self.basicWidgetList.append(self.compute_button)


        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of jobs.")


    def summarytable(self):
        def __init__(self, master):
            self.master = master
            self.canvases = []
            for i in range(5):  # Create 5 Canvas widgets
                canvas = tk.Canvas(self.master, width=800, height=600)
                canvas.pack()
                self.canvases.append(canvas)

        try:
            os_size = int(self.entry_os_size.get())
            memory_size = int(self.entry_memory_size.get())
            jobs = []

            for entry_job_size, entry_arrival, entry_runtime in self.job_entries:
                job_size = int(entry_job_size.get())
                arrival_time = int(entry_arrival.get())
                runtime = int(entry_runtime.get())
                jobs.append({"Job Number": len(jobs) + 1, "Job Size": job_size, "Arrival Time": arrival_time,
                             "Runtime": runtime})
            canvas = Canvas(self.master, width=800, height=600)
            canvas.pack()

            # Sorting jobs by arrival time
            jobs = sorted(jobs, key=lambda x: x["Arrival Time"])

            current_time = 0
            for job in jobs:
                job["Finish Time"] = max(current_time, job["Arrival Time"]) + job["Runtime"]
                job["Wait Time"] = max(current_time - job["Arrival Time"], 0)
                current_time = job["Finish Time"]

            # Create a dataframe to display the jobs
            df = pd.DataFrame(jobs)
            job_sizes = [int(entry_job_size.get()) for entry_job_size, _, _ in self.job_entries]

            # Define data
            data = {
                'Memory size': memory_size,
                'OS size': os_size,
                'Jobs': jobs,
                'Arrival time': [job['Arrival Time'] for job in jobs],
                'Run time': [job['Runtime'] for job in jobs]
            }

            self.display_table(df, job_sizes, data, canvas)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for OS size, Memory size, and job details.")

    def display_table(self, df, job_sizes, data, canvas):
        self.clearWidgets()
        self.basicWidgetList = []

        self.sumtablelabel = Label(root, text="Summary Table", font=('Poppins', 18, 'bold'), bg="#ecd3bf", height=2,
                                   width=19,
                                   borderwidth=4, relief="raised")
        self.sumtablelabel.place(x=140, y=15)
        self.basicWidgetList.append(self.sumtablelabel)

        self.memmaplabel = Label(root, text="Memory Map", font=('Poppins', 18, 'bold'), bg="#ecd3bf", height=2,
                                 width=19,
                                 borderwidth=4, relief="raised")
        self.memmaplabel.place(x=600, y=15)
        self.basicWidgetList.append(self.memmaplabel)

        # Add headers

        headers = ["Job Number", "Job Size", "Arrival Time", "Runtime", "Finish Time", "Wait Time"]
        for col_num, header in enumerate(headers):
            header_label = Label(root, text=header, font=('Poppins', 10, 'bold'), bg="#eec894", width=10, borderwidth=4,
                                 relief="raised")
            header_label.grid(row=0, column=col_num, padx=(7, 3), pady=(85, 1))
            self.basicWidgetList.append(header_label)

        # Add rows
        for row_num, row in df.iterrows():
            for col_num, value in enumerate(row):
                cell_label = Label(root, text=value, font=('Poppins', 10, 'bold'), bg="#FFFFFF", width=10,
                                   borderwidth=4, relief="raised")
                cell_label.grid(row=row_num + 1, column=col_num, padx=(7, 3))
                self.basicWidgetList.append(cell_label)

        self.memory_map_frame = Frame(root, bg='black')
        self.memory_map_frame.place(x=650, y=90)
        self.basicWidgetList.append(self.memory_map_frame)

        MEMORY_SIZE = data['Memory size']
        OS_SIZE = data['OS size']

        jobs = data['Jobs']
        arrival_time = data['Arrival time']
        run_time = data['Run time']

        self.canvas = Canvas(self.memory_map_frame, width=400, height=200, bg='white')
        self.canvas.pack()
        self.basicWidgetList.append(self.canvas)

        self.canvas.create_rectangle(10, 10, 390, 190, fill='gray')
        x = 100
        for job_size in job_sizes:
            self.canvas.create_rectangle(x, 190, x + job_size, 190, fill='blue')
            x += job_size + 10


        # Draw memory map
        #canvas.create_rectangle(10, 10, 390, 190, fill="gray")
        #x = 10
        #for job_size in job_sizes:
            #canvas.create_rectangle(x, 10, x + job_size, 190, fill="blue")
            #x += job_size + 10


        self.back_button = Button(root, text="Back", command=self.mainscreen1,

                                  font=('Poppins', 18, 'bold'), fg="white", width=20, bg="#4b3621", height=2,
                                  borderwidth=4,
                                  relief="sunken")
        self.back_button.place(x=300, y=550)
        self.basicWidgetList.append(self.back_button)

    def Batmassonic_screen(self):
        self.clearWidgets()
        self.mainscreenlogo = Label(root, image=image_8, borderwidth="0", highlightthickness="0", relief="flat", activebackground="black", background="black")
        self.mainscreenlogo.place(x=0, y=0)
        self.basicWidgetList.append(self.mainscreenlogo)

        if image_7:
            self.LOGOBUTTON6 = Button(root, image=image_7, command=self.mainscreen, bg="#f77f00", relief="sunken")
            self.LOGOBUTTON6.place(x=20, y=20)
            self.basicWidgetList.append(self.LOGOBUTTON6)

    def staticmainInput1_window(self):
        self.clearWidgets()
        self.basicWidgetList = []

        self.STATIC_entry_frame = Frame(root, bg="black")
        self.STATIC_entry_frame.place(x=50, y=110)
        self.basicWidgetList.append(self.STATIC_entry_frame)

        # Adding a picture to the input screen
        self.STATIC_header = Button(root, image=image_9, bg="#000000", relief="flat", borderwidth=0)
        self.STATIC_header.place(x=0, y=0)
        self.basicWidgetList.append(self.STATIC_header)

        self.STATIC_os_sizeLBL = Label(root, text="OS Size", font=('Poppins', 18, 'bold'), bg="#d3a075", height=2,
                                       width=19,
                                       borderwidth=4, relief="raised")
        self.STATIC_os_sizeLBL.place(x=90, y=180)
        self.basicWidgetList.append(self.STATIC_os_sizeLBL)

        self.STATIC_entry_os_size = Entry(root, font=('Poppins', 30, 'bold'), justify="center", width = 18)
        self.STATIC_entry_os_size.place(x=390, y=180)
        self.basicWidgetList.append(self.STATIC_entry_os_size)

        self.STATIC_memory_sizeLBL = Label(root, text="Memory Size", font=('Poppins', 18, 'bold'), bg="#ecd3bf",
                                           height=2,
                                           width=19, borderwidth=4, relief="raised")
        self.STATIC_memory_sizeLBL.place(x=90, y=250)
        self.basicWidgetList.append(self.STATIC_memory_sizeLBL)

        self.STATIC_entry_memory_size = Entry(root, font=('Poppins', 30, 'bold'), justify="center", width = 18)
        self.STATIC_entry_memory_size.place(x=390, y=250)
        self.basicWidgetList.append(self.STATIC_entry_memory_size)

        self.STATIC_job_numLBL = Label(root, text="Number of Jobs", font=('Poppins', 18, 'bold'), bg="#eec894",
                                       height=2,
                                       width=19, borderwidth=4, relief="raised")
        self.STATIC_job_numLBL.place(x=90, y=320)
        self.basicWidgetList.append(self.STATIC_job_numLBL)

        self.STATIC_entry_job_num = Entry(root, font=('Poppins', 30, 'bold'), justify="center", width = 18)
        self.STATIC_entry_job_num.place(x=390, y=320)
        self.basicWidgetList.append(self.STATIC_entry_job_num)

        self.STATIC_partition_sizeLBL = Label(root, text="Partition Size(comma-separated)",
                                              font=('Poppins', 18, 'bold'),
                                              bg="#b8804c", height=2, width=25, borderwidth=4, relief="raised")
        self.STATIC_partition_sizeLBL.place(x=90, y=390)
        self.basicWidgetList.append(self.STATIC_partition_sizeLBL)

        self.STATIC_entry_partition_sizes = Entry(root, font=('Poppins', 30, 'bold'), justify="center", width=14)
        self.STATIC_entry_partition_sizes.place(x=480, y=390)
        self.basicWidgetList.append(self.STATIC_entry_partition_sizes)

        self.STATIC_set_jobs_button = Button(root, text="Set Jobs", command=self.STATIC_create_job_entries,
                                             font=('Poppins', 18, 'bold'), width=20, bg="#b8804c", height=2,
                                             borderwidth=4,
                                             relief="sunken")
        self.STATIC_set_jobs_button.place(x=330, y=470)
        self.basicWidgetList.append(self.STATIC_set_jobs_button)

        self.back_button = Button(root, text="Back", command = self.mainscreen,
            font =('Poppins', 18, 'bold'), fg = 'white', width=20, bg = '#4b3621', height = 2, borderwidth = 4, relief = 'sunken')

        self.back_button.place(x = 328, y = 560)
        self.basicWidgetList.append(self.back_button)


def suppress_qt_warnings():
    os.environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    os.environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    os.environ["QT_SCALE_FACTOR"] = "1"


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


    def goto_static_partition(self):
        self.new_window = MyWindow()
        self.activate_window = SP_InputWindow(self.new_window)
        self.new_window.show()
        self.mainscreen.hide()

    def goto_dynamic_partition(self):
        self.new_window = MyWindow()
        self.activate_window = DP_InputWindow(self.new_window)
        self.new_window.show()
        self.mainscreen.hide()

    # Partitioned Allocation
class SP_InputWindow:
    def __init__(self, mainscreen, app):
        self.app = app
        self.mainscreen = mainscreen
        self.job_entries = {}
        self.size_entries = {}
        self.arrival_entries = {}
        self.run_entries = {}
        self.partition_nums = {}
        self.partition_sizes = {}
        self.csv_loaded_successful = False
        self.active_file = ''
        self.max_size = 0
        self.remaining_size = 0
        self.max_partition = 0
        mainscreen.setObjectName("mainscreen")
        mainscreen.setWindowIcon(QtGui.QIcon(resource_path('Images\MMWINDOWBG.png')))
        mainscreen.setFixedSize(917, 655)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainscreen.sizePolicy().hasHeightForWidth())
        mainscreen.setSizePolicy(sizePolicy)
        mainscreen.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        mainscreen.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(mainscreen)
        self.centralwidget.setObjectName("centralwidget")
        self.Group_job_details = QtWidgets.QGroupBox(self.centralwidget)
        self.Group_job_details.setGeometry(QtCore.QRect(370, 30, 531, 551))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.Group_job_details.setFont(font)
        self.Group_job_details.setObjectName("Group_job_details")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Group_job_details)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 10, 25, 10)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.job_label = QtWidgets.QLabel(self.Group_job_details)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.job_label.sizePolicy().hasHeightForWidth())
        self.job_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.job_label.setFont(font)
        self.job_label.setAlignment(QtCore.Qt.AlignCenter)
        self.job_label.setObjectName("job_label")
        self.horizontalLayout_3.addWidget(self.job_label)
        self.size_label = QtWidgets.QLabel(self.Group_job_details)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.size_label.sizePolicy().hasHeightForWidth())
        self.size_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.size_label.setFont(font)
        self.size_label.setAlignment(QtCore.Qt.AlignCenter)
        self.size_label.setObjectName("size_label")
        self.horizontalLayout_3.addWidget(self.size_label)
        self.arrival_label = QtWidgets.QLabel(self.Group_job_details)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.arrival_label.sizePolicy().hasHeightForWidth())
        self.arrival_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.arrival_label.setFont(font)
        self.arrival_label.setAlignment(QtCore.Qt.AlignCenter)
        self.arrival_label.setObjectName("arrival_label")
        self.horizontalLayout_3.addWidget(self.arrival_label)
        self.runtime_label = QtWidgets.QLabel(self.Group_job_details)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runtime_label.sizePolicy().hasHeightForWidth())
        self.runtime_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.runtime_label.setFont(font)
        self.runtime_label.setAlignment(QtCore.Qt.AlignCenter)
        self.runtime_label.setObjectName("runtime_label")
        self.horizontalLayout_3.addWidget(self.runtime_label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.scrollArea = QtWidgets.QScrollArea(self.Group_job_details)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMouseTracking(True)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(2)
        self.scrollArea.setMidLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 488, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setAutoFillBackground(True)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setHorizontalSpacing(40)
        self.gridLayout.setVerticalSpacing(55)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, 150, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.import_csv_btn = QtWidgets.QPushButton(self.Group_job_details)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_csv_btn.sizePolicy().hasHeightForWidth())
        self.import_csv_btn.setSizePolicy(sizePolicy)
        self.import_csv_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.import_csv_btn.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setKerning(True)
        self.import_csv_btn.setFont(font)
        self.import_csv_btn.setToolTip(
            'Must have this order in your file:\n{job number, job size*, arrival time*, run time*}')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("Icons/table_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.import_csv_btn.setIcon(icon)
        self.import_csv_btn.setIconSize(QtCore.QSize(15, 15))
        self.import_csv_btn.setCheckable(False)
        self.import_csv_btn.setDefault(False)
        self.import_csv_btn.setFlat(True)
        self.import_csv_btn.setObjectName("import_csv_btn")
        self.horizontalLayout_4.addWidget(self.import_csv_btn)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(100, -1, -1, -1)
        self.horizontalLayout_5.setSpacing(30)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.rmv_entry_btn = QtWidgets.QPushButton(self.Group_job_details)
        self.rmv_entry_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(resource_path("Icons/minus.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rmv_entry_btn.setIcon(icon1)
        self.rmv_entry_btn.setIconSize(QtCore.QSize(20, 20))
        self.rmv_entry_btn.setCheckable(False)
        self.rmv_entry_btn.setDefault(False)
        self.rmv_entry_btn.setFlat(True)
        self.rmv_entry_btn.setObjectName("rmv_entry_btn")
        self.horizontalLayout_5.addWidget(self.rmv_entry_btn)
        self.add_entry_btn = QtWidgets.QPushButton(self.Group_job_details)
        self.add_entry_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(resource_path("Icons/plus-black-symbol.png")), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.add_entry_btn.setIcon(icon2)
        self.add_entry_btn.setIconSize(QtCore.QSize(20, 20))
        self.add_entry_btn.setCheckable(False)
        self.add_entry_btn.setDefault(False)
        self.add_entry_btn.setFlat(True)
        self.add_entry_btn.setObjectName("add_entry_btn")
        self.horizontalLayout_5.addWidget(self.add_entry_btn)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)
        self.Group_memSize = QtWidgets.QGroupBox(self.centralwidget)
        self.Group_memSize.setGeometry(QtCore.QRect(26, 114, 151, 81))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Group_memSize.setFont(font)
        self.Group_memSize.setObjectName("Group_memSize")
        self.memSize_value = QtWidgets.QSpinBox(self.Group_memSize)
        self.memSize_value.setGeometry(QtCore.QRect(14, 40, 121, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.memSize_value.sizePolicy().hasHeightForWidth())
        self.memSize_value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.memSize_value.setFont(font)
        self.memSize_value.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.memSize_value.setAlignment(QtCore.Qt.AlignCenter)
        self.memSize_value.setMaximum(999999999)
        self.memSize_value.setSingleStep(5)
        self.memSize_value.setProperty("value", 0)
        self.memSize_value.setObjectName("memSize_value")
        self.Group_osSize = QtWidgets.QGroupBox(self.centralwidget)
        self.Group_osSize.setGeometry(QtCore.QRect(206, 114, 141, 81))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Group_osSize.setFont(font)
        self.Group_osSize.setObjectName("Group_osSize")
        self.osSize_value = QtWidgets.QSpinBox(self.Group_osSize)
        self.osSize_value.setGeometry(QtCore.QRect(13, 40, 121, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.osSize_value.sizePolicy().hasHeightForWidth())
        self.osSize_value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.osSize_value.setFont(font)
        self.osSize_value.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.osSize_value.setAlignment(QtCore.Qt.AlignCenter)
        self.osSize_value.setMaximum(999999999)
        self.osSize_value.setSingleStep(5)
        self.osSize_value.setProperty("value", 0)
        self.osSize_value.setObjectName("osSize_value")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(800, 615, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.start_btn.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(resource_path("Icons/arrow_right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start_btn.setIcon(icon3)
        self.start_btn.setIconSize(QtCore.QSize(20, 20))
        self.start_btn.setCheckable(False)
        self.start_btn.setAutoDefault(False)
        self.start_btn.setDefault(False)
        self.start_btn.setFlat(True)
        self.start_btn.setObjectName("start_btn")
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(-10, 615, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.back_btn.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(resource_path("Icons/arrow_left.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon4)
        self.back_btn.setIconSize(QtCore.QSize(20, 20))
        self.back_btn.setCheckable(False)
        self.back_btn.setAutoDefault(False)
        self.back_btn.setDefault(False)
        self.back_btn.setFlat(True)
        self.back_btn.setObjectName("back_btn")
        self.pv_line = QtWidgets.QFrame(self.centralwidget)
        self.pv_line.setGeometry(QtCore.QRect(29, 260, 21, 35))
        self.pv_line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pv_line.setLineWidth(2)
        self.pv_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.pv_line.setObjectName("pv_line")

        self.pv_line2 = QtWidgets.QFrame(self.centralwidget)
        self.pv_line2.setGeometry(QtCore.QRect(324, 260, 21, 35))
        self.pv_line2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pv_line2.setLineWidth(2)
        self.pv_line2.setFrameShape(QtWidgets.QFrame.VLine)
        self.pv_line2.setObjectName("pv_line2")

        self.ph_line = QtWidgets.QFrame(self.centralwidget)
        self.ph_line.setGeometry(QtCore.QRect(38, 250, 297, 20))
        self.ph_line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ph_line.setLineWidth(2)
        self.ph_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.ph_line.setObjectName("ph_line")
        self.Group_MemPartition = QtWidgets.QGroupBox(self.centralwidget)
        self.Group_MemPartition.setGeometry(QtCore.QRect(26, 214, 321, 301))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.Group_MemPartition.setFont(font)
        self.Group_MemPartition.setFlat(False)
        self.Group_MemPartition.setCheckable(False)
        self.Group_MemPartition.setObjectName("Group_MemPartition")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Group_MemPartition)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Partition_verticalLayout = QtWidgets.QVBoxLayout()
        self.Partition_verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.Partition_verticalLayout.setSpacing(0)
        self.Partition_verticalLayout.setObjectName("Partition_verticalLayout")
        self.Partition_horizontalLayout = QtWidgets.QHBoxLayout()
        self.Partition_horizontalLayout.setContentsMargins(0, 10, 25, 10)
        self.Partition_horizontalLayout.setSpacing(0)
        self.Partition_horizontalLayout.setObjectName("Partition_horizontalLayout")
        self.partition_label = QtWidgets.QLabel(self.Group_MemPartition)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.partition_label.sizePolicy().hasHeightForWidth())
        self.partition_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.partition_label.setFont(font)
        self.partition_label.setAlignment(QtCore.Qt.AlignCenter)
        self.partition_label.setObjectName("partition_label")
        self.Partition_horizontalLayout.addWidget(self.partition_label)

        self.partition_size_label = QtWidgets.QLabel(self.Group_MemPartition)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.partition_size_label.sizePolicy().hasHeightForWidth())
        self.partition_size_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.partition_size_label.setFont(font)
        self.partition_size_label.setAlignment(QtCore.Qt.AlignCenter)
        self.partition_size_label.setObjectName("partition_size_label")
        self.Partition_horizontalLayout.addWidget(self.partition_size_label)
        self.Partition_verticalLayout.addLayout(self.Partition_horizontalLayout)
        self.Partition_scrollArea = QtWidgets.QScrollArea(self.Group_MemPartition)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Partition_scrollArea.sizePolicy().hasHeightForWidth())
        self.Partition_scrollArea.setSizePolicy(sizePolicy)
        self.Partition_scrollArea.setMouseTracking(True)
        self.Partition_scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.Partition_scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Partition_scrollArea.setLineWidth(2)
        self.Partition_scrollArea.setMidLineWidth(0)
        self.Partition_scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.Partition_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Partition_scrollArea.setWidgetResizable(True)
        self.Partition_scrollArea.setObjectName("Partition_scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 278, 69))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setAutoFillBackground(True)
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setContentsMargins(20, 20, 20, 20)
        self.gridLayout_4.setHorizontalSpacing(40)
        self.gridLayout_4.setVerticalSpacing(20)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Partition_scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.Partition_verticalLayout.addWidget(self.Partition_scrollArea)
        self.gridLayout_3.addLayout(self.Partition_verticalLayout, 0, 0, 1, 2)
        self.Partition_horizontalLayout_btn = QtWidgets.QHBoxLayout()
        self.Partition_horizontalLayout_btn.setContentsMargins(100, -1, -1, -1)
        self.Partition_horizontalLayout_btn.setSpacing(30)
        self.Partition_horizontalLayout_btn.setObjectName("Partition_horizontalLayout_btn")
        self.rmv_partition_btn = QtWidgets.QPushButton(self.Group_MemPartition)
        self.rmv_partition_btn.setText("")
        self.rmv_partition_btn.setIcon(icon1)
        self.rmv_partition_btn.setIconSize(QtCore.QSize(20, 20))
        self.rmv_partition_btn.setCheckable(False)
        self.rmv_partition_btn.setDefault(False)
        self.rmv_partition_btn.setFlat(True)
        self.rmv_partition_btn.setObjectName("rmv_partition_btn")
        self.Partition_horizontalLayout_btn.addWidget(self.rmv_partition_btn)
        self.add_partition_btn = QtWidgets.QPushButton(self.Group_MemPartition)
        self.add_partition_btn.setText("")
        self.add_partition_btn.setIcon(icon2)
        self.add_partition_btn.setIconSize(QtCore.QSize(20, 20))
        self.add_partition_btn.setCheckable(False)
        self.add_partition_btn.setDefault(False)
        self.add_partition_btn.setFlat(True)
        self.add_partition_btn.setObjectName("add_partition_btn")
        self.Partition_horizontalLayout_btn.addWidget(self.add_partition_btn)
        self.gridLayout_3.addLayout(self.Partition_horizontalLayout_btn, 1, 1, 1, 1)

        self.jv_line = QtWidgets.QFrame(self.centralwidget)
        self.jv_line.setGeometry(QtCore.QRect(373, 70, 21, 41))
        self.jv_line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.jv_line.setLineWidth(2)
        global dark
        if dark == True:
            self.jv_line.setStyleSheet('color: #FFFFFF')
        else:
            self.jv_line.setStyleSheet('color: #838383')
        self.jv_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.jv_line.setObjectName("jv_line")

        self.jv_line2 = QtWidgets.QFrame(self.centralwidget)
        self.jv_line2.setGeometry(QtCore.QRect(878, 70, 21, 41))
        self.jv_line2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.jv_line2.setLineWidth(2)
        if dark == True:
            self.jv_line2.setStyleSheet('color: #FFFFFF')
        else:
            self.jv_line2.setStyleSheet('color: #838383')
        self.jv_line2.setFrameShape(QtWidgets.QFrame.VLine)
        self.jv_line2.setObjectName("jv_line2")

        self.remaining_label_horizontalLayout = QtWidgets.QHBoxLayout()
        self.remaining_label_horizontalLayout.setContentsMargins(10, 5, 0, 0)
        self.remaining_label_horizontalLayout.setSpacing(30)
        self.remaining_label_horizontalLayout.setObjectName("remaining_label_horizontalLayout")

        self.remaining_label = QtWidgets.QLabel(self.Group_MemPartition)
        self.remaining_label.setFont(font)
        self.remaining_label.setToolTip('This will automatically added to your partition.')
        self.remaining_label.setObjectName('remaining_label')
        self.remaining_label.setGeometry(QtCore.QRect(302, 535, 100, 20))
        self.remaining_label.setAlignment(QtCore.Qt.AlignLeft)
        self.remaining_label.adjustSize()
        self.remaining_label_horizontalLayout.addWidget(self.remaining_label)
        self.gridLayout_3.addLayout(self.remaining_label_horizontalLayout, 1, 0, 1, 1)

        self.jh_line = QtWidgets.QFrame(self.centralwidget)
        self.jh_line.setGeometry(QtCore.QRect(382, 60, 507, 20))
        self.jh_line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.jh_line.setLineWidth(2)
        if dark == True:
            self.jh_line.setStyleSheet('color: #FFFFFF')
        else:
            self.jh_line.setStyleSheet('color: #838383')
        self.jh_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.jh_line.setObjectName("jh_line")
        self.Group_job_details.raise_()
        self.Group_memSize.raise_()
        self.Group_osSize.raise_()
        self.start_btn.raise_()
        self.back_btn.raise_()
        self.ph_line.raise_()
        self.Group_MemPartition.raise_()
        self.pv_line.raise_()
        self.jv_line.raise_()
        self.jh_line.raise_()
        mainscreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainscreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 917, 21))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        mainscreen.setMenuBar(self.menubar)

        self.retranslateUi(mainscreen)
        QtCore.QMetaObject.connectSlotsByName(mainscreen)

        self.make_default_entry(default_entry)
        self.make_default_partition_count(default_partition_count)
        self.button_state()
        self.entry_detail_state()
        self.memSize_value.textChanged.connect(self.entry_detail_state)
        self.osSize_value.textChanged.connect(self.entry_detail_state)
        self.memSize_value.selectAll()


    def back_to_start_up(self):
        self.new_window = MyWindow()
        self.activate_window = mainUI(self.new_window)
        self.new_window.show()
        self.mainscreen.hide()

    def make_default_entry(self, default_entry):
        for _ in range(default_entry):
            self.add_entry()

    def make_default_partition_count(self, default_partition_count):
        for _ in range(default_partition_count):
            self.add_partition()

    def add_partition(self):
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        # Parition No.
        self.partition_nums[f'partition{len(self.partition_nums) + 1}'] = QtWidgets.QLabel(
            self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.partition_nums[f'partition{len(self.partition_nums)}'].sizePolicy().hasHeightForWidth())
        self.partition_nums[f'partition{len(self.partition_nums)}'].setSizePolicy(sizePolicy)
        self.partition_nums[f'partition{len(self.partition_nums)}'].setText(f'{len(self.partition_nums)}')
        self.partition_nums[f'partition{len(self.partition_nums)}'].setFont(font)
        self.partition_nums[f'partition{len(self.partition_nums)}'].setScaledContents(False)
        self.partition_nums[f'partition{len(self.partition_nums)}'].setAlignment(QtCore.Qt.AlignCenter)
        self.partition_nums[f'partition{len(self.partition_nums)}'].setObjectName(
            f'partition{len(self.partition_nums)}')
        self.gridLayout_4.addWidget(self.partition_nums[f'partition{len(self.partition_nums)}'],
                                    len(self.partition_nums), 0, 1, 1)

        # Partition Size
        self.partition_sizes[f'partition_size{len(self.partition_sizes) + 1}'] = QtWidgets.QSpinBox(
            self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.partition_sizes[f'partition_size{len(self.partition_sizes)}'].sizePolicy().hasHeightForWidth())
        self.partition_sizes[f'partition_size{len(self.partition_sizes)}'].setSizePolicy(sizePolicy)
        self.partition_sizes[f'partition_size{len(self.partition_sizes)}'].setFont(font)
        self.partition_sizes[f'partition_size{len(self.partition_sizes)}'].setCursor(
            QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.partition_sizes[f'partition_size{len(self.partition_sizes)}'].setAlignment(QtCore.Qt.AlignCenter)
        self.partition_sizes[f'partition_size{len(self.partition_sizes)}'].setMaximum(999999999)
        self.partition_sizes[f'partition_size{len(self.partition_sizes)}'].setMinimum(0)
        self.partition_sizes[f'partition_size{len(self.partition_sizes)}'].setSingleStep(5)
        self.partition_sizes[f'partition_size{len(self.partition_sizes)}'].setProperty("value", 0)
        self.partition_sizes[f'partition_size{len(self.partition_sizes)}'].textChanged.connect(
            self.partition_entry_state)
        self.partition_sizes[f'partition_size{len(self.partition_sizes)}'].setObjectName("partition_size1")
        self.gridLayout_4.addWidget(self.partition_sizes[f'partition_size{len(self.partition_sizes)}'],
                                    len(self.partition_sizes), 1, 1, 1)
        list(self.partition_sizes.values())[-1].selectAll()
        list(self.partition_sizes.values())[-1].setFocus()
        Pscroll_bar = self.Partition_scrollArea.verticalScrollBar()
        self.Partition_scrollArea.verticalScrollBar().rangeChanged.connect(
            lambda: Pscroll_bar.setValue(Pscroll_bar.maximum()))
        self.button_state()

    def add_entry(self):
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        # Job No.
        self.job_entries[f"job{len(self.job_entries) + 1}"] = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.job_entries[f"job{len(self.job_entries)}"].setText(f"{len(self.job_entries)}")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.job_entries[f"job{len(self.job_entries)}"].sizePolicy().hasHeightForWidth())
        self.job_entries[f"job{len(self.job_entries)}"].setSizePolicy(sizePolicy)
        self.job_entries[f"job{len(self.job_entries)}"].setFont(font)
        self.job_entries[f"job{len(self.job_entries)}"].setScaledContents(False)
        self.job_entries[f"job{len(self.job_entries)}"].setAlignment(QtCore.Qt.AlignCenter)
        self.job_entries[f"job{len(self.job_entries)}"].setObjectName(f"job{len(self.job_entries)}")
        self.gridLayout.addWidget(self.job_entries[f"job{len(self.job_entries)}"], len(self.job_entries), 0, 1, 1)

        # Size
        self.size_entries[f'size{len(self.size_entries) + 1}'] = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.size_entries[f'size{len(self.size_entries)}'].sizePolicy().hasHeightForWidth())
        self.size_entries[f'size{len(self.size_entries)}'].setSizePolicy(sizePolicy)
        self.size_entries[f'size{len(self.size_entries)}'].setFont(font)
        self.size_entries[f'size{len(self.size_entries)}'].setMinimum(0)
        self.size_entries[f'size{len(self.size_entries)}'].setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.size_entries[f'size{len(self.size_entries)}'].setAlignment(QtCore.Qt.AlignCenter)
        self.size_entries[f'size{len(self.size_entries)}'].setMaximum(
            self.memSize_value.value() - self.osSize_value.value())
        self.size_entries[f'size{len(self.size_entries)}'].setSingleStep(5)
        self.size_entries[f'size{len(self.size_entries)}'].setProperty("value", 0)
        self.size_entries[f'size{len(self.size_entries)}'].setObjectName(f'size{len(self.size_entries)}')
        self.gridLayout.addWidget(self.size_entries[f'size{len(self.size_entries)}'], len(self.size_entries), 1, 1, 1)

        # Arrival
        self.arrival_entries[f'arrival{len(self.arrival_entries) + 1}'] = QtWidgets.QTimeEdit(
            self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.arrival_entries[f'arrival{len(self.arrival_entries)}'].sizePolicy().hasHeightForWidth())
        self.arrival_entries[f'arrival{len(self.arrival_entries)}'].setSizePolicy(sizePolicy)
        self.arrival_entries[f'arrival{len(self.arrival_entries)}'].setDisplayFormat("h:mm")
        self.arrival_entries[f'arrival{len(self.arrival_entries)}'].setFont(font)
        self.arrival_entries[f'arrival{len(self.arrival_entries)}'].setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.arrival_entries[f'arrival{len(self.arrival_entries)}'].setAlignment(QtCore.Qt.AlignCenter)
        self.arrival_entries[f'arrival{len(self.arrival_entries)}'].setObjectName(f'arrival{len(self.arrival_entries)}')
        self.gridLayout.addWidget(self.arrival_entries[f'arrival{len(self.arrival_entries)}'],
                                  len(self.arrival_entries), 2, 1, 1)

        # Run
        self.run_entries[f'run{len(self.run_entries) + 1}'] = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_entries[f'run{len(self.run_entries)}'].sizePolicy().hasHeightForWidth())
        self.run_entries[f'run{len(self.run_entries)}'].setSizePolicy(sizePolicy)
        self.run_entries[f'run{len(self.run_entries)}'].setFont(font)
        self.run_entries[f'run{len(self.run_entries)}'].setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.run_entries[f'run{len(self.run_entries)}'].setAlignment(QtCore.Qt.AlignCenter)
        self.run_entries[f'run{len(self.run_entries)}'].setMaximum(999999999)
        self.run_entries[f'run{len(self.run_entries)}'].setSingleStep(5)
        self.run_entries[f'run{len(self.run_entries)}'].setProperty("value", 0)
        self.run_entries[f'run{len(self.run_entries)}'].setObjectName(f'run{len(self.run_entries)}')
        self.gridLayout.addWidget(self.run_entries[f'run{len(self.run_entries)}'], len(self.run_entries), 3, 1, 1)

        scroll_bar = self.scrollArea.verticalScrollBar()
        self.scrollArea.verticalScrollBar().rangeChanged.connect(lambda: scroll_bar.setValue(scroll_bar.maximum()))
        self.button_state()

    def remove_entry(self):
        self.job_entries[f"job{len(self.job_entries)}"].hide()
        self.size_entries[f'size{len(self.size_entries)}'].hide()
        self.arrival_entries[f'arrival{len(self.arrival_entries)}'].hide()
        self.run_entries[f'run{len(self.run_entries)}'].hide()

        del self.job_entries[f"job{len(self.job_entries)}"]
        del self.size_entries[f'size{len(self.size_entries)}']
        del self.arrival_entries[f'arrival{len(self.arrival_entries)}']
        del self.run_entries[f'run{len(self.run_entries)}']

        scroll_bar = self.scrollArea.verticalScrollBar()
        self.scrollArea.verticalScrollBar().rangeChanged.connect(lambda: scroll_bar.setValue(scroll_bar.maximum()))
        self.button_state()

    def remove_partition(self):
        self.partition_nums[f"partition{len(self.partition_nums)}"].hide()
        self.partition_sizes[f'partition_size{len(self.partition_sizes)}'].hide()

        del self.partition_nums[f"partition{len(self.partition_nums)}"]
        del self.partition_sizes[f'partition_size{len(self.partition_sizes)}']

        Pscroll_bar = self.Partition_scrollArea.verticalScrollBar()
        self.Partition_scrollArea.verticalScrollBar().rangeChanged.connect(
            lambda: Pscroll_bar.setValue(Pscroll_bar.maximum()))
        self.button_state()

    def scroll(self):
        item = self.ListWidget.findItems('ITEM-0011', QtCore.Qt.MatchRegExp)[0]
        item.setSelected(True)
        self.ListWidget.scrollToItem(item, QtGui.QAbstractItemView.PositionAtTop)

    def button_state(self):
        if len(self.partition_nums) == 1:
            self.rmv_partition_btn.setEnabled(False)
        else:
            self.rmv_partition_btn.setEnabled(True)

        if self.csv_loaded_successful:
            self.add_entry_btn.setEnabled(False)
            self.rmv_entry_btn.setEnabled(False)
        else:
            if len(self.job_entries) == 1:
                self.rmv_entry_btn.setEnabled(False)
            else:
                self.rmv_entry_btn.setEnabled(True)
            self.add_entry_btn.setEnabled(True)

    def make_import_btn(self):
        self.import_csv_btn = QtWidgets.QPushButton(self.Group_job_details)
        self.import_csv_btn.setGeometry(QtCore.QRect(270, 535, 100, 20))
        self.import_csv_btn.setText("  Import CSV")
        self.import_csv_btn.setToolTip(
            'Must have this order in your file:\n{job number, job size*, arrival time*, run time*}')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_csv_btn.sizePolicy().hasHeightForWidth())
        self.import_csv_btn.setSizePolicy(sizePolicy)
        self.import_csv_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.import_csv_btn.setSizeIncrement(QtCore.QSize(0, 0))
        self.horizontalLayout_4.addWidget(self.import_csv_btn)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(65)
        font.setKerning(True)
        self.import_csv_btn.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(resource_path("Icons/table_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.import_csv_btn.setIcon(icon2)
        self.import_csv_btn.setIconSize(QtCore.QSize(15, 15))
        self.import_csv_btn.setCheckable(False)
        self.import_csv_btn.setDefault(False)
        self.import_csv_btn.setFlat(True)
        self.import_csv_btn.setObjectName("import_csv_btn")
        self.import_csv_btn.clicked.connect(self.import_csv)
        self.import_csv_btn.show()

    def make_cancel_csv_btn(self):
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(65)
        font.setKerning(True)

        self.cancel_csv_btn = QtWidgets.QPushButton(self.Group_job_details)
        self.cancel_csv_btn.setGeometry(QtCore.QRect(270, 528, 32, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_csv_btn.sizePolicy().hasHeightForWidth())
        self.cancel_csv_btn.setSizePolicy(sizePolicy)
        self.cancel_csv_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.cancel_csv_btn.setSizeIncrement(QtCore.QSize(0, 0))
        self.horizontalLayout_4.addWidget(self.cancel_csv_btn)

        self.cancel_csv_btn.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(resource_path("Icons/Close_Icon_red.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_csv_btn.setIcon(icon2)
        self.cancel_csv_btn.setIconSize(QtCore.QSize(15, 15))
        self.cancel_csv_btn.setCheckable(False)
        self.cancel_csv_btn.setDefault(False)
        self.cancel_csv_btn.setFlat(True)
        self.cancel_csv_btn.setObjectName("cancel_csv_btn")
        self.cancel_csv_btn.clicked.connect(self.cancel_csv)

        self.file_name_label = QtWidgets.QLabel(self.Group_job_details)
        self.file_name_label.setFont(font)
        self.file_name_label.setObjectName('file_name_label')
        self.file_name_label.setGeometry(QtCore.QRect(302, 535, 100, 20))
        self.file_name_label.setText(self.active_file)
        self.file_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.file_name_label.adjustSize()
        self.horizontalLayout_4.addWidget(self.file_name_label)

    def cancel_csv(self):
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)

        notify_user = QtWidgets.QMessageBox()
        # notify_user.question()
        notify_user.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        notify_user.setDefaultButton(QtWidgets.QMessageBox.No)
        notify_user.setIcon(QtWidgets.QMessageBox.Question)
        notify_user.setFont(font)
        notify_user.setText('Are you sure you want to remove this file?      ')
        notify_user.setWindowTitle("Notify")

        if notify_user.exec_() == QtWidgets.QMessageBox.Yes:
            print('Yes  ')
            self.cancel_csv_btn.hide()
            self.file_name_label.hide()
            del self.cancel_csv_btn
            del self.file_name_label

            for _ in range(len(self.job_entries)):
                self.remove_entry()
            for _ in range(len(self.partition_sizes)):
                self.remove_partition()
            self.make_default_partition_count(default_partition_count)
            self.make_default_entry(default_entry)
            self.entry_detail_state()

            self.make_import_btn()
            self.max_size = 0
            self.memSize_value.textChanged.connect(self.entry_detail_state)
            self.osSize_value.textChanged.connect(self.entry_detail_state)
            for i in range(len(self.partition_sizes)):
                list(self.partition_sizes.values())[i].textChanged.connect(self.partition_entry_state)
            self.add_entry_btn.setEnabled(True)
            self.rmv_entry_btn.setEnabled(True)

            # QtWidgets.QSpinBox().clear
            self.csv_loaded_successful = False

    def getFileDir(self):
        file_filter = '*.csv'
        response = QtWidgets.QFileDialog.getOpenFileNames(
            parent=QtWidgets.QWidget(),
            caption='Select a csv file',
            directory=os.getcwd(),
            filter=file_filter
        )
        self.active_file = response[0][0].split('/')[-1]
        return response[0][0]

    def import_csv(self):
        try:
            fileDir = self.getFileDir()
            csv = pd.read_csv(fileDir)
            column_name = list(csv.columns)
            jobs = csv[column_name[0]].tolist()
            job_size = csv[column_name[1]].tolist()
            arrival_time = csv[column_name[2]].tolist()
            run_time = csv[column_name[3]].tolist()

            for _ in range(len(self.job_entries)):
                self.remove_entry()
            self.import_csv_btn.hide()
            del self.import_csv_btn
            self.make_cancel_csv_btn()
            self.load_csv_to_window(jobs, job_size, arrival_time, run_time)

        except IndexError:
            print('No file selected')

    def load_csv_to_window(self, j, s, a, r):
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        # Job No.
        for i in range(len(a)):
            self.job_entries[f"job{i + 1}"] = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            self.job_entries[f"job{i + 1}"].setText(f"{i + 1}")
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.job_entries[f"job{i + 1}"].sizePolicy().hasHeightForWidth())
            self.job_entries[f"job{i + 1}"].setSizePolicy(sizePolicy)
            self.job_entries[f"job{i + 1}"].setFont(font)
            self.job_entries[f"job{i + 1}"].setScaledContents(False)
            self.job_entries[f"job{i + 1}"].setAlignment(QtCore.Qt.AlignCenter)
            self.job_entries[f"job{i + 1}"].setObjectName(f"job{i + 1}")
            self.gridLayout.addWidget(self.job_entries[f"job{i + 1}"], i + 1, 0, 1, 1)
        # Size
        for i in range(len(a)):
            self.size_entries[f'size{i + 1}'] = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            self.size_entries[f'size{i + 1}'].setText(f"{s[i]}")
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.size_entries[f'size{i + 1}'].sizePolicy().hasHeightForWidth())
            self.size_entries[f'size{i + 1}'].setSizePolicy(sizePolicy)
            self.size_entries[f'size{i + 1}'].setFont(font)
            self.size_entries[f'size{i + 1}'].setScaledContents(False)
            self.size_entries[f'size{i + 1}'].setAlignment(QtCore.Qt.AlignCenter)
            self.size_entries[f'size{i + 1}'].setObjectName(f"size{i + 1}")
            self.gridLayout.addWidget(self.size_entries[f'size{i + 1}'], i + 1, 1, 1, 1)
        # Arrival
        for i in range(len(a)):
            self.arrival_entries[f'arrival{i + 1}'] = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            self.arrival_entries[f'arrival{i + 1}'].setText(f"{a[i]}")
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.arrival_entries[f'arrival{i + 1}'].sizePolicy().hasHeightForWidth())
            self.arrival_entries[f'arrival{i + 1}'].setSizePolicy(sizePolicy)
            self.arrival_entries[f'arrival{i + 1}'].setFont(font)
            self.arrival_entries[f'arrival{i + 1}'].setScaledContents(False)
            self.arrival_entries[f'arrival{i + 1}'].setAlignment(QtCore.Qt.AlignCenter)
            self.arrival_entries[f'arrival{i + 1}'].setObjectName(f"arrival{i + 1}")
            self.gridLayout.addWidget(self.arrival_entries[f'arrival{i + 1}'], i + 1, 2, 1, 1)
        # Run
        for i in range(len(a)):
            self.run_entries[f'run{i + 1}'] = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            self.run_entries[f'run{i + 1}'].setText(f"{r[i]}")
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.run_entries[f'run{i + 1}'].sizePolicy().hasHeightForWidth())
            self.run_entries[f'run{i + 1}'].setSizePolicy(sizePolicy)
            self.run_entries[f'run{i + 1}'].setFont(font)
            self.run_entries[f'run{i + 1}'].setScaledContents(False)
            self.run_entries[f'run{i + 1}'].setAlignment(QtCore.Qt.AlignCenter)
            self.run_entries[f'run{i + 1}'].setObjectName(f"run{i + 1}")
            self.gridLayout.addWidget(self.run_entries[f'run{i + 1}'], i + 1, 3, 1, 1)

        self.max_size = max(s)
        for i in range(len(self.partition_sizes)):
            list(self.partition_sizes.values())[i].textChanged.connect(self.partition_entry_state_QLabel)
        self.memSize_value.textChanged.connect(self.entry_detail_state_QLabel)
        self.osSize_value.textChanged.connect(self.entry_detail_state_QLabel)

        self.csv_loaded_successful = True
        self.Group_job_details.setEnabled(True)
        self.add_entry_btn.setEnabled(False)
        self.rmv_entry_btn.setEnabled(False)

        self.entry_detail_state_QLabel()
        scroll_bar = self.scrollArea.verticalScrollBar()
        self.scrollArea.verticalScrollBar().rangeChanged.connect(lambda: scroll_bar.setValue(scroll_bar.minimum()))
        # self.partition_entry_state_QLabel()

    def entry_detail_state(self):
        global dark
        if dark == True:
            self.jh_line.setStyleSheet('color: #FFFFFF')
        else:
            self.jh_line.setStyleSheet('color: #838383')
        if dark == False:
            if self.memSize_value.value() != 0:
                self.Group_job_details.setEnabled(True)
                self.jv_line.setStyleSheet('color: black')
                self.jv_line2.setStyleSheet('color: black')
                self.jh_line.setStyleSheet('color: black')
                self.Group_MemPartition.setEnabled(True)
                self.pv_line.setStyleSheet('color: black')
                self.pv_line2.setStyleSheet('color: black')
                self.ph_line.setStyleSheet('color: black')
            else:
                self.Group_job_details.setEnabled(False)
                self.jv_line.setStyleSheet('color: #838383')
                self.jv_line2.setStyleSheet('color: #838383')
                self.jh_line.setStyleSheet('color: #838383')
                self.Group_MemPartition.setEnabled(False)
                self.pv_line.setStyleSheet('color: #838383')
                self.pv_line2.setStyleSheet('color: #838383')
                self.ph_line.setStyleSheet('color: #838383')
        else:
            if self.memSize_value.value() != 0:
                self.Group_job_details.setEnabled(True)
                self.jv_line.setStyleSheet('color: #FFFFFF')
                self.jv_line2.setStyleSheet('color: #FFFFFF')
                self.jh_line.setStyleSheet('color: #FFFFFF')
                self.Group_MemPartition.setEnabled(True)
                self.pv_line.setStyleSheet('color: #FFFFFF')
                self.pv_line2.setStyleSheet('color: #FFFFFF')
                self.ph_line.setStyleSheet('color: #FFFFFF')
            else:
                self.Group_job_details.setEnabled(False)
                self.jv_line.setStyleSheet('color: #FFFFFF')
                self.jv_line2.setStyleSheet('color: #FFFFFF')
                self.jh_line.setStyleSheet('color: #FFFFFF')
                self.Group_MemPartition.setEnabled(False)
                self.pv_line.setStyleSheet('color: #FFFFFF')
                self.pv_line2.setStyleSheet('color: #FFFFFF')
                self.ph_line.setStyleSheet('color: #FFFFFF')

        if type(self.size_entries['size1']).__name__ != 'QLabel':
            self.osSize_value.setMaximum(self.memSize_value.value())
            self.partition_entry_state()
            for i in range(len(self.size_entries)):
                if type(self.size_entries['size1']).__name__ != 'QLabel':
                    if self.remaining_size > self.max_partition:
                        list(self.size_entries.values())[i].setMaximum(self.remaining_size)
                    else:
                        list(self.size_entries.values())[i].setMaximum(self.max_partition)
                    if list(self.size_entries.values())[i].value() < 0:
                        list(self.size_entries.values())[i].setMinimum(0)

    def partition_entry_state(self):
        if type(self.size_entries['size1']).__name__ != 'QLabel':
            partition = []
            self.osSize_value.setMaximum(self.memSize_value.value())
            self.remaining_size = self.memSize_value.value() - self.osSize_value.value()
            for i in range(len(self.partition_sizes)):
                list(self.partition_sizes.values())[i].setMaximum(self.remaining_size)
                list(self.partition_sizes.values())[i].setMinimum(0)
                self.remaining_size -= list(self.partition_sizes.values())[i].value()
                partition.append(list(self.partition_sizes.values())[i].value())
            self.max_partition = max(
                partition)  ################# Job Size Validation (based on max partition) #####################
            if self.remaining_size < 0:
                self.remaining_label.setText(f'Remaining: 0')
            else:
                self.remaining_label.setText(f'Remaining: {self.remaining_size}')

            for i in range(len(self.size_entries)):
                if self.remaining_size > self.max_partition:
                    list(self.size_entries.values())[i].setMaximum(self.remaining_size)
                else:
                    list(self.size_entries.values())[i].setMaximum(self.max_partition)
                if list(self.size_entries.values())[i].value() < 0:
                    list(self.size_entries.values())[i].setMinimum(0)

    def entry_detail_state_QLabel(self):
        if type(self.size_entries['size1']).__name__ == 'QLabel':
            self.memSize_value.setMinimum(self.max_size)
            self.osSize_value.setMaximum(self.memSize_value.value())

            self.remaining_size = self.memSize_value.value() - self.osSize_value.value()

            self.partition_entry_state_QLabel()
            if self.remaining_size < 0:
                self.remaining_label.setText(f'Remaining: 0')
            else:
                self.remaining_label.setText(f'Remaining: {self.remaining_size}')

    def partition_entry_state_QLabel(self):
        if type(self.size_entries['size1']).__name__ == 'QLabel':
            partition = []
            self.remaining_size = self.memSize_value.value() - self.osSize_value.value()
            for i in range(len(self.partition_sizes)):
                if self.remaining_size >= 0:
                    # list(self.partition_sizes.values())[i].setMinimum(self.max_size)
                    list(self.partition_sizes.values())[i].setMaximum(self.remaining_size)

                    self.remaining_size -= list(self.partition_sizes.values())[i].value()
                partition.append(list(self.partition_sizes.values())[i].value())
            self.max_partition = max(partition)
            if self.remaining_size < 0:
                self.remaining_label.setText(f'Remaining: 0')
            else:
                self.remaining_label.setText(f'Remaining: {self.remaining_size}')

    def start(self):
        print(type(self.size_entries['size1']).__name__, '<----------------------')
        # Validate Inputs
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)

        notify_user = QtWidgets.QMessageBox()
        notify_user.setIcon(QtWidgets.QMessageBox.Information)
        notify_user.setFont(font)

        err_msg = QtWidgets.QMessageBox()
        err_msg.setIcon(QtWidgets.QMessageBox.Information)
        err_msg.setFont(font)

        self.validated = True
        for _ in range(1):
            if self.memSize_value.value() <= self.osSize_value.value():
                self.validated = False
                err_msg.setText('Sizes must be:\nMemory size > OS size > 0      ')
                err_msg.setWindowTitle("Memory Error")
                err_msg.exec_()
                self.memSize_value.setFocus()
                self.memSize_value.selectAll()
                self.Group_job_details.setEnabled(False)
                break

            elif self.osSize_value.value() <= 0:
                self.validated = False
                err_msg.setText('Sizes must be:\nMemory size > OS size > 0      ')
                err_msg.setWindowTitle("Memory Error")
                err_msg.exec_()
                self.osSize_value.setFocus()
                self.osSize_value.selectAll()
                self.Group_job_details.setEnabled(False)
                break

            elif self.max_size > (self.memSize_value.value() - self.osSize_value.value()):
                self.validated = False
                err_msg.setText(f'Job sizes must fit !\n ~max={self.max_size}                  ')
                err_msg.setWindowTitle("Size Error")
                err_msg.exec_()
                break

            for i in range(len(self.job_entries)):
                if type(self.size_entries['size1']).__name__ == 'QLabel':
                    if list(self.size_entries.values())[i].text() == 0:
                        self.validated = False
                        err_msg.setText('Time and sizes must be greater than 0      ')
                        err_msg.setWindowTitle("Job Error")
                        err_msg.exec_()
                        list(self.size_entries.values())[i].setFocus()
                        list(self.size_entries.values())[i].selectAll()
                        break
                    if list(self.arrival_entries.values())[i].text().split(':')[0] == '0':
                        self.validated = False
                        err_msg.setText('Time and sizes must be greater than 0      ')
                        err_msg.setWindowTitle("Job Error")
                        err_msg.exec_()
                        list(self.arrival_entries.values())[i].setFocus()
                        list(self.arrival_entries.values())[i].selectAll()
                        break
                    if list(self.run_entries.values())[i].text() == 0:
                        self.validated = False
                        err_msg.setText('Time and sizes must be greater than 0      ')
                        err_msg.setWindowTitle("Job Error")
                        err_msg.exec_()
                        list(self.run_entries.values())[i].setFocus()
                        list(self.run_entries.values())[i].selectAll()
                        break
                else:
                    if list(self.size_entries.values())[i].value() == 0:
                        self.validated = False
                        err_msg.setText('Time and sizes must be greater than 0      ')
                        err_msg.setWindowTitle("Job Error")
                        err_msg.exec_()
                        list(self.size_entries.values())[i].setFocus()
                        list(self.size_entries.values())[i].selectAll()
                        yloc = list(self.size_entries.values())[i].y() - list(self.size_entries.values())[i].height()
                        self.scrollArea.verticalScrollBar().setValue(yloc)
                        break
                    if list(self.arrival_entries.values())[i].text().split(':')[0] == '0':
                        self.validated = False
                        err_msg.setText('Time and sizes must be greater than 0      ')
                        err_msg.setWindowTitle("Job Error")
                        err_msg.exec_()
                        list(self.arrival_entries.values())[i].setFocus()
                        list(self.arrival_entries.values())[i].selectAll()
                        yloc = list(self.arrival_entries.values())[i].y() - list(self.arrival_entries.values())[
                            i].height()
                        self.scrollArea.verticalScrollBar().setValue(yloc)
                        break
                    if list(self.run_entries.values())[i].value() == 0:
                        self.validated = False
                        err_msg.setText('Time and sizes must be greater than 0      ')
                        err_msg.setWindowTitle("Job Error")
                        err_msg.exec_()
                        list(self.run_entries.values())[i].setFocus()
                        list(self.run_entries.values())[i].selectAll()
                        yloc = list(self.run_entries.values())[i].y() - list(self.run_entries.values())[i].height()
                        self.scrollArea.verticalScrollBar().setValue(yloc)
                        break

        if self.validated == False and self.csv_loaded_successful == True:
            self.Group_job_details.setEnabled(True)

        # Export JSON
        if self.validated:
            if type(self.size_entries['size1']).__name__ == 'QLabel':
                dictionary = {
                    'Memory size': self.memSize_value.value(),
                    'OS size': self.osSize_value.value(),
                    'Partition size': [partition_size.value() for partition_size in self.partition_sizes.values()],
                    'Job': [job.text() for job in self.job_entries.values()],
                    'Size': [int(size.text()) for size in self.size_entries.values()],
                    'Arrival time': [arrival.text() for arrival in self.arrival_entries.values()],
                    'Run time': [int(run.text()) for run in self.run_entries.values()]
                }
            else:
                dictionary = {
                    'Memory size': self.memSize_value.value(),
                    'OS size': self.osSize_value.value(),
                    'Partition size': [partition_size.value() for partition_size in self.partition_sizes.values()],
                    'Job': [job.text() for job in self.job_entries.values()],
                    'Size': [int(size.value()) for size in self.size_entries.values()],
                    'Arrival time': [arrival.text() for arrival in self.arrival_entries.values()],
                    'Run time': [int(run.value()) for run in self.run_entries.values()]
                }

            if dictionary["Arrival time"] != sorted(dictionary["Arrival time"]):
                notify_user.setText('Unsorted arrival detected\n~Inputs are now sorted by arrival !      ')
                notify_user.setWindowTitle("Sort by Arrival")
                notify_user.button
                notify_user.setStandardButtons
                notify_user.exec_()

            # Sort by Arrival
            for i in range(len(dictionary['Arrival time']) - 1):
                for j in range(0, len(dictionary['Arrival time']) - i - 1):
                    if fcn.to_minutes(dictionary['Arrival time'][j]) > fcn.to_minutes(
                            dictionary['Arrival time'][j + 1]):
                        dictionary['Arrival time'][j], dictionary['Arrival time'][j + 1] = dictionary['Arrival time'][
                                                                                               j + 1], \
                                                                                           dictionary['Arrival time'][j]
                        dictionary['Size'][j], dictionary['Size'][j + 1] = dictionary['Size'][j + 1], \
                                                                           dictionary['Size'][j]
                        dictionary['Run time'][j], dictionary['Run time'][j + 1] = dictionary['Run time'][j + 1], \
                                                                                   dictionary['Run time'][j]

            with open(f"{usrfile_name}.json", "w") as outfile:
                json.dump(dictionary, outfile, indent=4)

            global D
            global X

            D = dictionary
            X = sp.static_partition_EXEC(usrfile_name)
            self.next_window(D, X)
            print('VALIDATAED')

        else:
            print('NOT VALIDATED')

    def next_window(self, inputs, Data):
        self.newWindow = MyWindow()
        self.second_ui = SP_ProcessWindow(self.newWindow, inputs, Data)
        self.newWindow.show()
        self.mainscreen.hide()


class SP_ProcessWindow:
    V_END = 470

    def __init__(self, mainscreen, inputs, D):
        self.mem_map, self.label, self.message, self.status_table, self.partition_size, = D[0], D[1], D[2], D[3], D[4]
        self.start_time, self.finish, self.cpu_wait = D[5], D[6], D[7]
        self.inputs = inputs
        self.mainscreen = mainscreen
        self.idx = 0
        self.fixed = False
        self.d = {}
        self.labels = {}
        self.mem_labels = {}
        self.end_show = False
        self.error_msg_value = 0
        global dark
        self.dark_theme_enabled = dark
        mainscreen.setObjectName("mainscreen")
        mainscreen.setWindowIcon(QtGui.QIcon(resource_path('Images\MainWindow.png')))
        mainscreen.setFixedSize(917, 655)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        mainscreen.setFont(font)
        mainscreen.setAutoFillBackground(False)
        mainscreen.setAnimated(True)
        mainscreen.setDocumentMode(False)
        mainscreen.setTabShape(QtWidgets.QTabWidget.Rounded)
        mainscreen.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(mainscreen)
        self.centralwidget.setObjectName("centralwidget")
        self.Group_memoryMap = QtWidgets.QGroupBox(self.centralwidget)
        self.Group_memoryMap.setGeometry(QtCore.QRect(510, 10, 321, 540))

        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Group_memoryMap.setFont(font)
        self.Group_memoryMap.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Group_memoryMap.setObjectName("Group_memoryMap")
        self.Group_job_table = QtWidgets.QGroupBox(self.centralwidget)
        self.Group_job_table.setGeometry(QtCore.QRect(20, 119, 451, 215))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.Group_job_table.setFont(font)
        self.Group_job_table.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.Group_job_table.setCheckable(False)
        self.Group_job_table.setChecked(False)
        self.Group_job_table.setObjectName("Group_job_table")
        self.Job_Table = QtWidgets.QTableWidget(self.Group_job_table)
        self.Job_Table.setGeometry(QtCore.QRect(10, 27, 432, 181))
        self.Job_Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Job_Table.horizontalHeader().setSortIndicatorShown(False)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Job_Table.setFont(font)
        self.Job_Table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.Job_Table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Job_Table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.Job_Table.verticalHeader().setVisible(False)  # Row Index
        self.Job_Table.setFocusPolicy(QtCore.Qt.FocusPolicy(False))  # Cell Highlighting
        self.Job_Table.horizontalHeader().setStyleSheet(
            'QHeaderView::section { border: none; border-bottom: 2px solid green;}')

        self.Job_Table.setAutoScroll(True)
        self.Job_Table.setAlternatingRowColors(True)
        self.Job_Table.setObjectName("Job_Table")
        self.Job_Table.setColumnCount(4)
        self.Job_Table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Job_Table.setHorizontalHeaderItem(0, item)
        self.Job_Table.setItemDelegateForColumn(0, AlignDelegate(self.Job_Table))
        item = QtWidgets.QTableWidgetItem()
        self.Job_Table.setHorizontalHeaderItem(1, item)
        self.Job_Table.setItemDelegateForColumn(1, AlignDelegate(self.Job_Table))
        item = QtWidgets.QTableWidgetItem()
        self.Job_Table.setHorizontalHeaderItem(2, item)
        self.Job_Table.setItemDelegateForColumn(2, AlignDelegate(self.Job_Table))
        item = QtWidgets.QTableWidgetItem()
        self.Job_Table.setHorizontalHeaderItem(3, item)
        self.Job_Table.setItemDelegateForColumn(3, AlignDelegate(self.Job_Table))
        self.Job_Table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)

        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(90)
        self.Job_Table.horizontalHeaderItem(0).setFont(font)
        self.Job_Table.horizontalHeaderItem(1).setFont(font)
        self.Job_Table.horizontalHeaderItem(2).setFont(font)
        self.Job_Table.horizontalHeaderItem(3).setFont(font)

        self.Job_Table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.Job_Table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.Job_Table.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.Job_Table.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        # self.Job_Table.verticalHeader().setDefaultSectionSize(44)

        self.Group_pat_table = QtWidgets.QGroupBox(self.centralwidget)
        self.Group_pat_table.setGeometry(QtCore.QRect(20, 350, 451, 215))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.Group_pat_table.setFont(font)
        self.Group_pat_table.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.Group_pat_table.setCheckable(False)
        self.Group_pat_table.setChecked(False)
        self.Group_pat_table.setObjectName("Group_pat_table")

        self.PAT_Table = QtWidgets.QTableWidget(self.Group_pat_table)
        self.PAT_Table.setGeometry(QtCore.QRect(10, 27, 432, 181))
        self.PAT_Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.PAT_Table.horizontalHeader().setSortIndicatorShown(False)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PAT_Table.setFont(font)
        self.PAT_Table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.PAT_Table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PAT_Table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.PAT_Table.verticalHeader().setVisible(False)  # Row Index
        self.PAT_Table.setFocusPolicy(QtCore.Qt.FocusPolicy(False))  # Cell Highlighting
        self.PAT_Table.horizontalHeader().setStyleSheet(
            'QHeaderView::section { border: none; border-bottom: 2px solid #2A74BB;}')

        self.PAT_Table.setAutoScroll(True)
        self.PAT_Table.setAlternatingRowColors(True)
        self.PAT_Table.setObjectName("PAT_Table")
        self.PAT_Table.setColumnCount(4)
        self.PAT_Table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.PAT_Table.setHorizontalHeaderItem(0, item)
        self.PAT_Table.setItemDelegateForColumn(0, AlignDelegate(self.PAT_Table))
        item = QtWidgets.QTableWidgetItem()
        self.PAT_Table.setHorizontalHeaderItem(1, item)
        self.PAT_Table.setItemDelegateForColumn(1, AlignDelegate(self.PAT_Table))
        item = QtWidgets.QTableWidgetItem()
        self.PAT_Table.setHorizontalHeaderItem(2, item)
        self.PAT_Table.setItemDelegateForColumn(2, AlignDelegate(self.PAT_Table))
        item = QtWidgets.QTableWidgetItem()
        self.PAT_Table.setHorizontalHeaderItem(3, item)
        self.PAT_Table.setItemDelegateForColumn(3, AlignDelegate(self.PAT_Table))
        self.PAT_Table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)

        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(90)
        self.PAT_Table.horizontalHeaderItem(0).setFont(font)
        self.PAT_Table.horizontalHeaderItem(1).setFont(font)
        self.PAT_Table.horizontalHeaderItem(2).setFont(font)
        self.PAT_Table.horizontalHeaderItem(3).setFont(font)

        self.PAT_Table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.PAT_Table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.PAT_Table.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.PAT_Table.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        # self.Job_Table.verticalHeader().setDefaultSectionSize(44)

        self.Group_osSize = QtWidgets.QGroupBox(self.centralwidget)
        self.Group_osSize.setGeometry(QtCore.QRect(350, 70, 120, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.Group_osSize.setFont(font)
        self.Group_osSize.setObjectName("Group_osSize")
        self.OS_size_label = QtWidgets.QLabel(self.Group_osSize)
        self.OS_size_label.setEnabled(True)
        self.OS_size_label.setGeometry(QtCore.QRect(10, 18, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.OS_size_label.setFont(font)
        self.OS_size_label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.OS_size_label.setMouseTracking(False)
        self.OS_size_label.setTabletTracking(False)
        self.OS_size_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.OS_size_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.OS_size_label.setAlignment(QtCore.Qt.AlignCenter)
        self.OS_size_label.setObjectName("OS_size_label")
        self.Group_memSize = QtWidgets.QGroupBox(self.centralwidget)
        self.Group_memSize.setGeometry(QtCore.QRect(30, 70, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.Group_memSize.setFont(font)
        self.Group_memSize.setFlat(False)
        self.Group_memSize.setCheckable(False)
        self.Group_memSize.setObjectName("Group_memSize")
        self.mem_size_label = QtWidgets.QLabel(self.Group_memSize)
        self.mem_size_label.setGeometry(QtCore.QRect(20, 18, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mem_size_label.setFont(font)
        self.mem_size_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mem_size_label.setObjectName("mem_size_label")
        self.partition_title = QtWidgets.QLabel(self.centralwidget)
        self.partition_title.setGeometry(QtCore.QRect(20, 5, 451, 61))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.partition_title.setFont(font)
        self.partition_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.partition_title.setFrameShadow(QtWidgets.QFrame.Plain)
        self.partition_title.setLineWidth(1)
        self.partition_title.setAlignment(QtCore.Qt.AlignCenter)
        self.partition_title.setObjectName("partition_title")
        self.prev_button = QtWidgets.QPushButton(self.centralwidget)
        self.prev_button.setGeometry(QtCore.QRect(550, 565, 111, 23))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.prev_button.setFont(font)
        self.prev_button.setObjectName("prev_button")
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(700, 565, 111, 23))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setBold(False)
        font.setWeight(50)
        self.next_button.setFont(font)
        self.next_button.setObjectName("next_button")
        self.simplify_cbx = QtWidgets.QCheckBox(self.centralwidget)
        self.simplify_cbx.setGeometry(QtCore.QRect(775, 605, 65, 19))
        self.simplify_cbx.setFont(font)
        self.simplify_cbx.setObjectName("simplify_cbx")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(18, 560, 451, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.message_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.message_label.setFont(font)
        self.message_label.setAlignment(QtCore.Qt.AlignCenter)
        self.message_label.setObjectName("message_label")
        self.horizontalLayout.addWidget(self.message_label)
        mainscreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainscreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 917, 28))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setBold(False)
        font.setWeight(50)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setBold(False)
        font.setWeight(50)
        self.menuHelp.setFont(font)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAbout = QtWidgets.QMenu(self.menuHelp)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setBold(False)
        font.setWeight(50)
        self.menuAbout.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("Icons/message.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuAbout.setIcon(icon)
        self.menuAbout.setObjectName("menuAbout")
        self.menuDevelopers = QtWidgets.QMenu(self.menuAbout)
        icon0 = QtGui.QIcon()
        icon0.addPixmap(QtGui.QPixmap(resource_path("Icons/group.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuDevelopers.setIcon(icon0)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setBold(False)
        font.setWeight(50)
        self.menuDevelopers.setFont(font)
        self.menuDevelopers.setObjectName("menuDevelopers")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")
        self.menuAppearance = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setBold(False)
        font.setWeight(50)
        self.menuAppearance.setFont(font)
        self.menuAppearance.setObjectName("menuAppearance")
        self.menuAppearance_2 = QtWidgets.QMenu(self.menuAppearance)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setBold(False)
        font.setWeight(50)
        self.menuAppearance_2.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("Icons/favorite.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuAppearance_2.setIcon(icon)
        self.menuAppearance_2.setObjectName("menuAppearance_2")
        mainscreen.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(mainscreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBar.setSizeIncrement(QtCore.QSize(0, 0))
        self.toolBar.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.toolBar.setFont(font)
        self.toolBar.setAcceptDrops(False)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setMovable(True)
        self.toolBar.setOrientation(QtCore.Qt.Vertical)
        self.toolBar.setIconSize(QtCore.QSize(30, 25))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        mainscreen.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionHome = QtWidgets.QAction(mainscreen)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("Icons/house_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHome.setIcon(icon)
        self.actionHome.setObjectName("actionHome")
        self.actionLyra = QtWidgets.QAction(mainscreen)
        self.actionLyra.setObjectName("actionLyra")
        self.actionRyan = QtWidgets.QAction(mainscreen)
        self.actionRyan.setObjectName("actionRyan")
        self.actionJoshua = QtWidgets.QAction(mainscreen)
        self.actionJoshua.setObjectName("actionJoshua")
        self.actionLyra_2 = QtWidgets.QAction(mainscreen)
        self.actionLyra_2.setObjectName("actionLyra_2")
        self.actionRyan_2 = QtWidgets.QAction(mainscreen)
        self.actionRyan_2.setObjectName("actionRyan_2")
        self.actionJoshua_2 = QtWidgets.QAction(mainscreen)
        self.actionJoshua_2.setObjectName("actionJoshua_2")
        self.actionKent = QtWidgets.QAction(mainscreen)
        self.actionKent.setObjectName("actionKent")
        self.actionGrant = QtWidgets.QAction(mainscreen)
        self.actionGrant.setObjectName("actionGrant")
        self.actionThis_partition = QtWidgets.QAction(mainscreen)
        self.actionThis_partition.setObjectName("actionThis_partition")
        self.actionHow_to_use = QtWidgets.QAction(mainscreen)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("Icons/idea.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHow_to_use.setIcon(icon)
        self.actionHow_to_use.setObjectName("actionHow_to_use")
        self.actionCSV = QtWidgets.QAction(mainscreen)
        self.actionCSV.setObjectName("actionCSV")
        self.actionPNG = QtWidgets.QAction(mainscreen)
        self.actionPNG.setObjectName("actionPNG")
        self.actionJPEG = QtWidgets.QAction(mainscreen)
        self.actionJPEG.setObjectName("actionJPEG")
        self.actionCSV_2 = QtWidgets.QAction(mainscreen)
        self.actionCSV_2.setObjectName("actionCSV_2")
        self.actionPNG_2 = QtWidgets.QAction(mainscreen)
        self.actionPNG_2.setObjectName("actionPNG_2")
        self.actionJPEG_2 = QtWidgets.QAction(mainscreen)
        self.actionJPEG_2.setObjectName("actionJPEG_2")
        self.actionJPEG_3 = QtWidgets.QAction(mainscreen)
        self.actionJPEG_3.setObjectName("actionJPEG_3")
        self.actionSave_image = QtWidgets.QAction(mainscreen)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(resource_path("Icons/picture.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_image.setIcon(icon1)
        self.actionSave_image.setObjectName("actionSave_image")
        self.actionclose = QtWidgets.QAction(mainscreen)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(resource_path("Icons/Close_Icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionclose.setIcon(icon2)
        self.actionclose.setObjectName("actionclose")
        self.actionExport_csv = QtWidgets.QAction(mainscreen)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(resource_path("Icons/calendar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport_csv.setIcon(icon3)
        self.actionExport_csv.setObjectName("actionExport_csv")
        self.actionOpen = QtWidgets.QAction(mainscreen)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(resource_path("Icons/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon4)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen_Recent = QtWidgets.QAction(mainscreen)
        self.actionOpen_Recent.setObjectName("actionOpen_Recent")
        self.actionNew = QtWidgets.QAction(mainscreen)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(resource_path("Icons/write.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon5)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.actionNew.setFont(font)
        self.actionNew.setObjectName("actionNew")
        self.actionDark_Mode = QtWidgets.QAction(mainscreen)
        self.actionDark_Mode.setObjectName("actionDark_Mode")
        self.actionLight_Mode = QtWidgets.QAction(mainscreen)
        self.actionLight_Mode.setObjectName("actionLight_Mode")
        self.actionJump_to = QtWidgets.QAction(mainscreen)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(resource_path("Icons/clock.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionJump_to.setIcon(icon6)
        self.actionJump_to.setObjectName("actionJump_to")
        self.actionExit = QtWidgets.QAction(mainscreen)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(resource_path("Icons/turn_off.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon7)
        self.actionExit.setObjectName("actionExit")
        self.actionShow_Summary_Table = QtWidgets.QAction(mainscreen)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(resource_path("Icons/presentation.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShow_Summary_Table.setIcon(icon8)
        self.actionShow_Summary_Table.setObjectName("actionShow_Summary_Table")
        self.menuDevelopers.addAction(self.actionLyra_2)
        self.menuDevelopers.addAction(self.actionRyan_2)
        self.menuDevelopers.addAction(self.actionKent)
        self.menuDevelopers.addAction(self.actionJoshua_2)
        self.menuDevelopers.addAction(self.actionGrant)
        self.menuAbout.addAction(self.actionThis_partition)
        self.menuAbout.addAction(self.menuDevelopers.menuAction())
        self.menuHelp.addAction(self.actionHow_to_use)
        self.menuHelp.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_image)
        self.menuFile.addAction(self.actionExport_csv)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionclose)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuAppearance_2.addAction(self.actionLight_Mode)
        self.menuAppearance_2.addAction(self.actionDark_Mode)
        self.menuAppearance.addAction(self.menuAppearance_2.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAppearance.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionHome)
        self.toolBar.addAction(self.actionJump_to)
        self.toolBar.addAction(self.actionShow_Summary_Table)

        self.label_zero = QtWidgets.QLabel(self.Group_memoryMap)
        self.label_zero.setText('0')
        self.label_zero.adjustSize()
        self.label_zero.setAlignment(QtCore.Qt.AlignRight)
        self.label_zero.setGeometry(QtCore.QRect(0, 30, 43, 13))
        self.label_zero.setObjectName("label_zero")

        self.label_memory_size = QtWidgets.QLabel(self.Group_memoryMap)
        self.label_memory_size.setText(f'{self.mem_map[0][-1]}')
        self.label_memory_size.adjustSize()
        self.label_memory_size.setAlignment(QtCore.Qt.AlignRight)
        self.label_memory_size.setGeometry(QtCore.QRect(0, self.V_END + 30, 43, 13))
        self.label_memory_size.setObjectName("label_memory_size")

        self.v_line = QtWidgets.QFrame(self.Group_memoryMap)
        self.v_line.setGeometry(QtCore.QRect(40, 40, 20, self.V_END))
        self.v_line.setLineWidth(2)
        self.v_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.v_line.setObjectName("v_line")

        self.retranslateUi(mainscreen)
        QtCore.QMetaObject.connectSlotsByName(mainscreen)
        self.make_lines(len(self.mem_map[self.idx]))
        self.make_labels(len(self.mem_map[self.idx]))
        self.make_memory_labels(self.mem_map[self.idx], self.fixed)
        self.button_state()
        self.load_job_table()
        self.load_pat_table()
        self.show_status_column()

    def retranslateUi(self, mainscreen):
        _translate = QtCore.QCoreApplication.translate
        mainscreen.setWindowTitle(_translate("mainscreen", "Static Partition"))
        self.Group_memoryMap.setTitle(_translate("mainscreen", "Memory Map"))
        self.Group_job_table.setTitle(_translate("mainscreen", "Job Table"))
        item = self.Job_Table.horizontalHeaderItem(0)
        item.setText(_translate("mainscreen", "Job"))
        item = self.Job_Table.horizontalHeaderItem(1)
        item.setText(_translate("mainscreen", "Size"))
        item = self.Job_Table.horizontalHeaderItem(2)
        item.setText(_translate("mainscreen", "Arrival time"))
        item = self.Job_Table.horizontalHeaderItem(3)
        item.setText(_translate("mainscreen", "Run time"))
        self.Group_pat_table.setTitle(_translate("mainscreen", "Partition Allocation Table"))
        item = self.PAT_Table.horizontalHeaderItem(0)
        item.setText(_translate("mainscreen", "Partition"))
        item = self.PAT_Table.horizontalHeaderItem(1)
        item.setText(_translate("mainscreen", "Size"))
        item = self.PAT_Table.horizontalHeaderItem(2)
        item.setText(_translate("mainscreen", "Location"))
        item = self.PAT_Table.horizontalHeaderItem(3)
        item.setText(_translate("mainscreen", "Status"))

        self.Group_osSize.setTitle(_translate("mainscreen", "OS Size"))
        self.OS_size_label.setText(_translate("mainscreen", f"{self.inputs['OS size']}"))
        self.Group_memSize.setTitle(_translate("mainscreen", "Memory Size"))
        self.mem_size_label.setText(_translate("mainscreen", f"{self.inputs['Memory size']}"))
        self.partition_title.setText(_translate("mainscreen", "Static Partition Memory Management"))
        self.prev_button.setText(_translate("mainscreen", "Prev"))
        self.next_button.setText(_translate("mainscreen", "Next"))
        self.simplify_cbx.setText(_translate("mainscreen", "Simplify"))
        self.message_label.setText(_translate("mainscreen", f"{self.message[0]}"))
        self.menuHelp.setTitle(_translate("mainscreen", "Help"))
        self.menuAbout.setTitle(_translate("mainscreen", "About"))
        self.menuDevelopers.setTitle(_translate("mainscreen", "Developers"))
        self.menuFile.setTitle(_translate("mainscreen", "File"))
        self.menuAppearance.setTitle(_translate("mainscreen", "View"))
        self.menuAppearance_2.setTitle(_translate("mainscreen", "Theme"))
        self.toolBar.setWindowTitle(_translate("mainscreen", "Tool Bar"))
        self.actionHome.setText(_translate("mainscreen", "Home"))
        self.actionLyra.setText(_translate("mainscreen", "Lyra"))
        self.actionRyan.setText(_translate("mainscreen", "Ryan"))
        self.actionJoshua.setText(_translate("mainscreen", "Joshua"))
        self.actionLyra_2.setText(_translate("mainscreen", "Lyra"))
        self.actionRyan_2.setText(_translate("mainscreen", "Ryan"))
        self.actionJoshua_2.setText(_translate("mainscreen", "Joshua"))
        self.actionKent.setText(_translate("mainscreen", "Kent"))
        self.actionGrant.setText(_translate("mainscreen", "Grant"))
        self.actionThis_partition.setText(_translate("mainscreen", "This partition"))
        self.actionHow_to_use.setText(_translate("mainscreen", "How to use"))
        self.actionCSV.setText(_translate("mainscreen", "CSV"))
        self.actionPNG.setText(_translate("mainscreen", "PNG"))
        self.actionJPEG.setText(_translate("mainscreen", "JPEG"))
        self.actionCSV_2.setText(_translate("mainscreen", "CSV"))
        self.actionPNG_2.setText(_translate("mainscreen", "PNG"))
        self.actionJPEG_2.setText(_translate("mainscreen", "JPEG"))
        self.actionJPEG_3.setText(_translate("mainscreen", "JPEG"))
        self.actionSave_image.setText(_translate("mainscreen", "Save Image"))
        self.actionclose.setText(_translate("mainscreen", "Close"))
        self.actionExport_csv.setText(_translate("mainscreen", "Export (.csv)"))
        self.actionOpen.setText(_translate("mainscreen", "Open"))
        self.actionOpen_Recent.setText(_translate("mainscreen", "Open Recent"))
        self.actionNew.setText(_translate("mainscreen", "New"))
        self.actionDark_Mode.setText(_translate("mainscreen", "Dark"))
        self.actionLight_Mode.setText(_translate("mainscreen", "Light"))
        self.actionJump_to.setText(_translate("mainscreen", "Jump to"))
        self.actionExit.setText(_translate("mainscreen", "Exit"))
        self.actionShow_Summary_Table.setText(_translate("mainscreen", "Summary"))
        self.next_button.clicked.connect(self.next_clicked)
        self.prev_button.clicked.connect(self.prev_clicked)
        self.actionJump_to.triggered.connect(self.jump_to)
        self.actionShow_Summary_Table.triggered.connect(self.show_summary_table)
        self.actionLight_Mode.triggered.connect(self.light_theme)
        self.actionDark_Mode.triggered.connect(self.dark_theme)
        self.simplify_cbx.stateChanged.connect(self.simplify_mem_map)
        self.actionNew.triggered.connect(self.new_input)
        self.actionExit.triggered.connect(self.quitting)

        self.actionSave_image.triggered.connect(self.message_to_user)
        self.actionExport_csv.triggered.connect(self.message_to_user)
        self.actionOpen.triggered.connect(self.message_to_user)
        self.actionHow_to_use.triggered.connect(self.message_to_user)
        self.actionThis_partition.triggered.connect(self.message_to_user)

        self.actionclose.triggered.connect(self.closing)
        self.actionHome.triggered.connect(self.goto_home)

    def goto_home(self):
        self.new_window = MyWindow()
        self.activate_window = mainUI(self.new_window)
        self.new_window.show()
        self.mainscreen.hide()

    def message_to_user(self):
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)

        info = QtWidgets.QMessageBox()
        info.setIcon(QtWidgets.QMessageBox.Information)
        info.setFont(font)
        info.setText("Sorry not available right now, we're still working on this.      ")
        info.setWindowTitle("Info")
        info.exec_()

    def closing(self):
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)

        notify_user = QtWidgets.QMessageBox()
        notify_user.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        notify_user.setDefaultButton(QtWidgets.QMessageBox.No)
        notify_user.setIcon(QtWidgets.QMessageBox.Question)
        notify_user.setFont(font)
        notify_user.setText('This will bring you to the home window, continue?      ')
        notify_user.setWindowTitle("Notify")

        if notify_user.exec_() == QtWidgets.QMessageBox.Yes:
            self.goto_home()

    def quitting(self):
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)

        notify_user = QtWidgets.QMessageBox()
        notify_user.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        notify_user.setDefaultButton(QtWidgets.QMessageBox.No)
        notify_user.setIcon(QtWidgets.QMessageBox.Question)
        notify_user.setFont(font)
        notify_user.setText('Are you sure you want to quit?      ')
        notify_user.setWindowTitle("Notify")

        if notify_user.exec_() == QtWidgets.QMessageBox.Yes:
            sys.exit()

    def dark_theme(self):
        # Palette to switch to dark colors:
        # app.setStyle("Fusion")
        global dark
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette().Window, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette().WindowText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette().Base, QtGui.QColor(25, 25, 25))
        palette.setColor(QtGui.QPalette().AlternateBase, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette().ToolTipBase, QtCore.Qt.black)
        palette.setColor(QtGui.QPalette().ToolTipText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette().Text, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette().Button, QtGui.QColor(53, 53, 53))
        palette.setColor(QtGui.QPalette().ButtonText, QtCore.Qt.white)
        palette.setColor(QtGui.QPalette().BrightText, QtCore.Qt.red)
        palette.setColor(QtGui.QPalette().Link, QtGui.QColor(42, 130, 218))
        palette.setColor(QtGui.QPalette().Highlight, QtGui.QColor(42, 130, 218))
        palette.setColor(QtGui.QPalette().HighlightedText, QtCore.Qt.black)
        app.setPalette(palette)
        self.PAT_Table.horizontalHeader().setStyleSheet(
            'QHeaderView::section { border: none; border-bottom: 2px solid #2A74BB;}')
        self.Job_Table.horizontalHeader().setStyleSheet(
            'QHeaderView::section { border: none; border-bottom: 2px solid green;}')
        self.dark_theme_enabled = True
        dark = True
        self.show_MMlabel_LOC(self.mem_map[self.idx], self.fixed)

    def light_theme(self):
        global dark
        palette = QtGui.QPalette()
        app.setPalette(palette)
        self.PAT_Table.horizontalHeader().setStyleSheet(
            'QHeaderView::section { border: none; border-bottom: 2px solid #2A74BB;}')
        self.Job_Table.horizontalHeader().setStyleSheet(
            'QHeaderView::section { border: none; border-bottom: 2px solid green;}')
        self.dark_theme_enabled = False
        dark = False
        self.show_MMlabel_LOC(self.mem_map[self.idx], self.fixed)

    def load_job_table(self):
        size = self.inputs['Size']
        arrival = self.inputs['Arrival time']
        run = self.inputs['Run time']
        self.Job_Table.setRowCount(len(size))
        for row in range(len(size)):
            self.Job_Table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(row + 1)))
            self.Job_Table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(size[row])))
            self.Job_Table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(arrival[row])))
            self.Job_Table.setItem(row, 3, QtWidgets.QTableWidgetItem(str(run[row])))

    def load_pat_table(self):
        self.PAT_Table.setRowCount(len(self.partition_size))
        for row in range(len(self.partition_size)):
            self.PAT_Table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(row + 1)))
            self.PAT_Table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(self.partition_size[row])))
            self.PAT_Table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(self.mem_map[0][row])))
            # self.PAT_Table.setItem(row, 3, QtWidgets.QTableWidgetItem(str(psize[row])))

    def show_status_column(self):
        for row in range(len(self.status_table[self.idx])):
            self.PAT_Table.setItem(row, 3, QtWidgets.QTableWidgetItem(str(self.status_table[self.idx][row])))

    def simplify_mem_map(self):
        if self.simplify_cbx.isChecked():
            if self.fixed == False:
                self.fixed = True
        else:
            if self.fixed == True:
                self.fixed = False
        self.show_line_LOC(self.mem_map[self.idx], self.fixed)
        self.show_label_LOC(self.mem_map[self.idx], self.fixed)
        self.show_MMlabel_LOC(self.mem_map[self.idx], self.fixed)

    def button_state(self):
        if self.idx == len(self.mem_map) - 1:
            self.next_button.setEnabled(False)
            self.end_show = True
            # self.summaryButton.setStyleSheet("color: blue")
        else:
            self.next_button.setEnabled(True)

        if self.idx == 0:
            self.prev_button.setEnabled(False)
        else:
            self.prev_button.setEnabled(True)

        # self.summaryButton.setEnabled(self.end_show)

    def new_input(self):
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)

        notify_user = QtWidgets.QMessageBox()
        # notify_user.question()
        notify_user.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        notify_user.setDefaultButton(QtWidgets.QMessageBox.Yes)
        notify_user.setIcon(QtWidgets.QMessageBox.Question)
        notify_user.setFont(font)
        notify_user.setText('New file?      ')
        notify_user.setWindowTitle("Notify")

        if notify_user.exec_() == QtWidgets.QMessageBox.Yes:
            self.new_window = mainscreen()
            self.activate_window = SP_InputWindow(self.new_window)
            self.new_window.show()
            self.mainscreen.hide()

    def next_clicked(self):
        try:
            self.idx += 1
            self.message_label.setText(self.message[self.idx])
            self.message_label.setAlignment(QtCore.Qt.AlignCenter)
            self.message_label.adjustSize()

            self.show_status_column()
            self.show_line_LOC(self.mem_map[self.idx], self.fixed)
            self.show_label_LOC(self.mem_map[self.idx], self.fixed)
            self.show_MMlabel_LOC(self.mem_map[self.idx], self.fixed)
        except IndexError:
            if self.error_msg_value == 0:
                self.mainscreen.setWindowTitle('An error as occured when processing your data :(')
                self.show_error_message()
                self.error_msg_value = 1
        self.button_state()

    def prev_clicked(self):
        try:
            self.idx -= 1
            self.message_label.setText(self.message[self.idx])
            self.message_label.setAlignment(QtCore.Qt.AlignCenter)
            self.message_label.adjustSize()

            self.show_status_column()
            self.show_line_LOC(self.mem_map[self.idx], self.fixed)
            self.show_label_LOC(self.mem_map[self.idx], self.fixed)
            self.show_MMlabel_LOC(self.mem_map[self.idx], self.fixed)

        except IndexError:
            if self.error_msg_value == 0:
                self.mainscreen.setWindowTitle('An error as occured when processing your data :(')
                self.show_error_message()
                self.error_msg_value = 1
        self.button_state()

    def show_error_message(self):
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)

        info = QtWidgets.QMessageBox()
        info.setIcon(QtWidgets.QMessageBox.Information)
        info.setFont(font)
        info.setTextFormat(QtCore.Qt.RichText)
        info.setText("Sorry, an error has occured when I begin to process your data. We're still working on this, please try another input. \
                     <a href='https://www.facebook.com/xtnctx'><br><br>Tell me about the error</br></br></a>    ")
        info.setWindowTitle("Developer message")
        info.exec_()

    # Make unique objects returning in different memory location (of Python)
    def make_lines(self, length):
        self.new_mem_map = fcn.margin_memory_loc(self.mem_map[self.idx], self.V_END, y=30, fixed=self.fixed)
        for i in range(length - 1):
            self.d[f"self.horizontal_line{i}"] = QtWidgets.QFrame(self.Group_memoryMap)
            self.d[f"self.horizontal_line{i}"].setLineWidth(2)
            self.d[f"self.horizontal_line{i}"].setGeometry(QtCore.QRect(50, self.new_mem_map[i] + 20, 251, 16))
            self.d[f"self.horizontal_line{i}"].setFrameShape(QtWidgets.QFrame.HLine)
            self.d[f"self.horizontal_line{i}"].setFrameShadow(QtWidgets.QFrame.Raised)
            self.d[f"self.horizontal_line{i}"].setObjectName("horizontal_line")
        return self.d

    def make_labels(self, length):
        self.new_mem_map = fcn.margin_memory_loc(self.mem_map[self.idx], self.V_END, y=30, fixed=self.fixed)
        for i in range(length - 1):
            self.labels[f"self.pointer_label{i}"] = QtWidgets.QLabel(self.Group_memoryMap)
            self.labels[f"self.pointer_label{i}"].setText(f"{self.mem_map[self.idx][i]}")
            self.labels[f"self.pointer_label{i}"].adjustSize()
            self.labels[f"self.pointer_label{i}"].setAlignment(QtCore.Qt.AlignRight)
            self.labels[f"self.pointer_label{i}"].setGeometry(QtCore.QRect(0, self.new_mem_map[i] + 20, 43, 13))
            self.labels[f"self.pointer_label{i}"].setObjectName("pointer_label")
        return self.labels

    def make_memory_labels(self, mem_map, fixed):
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(80)
        font.setKerning(True)

        self.new_mem_map = fcn.margin_memory_loc(mem_map, self.V_END, y=30, fixed=fixed)
        self.memory_label_yloc = fcn.memory_label_yloc([self.new_mem_map], self.fixed)

        length = len(mem_map)
        for i in range(length):
            self.mem_labels[f"self.memory_label{i}"] = QtWidgets.QLabel(self.Group_memoryMap)
            if 'J' in self.label[self.idx][i]:
                font.setPointSize(10)
                if self.dark_theme_enabled:
                    self.mem_labels[f"self.memory_label{i}"].setFont(font)
                    self.mem_labels[f"self.memory_label{i}"].setStyleSheet("color: #44B432")
                else:
                    self.mem_labels[f"self.memory_label{i}"].setFont(font)
                    self.mem_labels[f"self.memory_label{i}"].setStyleSheet("color: #6FBE28")
            elif 'wasted' in self.label[self.idx][i]:
                font.setPointSize(8)
                if self.dark_theme_enabled:
                    self.mem_labels[f"self.memory_label{i}"].setFont(font)
                    self.mem_labels[f"self.memory_label{i}"].setStyleSheet("color: #C64943")
                else:
                    self.mem_labels[f"self.memory_label{i}"].setFont(font)
                    self.mem_labels[f"self.memory_label{i}"].setStyleSheet("color: #D84B4B")
            elif 'P' in self.label[self.idx][i]:
                font.setPointSize(10)
                if self.dark_theme_enabled:
                    self.mem_labels[f"self.memory_label{i}"].setFont(font)
                    self.mem_labels[f"self.memory_label{i}"].setStyleSheet("color: #436DC6")
                else:
                    self.mem_labels[f"self.memory_label{i}"].setFont(font)
                    self.mem_labels[f"self.memory_label{i}"].setStyleSheet("color: #3C5277")
            else:
                font.setPointSize(10)
                if self.dark_theme_enabled:
                    self.mem_labels[f"self.memory_label{i}"].setFont(font)
                    self.mem_labels[f"self.memory_label{i}"].setStyleSheet("color: #DBDBDB")
                else:
                    self.mem_labels[f"self.memory_label{i}"].setFont(font)
                    self.mem_labels[f"self.memory_label{i}"].setStyleSheet("color: #4F4F4F")
            self.mem_labels[f"self.memory_label{i}"].setText(f"{self.label[self.idx][i]}")
            self.mem_labels[f"self.memory_label{i}"].adjustSize()
            self.mem_labels[f"self.memory_label{i}"].setAlignment(QtCore.Qt.AlignCenter)
            self.mem_labels[f"self.memory_label{i}"].setGeometry(
                QtCore.QRect(50, self.memory_label_yloc[0][i] + 20, 270, 13))
            self.mem_labels[f"self.memory_label{i}"].setObjectName("memory_label")

    # Configure assigned variables from dictionary
    def show_line_LOC(self, mem_map, fixed):
        self.new_mem_map = fcn.margin_memory_loc(mem_map, self.V_END, y=30, fixed=fixed)
        # Add missing widget
        if len(self.new_mem_map) > len(self.d) + 1:
            for missing in range(len(self.d), len(self.new_mem_map) - 1):
                self.d[f"self.horizontal_line{missing}"] = QtWidgets.QFrame(self.Group_memoryMap)
                self.d[f"self.horizontal_line{missing}"].setLineWidth(2)
                self.d[f"self.horizontal_line{missing}"].setGeometry(
                    QtCore.QRect(50, self.new_mem_map[missing] + 20, 251, 16))
                self.d[f"self.horizontal_line{missing}"].setFrameShape(QtWidgets.QFrame.HLine)
                self.d[f"self.horizontal_line{missing}"].setFrameShadow(QtWidgets.QFrame.Raised)
                self.d[f"self.horizontal_line{missing}"].setObjectName("horizontal_line")

        # Show widget
        d = dict(itertools.islice(self.d.items(), len(self.new_mem_map) - 1))
        for i in range(len(d)):
            d[f"self.horizontal_line{i}"].setLineWidth(2)
            d[f"self.horizontal_line{i}"].setGeometry(QtCore.QRect(50, self.new_mem_map[i] + 20, 251, 16))
            d[f"self.horizontal_line{i}"].setFrameShape(QtWidgets.QFrame.HLine)
            d[f"self.horizontal_line{i}"].setFrameShadow(QtWidgets.QFrame.Raised)
            d[f"self.horizontal_line{i}"].setObjectName("horizontal_line")
            d[f"self.horizontal_line{i}"].show()

        # Hide the excess widget
        for k in range(len(d), len(self.d)):
            self.d[f"self.horizontal_line{k}"].hide()
            # del self.d[f"self.horizontal_line{k}"]

    def show_label_LOC(self, mem_map, fixed):
        self.new_mem_map = fcn.margin_memory_loc(mem_map, self.V_END, y=30, fixed=fixed)
        if len(self.new_mem_map) > len(self.labels) + 1:
            for missing in range(len(self.labels), len(self.new_mem_map) - 1):
                self.labels[f"self.pointer_label{missing}"] = QtWidgets.QLabel(self.Group_memoryMap)
                self.labels[f"self.pointer_label{missing}"].setText(f"{mem_map[missing]}")
                self.labels[f"self.pointer_label{missing}"].adjustSize()
                self.labels[f"self.pointer_label{missing}"].setAlignment(QtCore.Qt.AlignRight)
                self.labels[f"self.pointer_label{missing}"].setGeometry(
                    QtCore.QRect(0, self.new_mem_map[missing] + 20, 43, 13))
                self.labels[f"self.pointer_label{missing}"].setObjectName("pointer_label")

        p = dict(itertools.islice(self.labels.items(), len(self.new_mem_map) - 1))
        for i in range(len(p)):
            p[f"self.pointer_label{i}"].setText(f"{mem_map[i]}")
            p[f"self.pointer_label{i}"].adjustSize()
            p[f"self.pointer_label{i}"].setAlignment(QtCore.Qt.AlignRight)
            p[f"self.pointer_label{i}"].setGeometry(QtCore.QRect(0, self.new_mem_map[i] + 20, 43, 13))
            p[f"self.pointer_label{i}"].setObjectName("pointer_label")
            p[f"self.pointer_label{i}"].show()

        for k in range(len(p), len(self.labels)):
            self.labels[f"self.pointer_label{k}"].hide()
            # del self.labels[f"self.pointer_label{k}"]

    def show_MMlabel_LOC(self, mem_map, fixed):
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(80)
        font.setKerning(True)

        self.new_mem_map = fcn.margin_memory_loc(mem_map, self.V_END, y=30, fixed=fixed)
        self.memory_label_yloc = fcn.memory_label_yloc([self.new_mem_map], self.fixed)

        if len(self.memory_label_yloc[0]) > len(self.mem_labels):
            for missing in range(len(self.mem_labels), len(self.memory_label_yloc[0])):
                self.mem_labels[f"self.memory_label{missing}"] = QtWidgets.QLabel(self.Group_memoryMap)
                self.mem_labels[f"self.memory_label{missing}"].setText(f"{self.label[self.idx][missing]}")
                self.mem_labels[f"self.memory_label{missing}"].adjustSize()
                self.mem_labels[f"self.memory_label{missing}"].setAlignment(QtCore.Qt.AlignCenter)
                self.mem_labels[f"self.memory_label{missing}"].setGeometry(QtCore.QRect(50,
                                                                                        self.memory_label_yloc[0][
                                                                                            missing] + 20, 270, 13))
                self.mem_labels[f"self.memory_label{missing}"].setObjectName("memory_label")

        elif len(self.memory_label_yloc[0]) < len(self.mem_labels):
            for k in range(len(self.memory_label_yloc[0]), len(self.mem_labels)):
                self.mem_labels[f"self.memory_label{k}"].hide()
                del self.mem_labels[f"self.memory_label{k}"]

        for i in range(len(self.mem_labels)):
            if 'J' in self.label[self.idx][i]:
                font.setPointSize(10)
                if self.dark_theme_enabled:
                    self.mem_labels[f"self.memory_label{i}"].setFont(font)
                    self.mem_labels[f"self.memory_label{i}"].setStyleSheet("color: #44B432")
                else:
                    self.mem_labels[f"self.memory_label{i}"].setFont(font)
                    self.mem_labels[f"self.memory_label{i}"].setStyleSheet("color: #3C773D")
            elif 'wasted' in self.label[self.idx][i]:
                font.setPointSize(8)
                if self.dark_theme_enabled:
                    self.mem_labels[f"self.memory_label{i}"].setFont(font)
                    self.mem_labels[f"self.memory_label{i}"].setStyleSheet("color: #C64943")
                else:
                    self.mem_labels[f"self.memory_label{i}"].setFont(font)
                    self.mem_labels[f"self.memory_label{i}"].setStyleSheet("color: #823D3D")
            elif 'P' in self.label[self.idx][i]:
                font.setPointSize(10)
                if self.dark_theme_enabled:
                    self.mem_labels[f"self.memory_label{i}"].setFont(font)
                    self.mem_labels[f"self.memory_label{i}"].setStyleSheet("color: #436DC6")
                else:
                    self.mem_labels[f"self.memory_label{i}"].setFont(font)
                    self.mem_labels[f"self.memory_label{i}"].setStyleSheet("color: #3C5277")
            else:
                font.setPointSize(10)
                if self.dark_theme_enabled:
                    self.mem_labels[f"self.memory_label{i}"].setFont(font)
                    self.mem_labels[f"self.memory_label{i}"].setStyleSheet("color: #DBDBDB")
                else:
                    self.mem_labels[f"self.memory_label{i}"].setFont(font)
                    self.mem_labels[f"self.memory_label{i}"].setStyleSheet("color: #4F4F4F")
            self.mem_labels[f"self.memory_label{i}"].setText(f"{self.label[self.idx][i]}")
            self.mem_labels[f"self.memory_label{i}"].adjustSize()
            self.mem_labels[f"self.memory_label{i}"].setGeometry(
                QtCore.QRect(50, self.memory_label_yloc[0][i] + 20, 270, 13))
            self.mem_labels[f"self.memory_label{i}"].setAlignment(QtCore.Qt.AlignCenter)
            self.mem_labels[f"self.memory_label{i}"].setObjectName("memory_label")
            self.mem_labels[f"self.memory_label{i}"].show()

    def show_summary_table(self):
        self.second_ui = SummaryTableWindow([self.start_time, self.finish, self.cpu_wait])

    def jump_to(self):
        self.new_window = QtWidgets.Qmainscreen()
        self.second_ui = Partition_TimeList(self.new_window)
        self.second_ui.pushButton.clicked.connect(self.go_)
        self.new_window.show()

    def go_(self):
        if not self.idx == self.second_ui.comboBox.currentIndex():
            self.idx = self.second_ui.comboBox.currentIndex()
            self.message_label.setText(self.message[self.idx])
            self.message_label.setAlignment(QtCore.Qt.AlignCenter)
            self.message_label.adjustSize()

            self.show_status_column()
            self.show_line_LOC(self.mem_map[self.idx], self.fixed)
            self.show_label_LOC(self.mem_map[self.idx], self.fixed)
            self.show_MMlabel_LOC(self.mem_map[self.idx], self.fixed)

            self.button_state()


class MyWindow(QtWidgets.QMainWindow):
    def closeEvent(self, event):
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)

        notify_user = QtWidgets.QMessageBox()
        notify_user.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        notify_user.setDefaultButton(QtWidgets.QMessageBox.No)
        notify_user.setIcon(QtWidgets.QMessageBox.Question)
        notify_user.setFont(font)
        notify_user.setText('Are you sure you want to quit?      ')
        notify_user.setWindowTitle("Notify")
        event.ignore()

        if notify_user.exec_() == QtWidgets.QMessageBox.Yes:
            event.accept()


if __name__ == "__main__":
    suppress_qt_warnings()
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(Style)
    BATMAS = mainUI()
    ui = BATMAS.mainscreen
    BATMAS.mainscreen()
    sys.exit(app.exec_())


# Create the main UI object
BATMAS = mainUI(mainscreen, app)
BATMAS.mainscreen()
root.mainloop()
