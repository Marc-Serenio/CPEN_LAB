from tkinter import *
from tkinter import messagebox, PhotoImage, Label, Button
from tkinter import Canvas, Tk
import os
import pandas as pd
import tkinter as tk
from PIL import Image, ImageTk
from fcn import *
import json
import re


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

    def STATIC_create_job_entries(self):

        self.clearWidgets()


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
        canvas.create_rectangle(10, 10, 390, 190, fill="gray")
        x = 10
        for job_size in job_sizes:
            canvas.create_rectangle(x, 10, x + job_size, 190, fill="blue")
            x += job_size + 10


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

    def find_job_in_status(status, t):
        for s in range(len(status)):
            try:
                J = re.search(f'Allocated (.*)', status[s]).group(1)
                if t == J:
                    return s
            except AttributeError:
                pass

    def create_mem_map(status, loc, job_size):
        loc_copy = loc.copy()
        for i in range(len(status)):
            if 'Allocated' in status[i]:
                J = re.search(f'Allocated J(.*)', status[i]).group(1)
                x = status.index(status[i])
                x = loc.index(loc_copy[x])
                loc.insert(x + 1, loc[x] + job_size[(int(J) - 1)])
        return list(sorted(set(loc)))

    def first_fit_available(status, job_index, P, J):
        for i in range(len(status)):
            if status[i] == 'available' and P[i] >= J[job_index]:
                return i

    def static_partition_EXEC(file_name):
        file = open(f'{file_name}.json')
        data = json.load(file)

        MEMORY_SIZE = data['Memory size']
        OS_SIZE = data['OS size']
        PARTITION_SIZE = data['Partition size']
        PARTITION_SIZE = [i for i in PARTITION_SIZE if i != 0]

        jobs = data['Job']
        job_size = data['Size']
        arrival_time = data['Arrival time']
        run_time = data['Run time']

        file.close()

        if OS_SIZE <= 0 or MEMORY_SIZE <= OS_SIZE:
            print('Invalid memory size')
            exit()

        LOCATION = [OS_SIZE]

        total_PARTITION_SIZE = (sum(PARTITION_SIZE) + OS_SIZE)
        if total_PARTITION_SIZE <= MEMORY_SIZE:
            if (MEMORY_SIZE - total_PARTITION_SIZE) != 0:
                PARTITION_SIZE.append(MEMORY_SIZE - total_PARTITION_SIZE)
        else:
            print('Invalid partition')
            exit()

        for i in PARTITION_SIZE:
            LOCATION.append(i + LOCATION[-1])
        status = ['available'] * len(PARTITION_SIZE)

        Ft = {}
        St = {}
        for i in jobs:
            Ft[f'{i}'] = ''
            St[f'{i}'] = ''

        ter = ''
        terminating = {}
        waiting = []
        msg = [f'Before {arrival_time[0]}']

        status_table = [status]
        job_index = 0
        LOC = [LOCATION]
        for job_index in range(len(arrival_time)):
            # status = status.copy()
            arrival_minutes = to_minutes(arrival_time[job_index])
            # Terminated
            if len(terminating) > 0:
                for _ in range(list(terminating.values()).count(list(terminating.values())[0])):
                    if arrival_minutes >= list(terminating.values())[0]:
                        ter = list(terminating.values())[0]
                        t_time = time_format('00:' + str(ter))
                        msg.append(f'At {t_time}, {list(terminating)[0]} terminated')
                        x = find_job_in_status(status, list(terminating)[0])
                        terminating.pop(list(terminating)[0])
                        status[x] = 'available'
                        status_table.append(list(status))
                        LOC.append(create_mem_map(status, LOCATION.copy(), job_size))

            # Waiting starts
            if len(waiting) != 0:
                status_index = first_fit_available(status, waiting[0], PARTITION_SIZE, job_size)
                for w in waiting:
                    if status_index != None:
                        if status[status_index] == 'available' and PARTITION_SIZE[status_index] >= job_size[w]:
                            tf = time_format('00:' + str(ter))
                            msg.append(f'At {tf}, J{waiting[0] + 1} starts')
                            status[status_index] = f'Allocated J{w + 1}'
                            status_table.append(list(status))
                            LOC.append(create_mem_map(status, LOCATION.copy(), job_size))
                            terminating[f'J{w + 1}'] = ter + run_time[w]
                            terminating = {k: v for k, v in
                                           sorted(terminating.items(), key=lambda item: item[1])}  # Sort dict by values
                            St[f'{w + 1}'] = time_format('00:' + str(ter))
                            Ft[f'{w + 1}'] = time_format('00:' + str(ter + run_time[w]))
                            waiting.pop(0)

            # Waits
            status_index = first_fit_available(status, job_index, PARTITION_SIZE, job_size)
            if status_index == None:
                waiting.append(job_index)
            elif len(waiting) != 0:
                if arrival_minutes > to_minutes(arrival_time[waiting[0]]):
                    waiting.append(job_index)
            # Arrived/Starts
            else:
                if status[status_index] == 'available' and PARTITION_SIZE[status_index] >= job_size[job_index]:
                    msg.append(f'At {arrival_time[job_index]}, J{job_index + 1} arrived/starts')
                    status[status_index] = f'Allocated J{job_index + 1}'
                    status_table.append(list(status))
                    LOC.append(create_mem_map(status, LOCATION.copy(), job_size))
                    terminating[f'J{job_index + 1}'] = arrival_minutes + run_time[job_index]
                    terminating = {k: v for k, v in
                                   sorted(terminating.items(), key=lambda item: item[1])}  # Sort dict by values
                    St[f'{job_index + 1}'] = arrival_time[job_index]
                    Ft[f'{job_index + 1}'] = time_format('00:' + str(arrival_minutes + run_time[job_index]))

        while len(waiting) > 0:  # Start the jobs in waiting queues
            status_index = first_fit_available(status, waiting[0], PARTITION_SIZE, job_size)
            if status_index == None:
                for _ in range(list(terminating.values()).count(list(terminating.values())[0])):
                    ter = list(terminating.values())[0]
                    t_time = time_format('00:' + str(ter))
                    msg.append(f'At {t_time}, {list(terminating)[0]} terminated')
                    x = find_job_in_status(status, list(terminating)[0])
                    terminating.pop(list(terminating)[0])
                    status[x] = 'available'
                    status_table.append(list(status))
                    LOC.append(create_mem_map(status, LOCATION.copy(), job_size))
            else:
                for w in waiting:
                    if status_index != None:
                        if status[status_index] == 'available' and PARTITION_SIZE[status_index] >= job_size[w]:
                            tf = time_format('00:' + str(ter))
                            msg.append(f'At {tf}, J{waiting[0] + 1} starts')
                            status[status_index] = f'Allocated J{w + 1}'
                            status_table.append(list(status))
                            LOC.append(create_mem_map(status, LOCATION.copy(), job_size))
                            terminating[f'J{w + 1}'] = ter + run_time[w]
                            terminating = {k: v for k, v in
                                           sorted(terminating.items(), key=lambda item: item[1])}  # Sort dict by values
                            St[f'{w + 1}'] = time_format('00:' + str(ter))
                            Ft[f'{w + 1}'] = time_format('00:' + str(ter + run_time[w]))
                            waiting.pop(0)
        else:
            for i in range(len(terminating)):
                try:
                    ter = list(terminating.values())[0]
                    t_time = time_format('00:' + str(ter))
                    msg.append(f'At {t_time}, {list(terminating)[0]} terminated')
                    x = find_job_in_status(status, list(terminating)[0])
                    terminating.pop(list(terminating)[0])
                    status[x] = 'available'
                    status_table.append(list(status))
                    LOC.append(create_mem_map(status, LOCATION.copy(), job_size))
                except TypeError:
                    pass

        CPU_Wait = [to_minutes(list(St.values())[i]) - to_minutes(arrival_time[i]) for i in
                    range(len(list(St.values())))]
        Start = list(St.values())
        Finish = list(Ft.values())

        x = generate_memory_label(LOC, status_table, LOCATION, fixed=False)[0]
        for i in range(len(x)):
            for j in range(len(x[i])):
                try:
                    W = re.search(f'wasted(.*)', x[i][j]).group(1)
                    if 'wasted' in x[i][j]:
                        j_index = 0
                        num = ''
                        for k in range(len(x[i][j - 1])):
                            if x[i][j - 1][k].isdigit():
                                num += x[i][j - 1][k]
                        j_index = int(num)
                        x[i][j] = f'wasted ({PARTITION_SIZE[int(W) - 1] - job_size[j_index - 1]})'
                except (AttributeError, ValueError):
                    pass

        for i in range(len(x)):
            for j in range(len(x[i])):
                try:
                    J = re.search(f'J(.*)', x[i][j]).group(1)
                    if 'J' in x[i][j]:
                        x[i][j] += f' ({job_size[int(J) - 1]})'
                except (AttributeError, ValueError):
                    pass

        for i in range(len(x)):
            for j in range(len(x[i])):
                try:
                    P = re.search(f'P(.*)', x[i][j]).group(1)
                    if 'P' in x[i][j]:
                        x[i][j] += f' ({PARTITION_SIZE[int(P) - 1]})'
                except (AttributeError, ValueError):
                    pass

        class Process:
            def __init__(self, pid, size):
                self.pid = pid
                self.size = size

class Process:
    def __init__(self, pid, size):
        self.pid = pid
        self.size = size

class Partition:
    def __init__(self, size):
        self.size = size
        self.process = None

def static_partitioning(processes, partitions):
    processes.sort(key=lambda x: x.size)
    partitions.sort(key=lambda x: x.size)

    for process in processes:
        for partition in partitions:
            if partition.process is None and partition.size >= process.size:
                partition.process = process
                break

    print("Static Partitioning:")
    for i, partition in enumerate(partitions):
        if partition.process is not None:
            print(f"Partition {i+1}: Allocated to process {partition.process.pid} of size {partition.process.size}")
        else:
            print(f"Partition {i+1}: Empty (size {partition.size})")

    print("\nPartition Table:")
    print("Partition #\tProcess #\tSize")
    for i, partition in enumerate(partitions):
        if partition.process is not None:
            print(f"{i+1}\t\t{partition.process.pid}\t\t{partition.process.size}")
        else:
            print(f"{i+1}\t\t-\t\t{partition.size}")

# Example usage
        processes = [Process(1, 10), Process(2, 20), Process(3, 30), Process(4, 40)]
        partitions = [Partition(10), Partition(20), Partition(30), Partition(40)]

        static_partitioning(processes, partitions)
        return [LOC, x, msg, status_table, PARTITION_SIZE, Start, Finish, CPU_Wait]


# Create the main UI object
BATMAS = mainUI()
BATMAS.mainscreen()
root.mainloop()
