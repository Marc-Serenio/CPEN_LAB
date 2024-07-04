from tkinter import *
from tkinter import messagebox
import os
import pandas as pd
import threading
from PIL import Image, ImageTk
from subprocess import run
from datetime import datetime, timedelta

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

root = Tk()
root.title("Memory Management")
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
image_9 = load_image("statictopper.png")
image_D = load_image("entrytopper1_Dnew.png")
image_DD = load_image("dynamicup.png")
image_F = load_image("dynamicfront.png")

BUTTONOPT1 = load_image('HEADERB1.png')
BUTTONOPT2 = load_image('HEADERB2.png')
BUTTONOPT3 = load_image('HEADERB3.png')
BUTTONOPT4 = load_image('HEADERB4.png')
BUTTONSPEC1 = load_image('SPEC1.png')
BUTTONSPEC2 = load_image('SPEC2.png')
BUTTONSPEC3 = load_image('SPEC3.png')
BUTTONSPEC4 = load_image('SPEC4.png')

class mainUI:
    def __init__(self, root):
        self.root = root
        self.basicWidgetList = []
        self.current_timestamp = 0

    def go_back(self):
        self.back_button.place_forget()
        self.exit_button.place_forget()
        self.clearWidgets()

    def clearWidgets(self):
        for widget in self.basicWidgetList:
            widget.destroy()
        self.basicWidgetList = []

    def os_size_value(self):
        for widget in self.basicWidgetList:
            self.basicWidgetList = []

    def dynamicComm(self):
        root.destroy()
        run(["python", "DynamicFirstFit.py"])

    def BEstyComm(self):
        root.destroy()
        run(["python", "DynamicBestFit1.py"])

    def memory_size_value(self):
        for widget in self.basicWidgetList:
            self.basicWidgetList = []

    def mainscreen(self):
        self.clearWidgets()

        if image_3:
            self.mainscreenlogo = Label(root, image=image_3, borderwidth="0", highlightthickness="0", relief="flat", activebackground="black", background="black")
            self.mainscreenlogo.place(x=5, y=0)
            self.basicWidgetList.append(self.mainscreenlogo)

        self.bg1LBL = Label(root, bg="black")
        self.bg1LBL.place(x=0, y=0)
        self.basicWidgetList.append(self.bg1LBL)

        if BUTTONOPT2:
            self.LOGOBUTTON1 = Button(root, image=BUTTONOPT2, command=self.mainInput1_window, bg="black", border=0, relief="groove")
            self.LOGOBUTTON1.place(x=70, y=500)
            self.basicWidgetList.append(self.LOGOBUTTON1)

        if BUTTONOPT3:
            self.LOGOBUTTON2 = Button(root, image=BUTTONOPT3, command=self.staticmainInput1_window, bg="black", border=0, relief="groove")
            self.LOGOBUTTON2.place(x=360, y=500)
            self.basicWidgetList.append(self.LOGOBUTTON2)

        if BUTTONOPT4:
            self.LOGOBUTTON3 = Button(root, image=BUTTONOPT4, command=self.mainscreen1, bg="black", border=0, relief="groove")
            self.LOGOBUTTON3.place(x=640, y=500)
            self.basicWidgetList.append(self.LOGOBUTTON3)

        if image_6:
            self.LOGOBUTTON5 = Button(root, image=image_6, command=self.Batmassonic_screen, bg="black", border=0, relief="groove")
            self.LOGOBUTTON5.place(x=20, y=20)
            self.basicWidgetList.append(self.LOGOBUTTON5)

    def mainscreen1(self):
        self.clearWidgets()
        self.basicWidgetList = []

        self.bg1LBL1 = Label(root, bg="black")
        self.bg1LBL1.place(x=0, y=0)
        self.basicWidgetList.append(self.bg1LBL1)

        if image_F:
            self.mainscreenlogo = Label(root, image=image_F, borderwidth="0", highlightthickness="0", relief="flat", activebackground="black", background="black")
            self.mainscreenlogo.place(x=20, y=-40)
            self.basicWidgetList.append(self.mainscreenlogo)

        if BUTTONSPEC1:
            self.LOGOBUTTON8 = Button(root, image=BUTTONSPEC1, bg="black", border=0, relief="groove", command=self.dynamicComm)
            self.LOGOBUTTON8.place(x=230, y=450)
            self.basicWidgetList.append(self.LOGOBUTTON8)

        if BUTTONSPEC3:
            self.LOGOBUTTON10 = Button(root, image=BUTTONSPEC3, bg="black", border=0, relief="groove", command=self.BEstyComm)
            self.LOGOBUTTON10.place(x=530, y=450)
            self.basicWidgetList.append(self.LOGOBUTTON10)

        self.back_buttonD = Button(root, text="Back", command=self.mainscreen, font=('Poppins', 18, 'bold'), fg='gray', width=20, bg='#4b3621', height=2, borderwidth=4, relief='sunken')
        self.back_buttonD.place(x=328, y=580)
        self.basicWidgetList.append(self.back_buttonD)

    def mainInput1_window(self):
        self.clearWidgets()
        self.basicWidgetList = []

        self.entry_frame = Frame(root, bg="black")
        self.entry_frame.place(x=50, y=110)
        self.basicWidgetList.append(self.entry_frame)

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

        self.entry_memory_size = Entry(root, font=('Poppins', 30, 'bold'), justify="center", width=18)
        self.entry_memory_size.place(x=390, y=250)
        self.basicWidgetList.append(self.entry_memory_size)

        self.job_numLBL = Label(root, text="Number of Jobs", font=('Poppins', 18, 'bold'), bg="#eec894", height=2, width=19, borderwidth=4, relief="raised")
        self.job_numLBL.place(x=90, y=320)
        self.basicWidgetList.append(self.job_numLBL)

        self.entry_job_num = Entry(root, font=('Poppins', 30, 'bold'), justify="center", width=18)
        self.entry_job_num.place(x=390, y=320)
        self.basicWidgetList.append(self.entry_job_num)

        self.job_entries = []
        self.job_frame = Frame(self.entry_frame, bg="black")
        self.job_frame.grid(row=6, columnspan=5)
        self.basicWidgetList.append(self.job_frame)

        self.set_jobs_button = Button(root, text="Set Jobs", command=self.create_job_entries, font=('Poppins', 18, 'bold'), width=20, bg="#b8804c", height=2, borderwidth=4, relief="sunken")
        self.set_jobs_button.place(x=330, y=450)
        self.basicWidgetList.append(self.set_jobs_button)

        self.back_button = Button(root, text="Back", command=self.mainscreen, font=('Poppins', 18, 'bold'), fg='gray', width=20, bg='#4b3621', height=2, borderwidth=4, relief='sunken')
        self.back_button.place(x=328, y=550)
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

    def hhmm_to_ms(self, time_str):
        hh, mm = map(int, time_str.split(':'))
        total_ms = (hh * 60 * 60 * 1000) + (mm * 60 * 1000)
        return total_ms

    def ms_to_hhmm(self, total_ms):
        hh = total_ms // (60 * 60 * 1000)
        total_ms %= (60 * 60 * 1000)
        mm = total_ms // (60 * 1000)
        return f"{hh:02}:{mm:02}"

    def create_job_entries(self):
        try:
            num_jobs = int(self.entry_job_num.get())
            for widget in self.job_frame.winfo_children():
                widget.destroy()
            self.job_entries.clear()

            self.hide_initial_inputs()

            for i in range(num_jobs):
                Label(self.job_frame, text=f"Job {i + 1}", font=('Poppins', 10, 'bold'), bg="#000000", fg="#FFFFFF", width=9, relief="flat").grid(row=i, column=0)
                Label(self.job_frame, text=f"Job Size:", font=('Poppins', 9, 'bold'), bg="#D3A075", width=12, relief="groove").grid(row=i, column=1, padx=0)
                entry_job_size = Entry(self.job_frame, font=('Poppins', 10, 'bold'), justify="center", width=15)
                entry_job_size.grid(row=i, column=2, padx=20)
                Label(self.job_frame, text=f"Arrival Time (hh:mm):", font=('Poppins', 9, 'bold'), bg="#ECD3BF", width=20, relief="groove").grid(row=i, column=3, padx=0)
                entry_arrival_hhmm = Entry(self.job_frame, font=('Poppins', 10, 'bold'), justify="center", width=15)
                entry_arrival_hhmm.grid(row=i, column=4, padx=20)
                Label(self.job_frame, text=f"Run Time (hh:mm):", font=('Poppins', 9, 'bold'), bg="#EEC894", width=18, relief="groove").grid(row=i, column=5, padx=0)
                entry_runtime_hhmm = Entry(self.job_frame, font=('Poppins', 10, 'bold'), justify="center", width=15)
                entry_runtime_hhmm.grid(row=i, column=6, padx=20)
                self.job_entries.append((entry_job_size, entry_arrival_hhmm, entry_runtime_hhmm))

            self.compute_button = Button(self.root, text="Show Summary Table and Memory Map", command=self.summarytable, font=('Poppins', 18, 'bold'), width=30, bg="#b8804c", height=1, borderwidth=4, relief="sunken")
            self.compute_button.place(x=260, y=30)
            self.basicWidgetList.append(self.compute_button)

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of jobs.")

    def summarytable(self):
        thread = threading.Thread(target=self._summarytable_task)
        thread.daemon = True
        thread.start()

    def _summarytable_task(self):
        try:
            self.os_size = int(self.entry_os_size.get())
            self.memory_size = int(self.entry_memory_size.get())
            self.jobs = []

            for entry_job_size, entry_arrival, entry_runtime in self.job_entries:
                job_size = int(entry_job_size.get())
                arrival_time = self.hhmm_to_ms(entry_arrival.get())
                runtime = self.hhmm_to_ms(entry_runtime.get())
                self.jobs.append({"Job Number": len(self.jobs) + 1, "Job Size": job_size, "Arrival Time": arrival_time, "Runtime": runtime})

            self.jobs = sorted(self.jobs, key=lambda x: x["Arrival Time"])

            current_time = 0
            for job in self.jobs:
                job["Finish Time"] = max(current_time, job["Arrival Time"]) + job["Runtime"]
                job["Wait Time"] = max(current_time - job["Arrival Time"], 0)
                current_time = job["Finish Time"]

                # Convert times back to hh:mm format
                job["Arrival Time"] = self.ms_to_hhmm(job["Arrival Time"])
                job["Runtime"] = self.ms_to_hhmm(job["Runtime"])
                job["Finish Time"] = self.ms_to_hhmm(job["Finish Time"])
                job["Wait Time"] = self.ms_to_hhmm(job["Wait Time"])

            df = pd.DataFrame(self.jobs)
            self.display_table(df)
            self.create_memory_map()

        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for OS size, Memory size, and job details.")

    def display_table(self, df):
        self.clearWidgets()
        self.basicWidgetList = []

        self.sumtablelabel = Label(self.root, text="Summary Table", font=('Poppins', 18, 'bold'), bg="#ecd3bf", height=2, width=19, borderwidth=4, relief="raised")
        self.sumtablelabel.place(x=140, y=15)
        self.basicWidgetList.append(self.sumtablelabel)

        self.memmaplabel = Label(self.root, text="Memory Map", font=('Poppins', 18, 'bold'), bg="#ecd3bf", height=2, width=19, borderwidth=4, relief="raised")
        self.memmaplabel.place(x=625, y=15)
        self.basicWidgetList.append(self.memmaplabel)

        # Add headers
        headers = ["Job Number", "Job Size", "Arrival Time", "Runtime", "Finish Time", "Wait Time"]
        for col_num, header in enumerate(headers):
            header_label = Label(self.root, text=header, font=('Poppins', 10, 'bold'), bg="#eec894", width=10, borderwidth=4, relief="raised")
            header_label.grid(row=0, column=col_num, padx=(15, 3), pady=(85, 1))
            self.basicWidgetList.append(header_label)

        # Add rows
        for row_num, row in df.iterrows():
            for col_num, value in enumerate(row):
                cell_label = Label(self.root, text=value, font=('Poppins', 10, 'bold'), bg="#FFFFFF", width=10, borderwidth=4, relief="raised")
                cell_label.grid(row=row_num + 1, column=col_num, padx=(15, 3))
                self.basicWidgetList.append(cell_label)

    def create_memory_map(self):

        self.canvas = Canvas(self.root, width=200, height=495, bg="#f2f2f2",
                             highlightthickness=0)  # Remove white spaces
        self.canvas.place(x=675, y=100)

        self.time_label = Label(self.root, text="Current Time:", font=('Poppins', 18, 'bold'), bg="#ecd3bf")
        self.time_label.place(x=645, y=690)
        self.basicWidgetList.append(self.time_label)

        # Get the time range considering the 10 minutes buffer
        first_arrival_ms = min(self.hhmm_to_ms(job["Arrival Time"]) for job in self.jobs)
        last_finish_ms = max(self.hhmm_to_ms(job["Finish Time"]) for job in self.jobs)
        min_time_ms = first_arrival_ms - 10 * 60 * 1000  # 10 minutes before
        max_time_ms = last_finish_ms + 10 * 60 * 1000  # 10 minutes after

        self.time_slider = Scale(self.root, from_=min_time_ms, to=max_time_ms, orient=HORIZONTAL, length=202,
                                 command=self.update_memory_map, bg="black")
        self.time_slider.place(x=675, y=620)

        self.time_slider_label = Label(self.root, text=self.hhmm_from_ms(min_time_ms), font=('Poppins', 18, 'bold'),
                                       bg="#ecd3bf")
        self.time_slider_label.place(x=830, y=690)
        self.basicWidgetList.append(self.time_slider)

        #self.update_button = Button(self.root, text="Update Memory Map", command=self.update_memory_map,
         #                           font=('Poppins', 14, 'bold'), bg="#b8804c", width=20, height=1, borderwidth=4,
          #                          relief="sunken")
        #self.update_button.place(x=625, y=700)
        #self.basicWidgetList.append(self.update_button)

        self.update_memory_map()


        self.exit_button = Button(root, text="Exit", command=self.mainscreen, font=('Poppins', 20, 'bold'), fg='white', width=15, bg='#4b3621', height=1, borderwidth=2, relief='sunken')
        self.exit_button.place(x=350, y=680)
        self.basicWidgetList.append(self.exit_button)

    def hhmm_from_ms(self, ms):
        total_seconds = ms // 1000
        hours, remainder = divmod(total_seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}"

    def update_memory_map(self, *args):
        try:
            self.canvas.delete("all")
            self.canvas.create_rectangle(0, 0, 200, 500, outline="black")  # Adjust width

            os_height = (self.os_size / self.memory_size) * 500
            self.canvas.create_rectangle(0, 0, 200, os_height, fill="#63c8c4", outline="black")
            self.canvas.create_text(100, os_height / 2, text="OS", fill="black")

            current_time = self.time_slider.get()
            self.time_slider_label.config(text=self.hhmm_from_ms(current_time))

            if current_time >= self.hhmm_to_ms(self.jobs[-1]["Finish Time"]):
                self.canvas.create_rectangle(0, os_height, 200, 500, fill="#f765a3", outline="black")
                wasted_memory = self.memory_size - self.os_size
                self.canvas.create_text(100, (os_height + 500) / 2, text=f"Waste: {wasted_memory}", fill="black")
                return

            for job in self.jobs:
                job_arrival_time_ms = self.hhmm_to_ms(job["Arrival Time"])
                job_finish_time_ms = self.hhmm_to_ms(job["Finish Time"])

                if job_arrival_time_ms <= current_time < job_finish_time_ms:
                    job_height = (job["Job Size"] / self.memory_size) * 500
                    self.canvas.create_rectangle(0, os_height, 200, os_height + job_height, fill="#F0A8A8",
                                                 outline="black")  # Changed color to blue
                    self.canvas.create_text(100, os_height + job_height / 2, text=f"Job {job['Job Number']}",
                                            fill="black")

                    os_height += job_height

                    # Calculate and indicate wasted memory
                    if os_height < 500:
                        wasted_memory = self.memory_size - (self.os_size + job["Job Size"])
                        self.canvas.create_rectangle(0, os_height, 200, 500, fill="#f765a3", outline="black")
                        self.canvas.create_text(100, (os_height + 500) / 2, text=f"Waste: {wasted_memory}",
                                                fill="black")
                    break
            else:
                self.canvas.create_rectangle(0, os_height, 200, 500, fill="#f765a3", outline="black")
                wasted_memory = self.memory_size - self.os_size
                self.canvas.create_text(100, (os_height + 500) / 2, text=f"Waste: {wasted_memory}", fill="black")

        except ValueError:
            messagebox.showerror("Error", "Invalid time entered.")

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

        self.STATIC_header = Label(root, text="Static Partition Input", font=('Poppins', 24, 'bold'), bg="#000000",
                                   fg="white")
        self.STATIC_header.place(x=0, y=0)
        self.basicWidgetList.append(self.STATIC_header)

        self.STATIC_os_sizeLBL = Label(root, text="OS Size", font=('Poppins', 18, 'bold'), bg="#d3a075", height=2,
                                       width=19, borderwidth=4, relief="raised")
        self.STATIC_os_sizeLBL.place(x=90, y=180)
        self.basicWidgetList.append(self.STATIC_os_sizeLBL)

        self.STATIC_entry_os_size = Entry(root, font=('Poppins', 30, 'bold'), justify="center", width=18)
        self.STATIC_entry_os_size.place(x=390, y=180)
        self.basicWidgetList.append(self.STATIC_entry_os_size)

        self.STATIC_memory_sizeLBL = Label(root, text="Memory Size", font=('Poppins', 18, 'bold'), bg="#ecd3bf",
                                           height=2, width=19, borderwidth=4, relief="raised")
        self.STATIC_memory_sizeLBL.place(x=90, y=250)
        self.basicWidgetList.append(self.STATIC_memory_sizeLBL)

        self.STATIC_entry_memory_size = Entry(root, font=('Poppins', 30, 'bold'), justify="center", width=18)
        self.STATIC_entry_memory_size.place(x=390, y=250)
        self.basicWidgetList.append(self.STATIC_entry_memory_size)

        self.STATIC_job_numLBL = Label(root, text="Number of Jobs", font=('Poppins', 18, 'bold'), bg="#eec894",
                                       height=2, width=19, borderwidth=4, relief="raised")
        self.STATIC_job_numLBL.place(x=90, y=320)
        self.basicWidgetList.append(self.STATIC_job_numLBL)

        self.STATIC_entry_job_num = Entry(root, font=('Poppins', 30, 'bold'), justify="center", width=18)
        self.STATIC_entry_job_num.place(x=390, y=320)
        self.basicWidgetList.append(self.STATIC_entry_job_num)

        self.STATIC_set_jobs_button = Button(root, text="Set Jobs", command=self.STATIC_show_partition_input,
                                             font=('Poppins', 18, 'bold'), width=20, bg="#b8804c", height=2,
                                             borderwidth=4, relief="sunken")
        self.STATIC_set_jobs_button.place(x=330, y=470)
        self.basicWidgetList.append(self.STATIC_set_jobs_button)

        self.back_button = Button(root, text="Back", command=self.mainscreen, font=('Poppins', 18, 'bold'), fg='gray',
                                  width=20, bg='#4b3621', height=2, borderwidth=4, relief='sunken')
        self.back_button.place(x=330, y=560)
        self.basicWidgetList.append(self.back_button)

    def STATIC_show_partition_input(self):
        self.STATIC_set_jobs_button.place_forget()

        self.STATIC_partition_sizeLBL = Label(root, text="Partition Sizes (comma-separated)",
                                              font=('Poppins', 18, 'bold'), bg="#b8804c", height=2, width=25,
                                              borderwidth=4, relief="raised")
        self.STATIC_partition_sizeLBL.place(x=90, y=390)
        self.basicWidgetList.append(self.STATIC_partition_sizeLBL)

        self.STATIC_entry_partition_sizes = Entry(root, font=('Poppins', 30, 'bold'), justify="center", width=14)
        self.STATIC_entry_partition_sizes.place(x=480, y=390)
        self.basicWidgetList.append(self.STATIC_entry_partition_sizes)

        self.STATIC_submit_button = Button(root, text="Submit", command=self.STATIC_create_job_entries,
                                           font=('Poppins', 18, 'bold'), width=20, bg="#b8804c", height=2,
                                           borderwidth=4, relief="sunken")
        self.STATIC_submit_button.place(x=330, y=470)
        self.basicWidgetList.append(self.STATIC_submit_button)

    def static_hide_initial_inputs(self):
        self.STATIC_os_sizeLBL.place_forget()
        self.STATIC_entry_os_size.place_forget()
        self.STATIC_memory_sizeLBL.place_forget()
        self.STATIC_entry_memory_size.place_forget()
        self.STATIC_job_numLBL.place_forget()
        self.STATIC_entry_job_num.place_forget()
        self.STATIC_set_jobs_button.place_forget()
        self.back_button.place_forget()

    def STATIC_create_job_entries(self):
        self.static_hide_initial_inputs()
        self.static_hide_partition_inputs()

        try:
            self.STATIC_num_jobs = int(self.STATIC_entry_job_num.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number of jobs.")
            return

        initial_y = 90
        self.STATIC_job_entries = []
        self.STATIC_start_button = Button(root, text="Start Computing", command=self.STATIC_get_main_input1,
                                          font=('Poppins', 17, 'bold'), width=20, bg="#b8804c", height=2, borderwidth=4,
                                          relief="sunken")
        self.STATIC_start_button.place(x=550, y=initial_y)
        self.basicWidgetList.append(self.STATIC_start_button)

        self.back_buttonSTATIC = Button(root, text="Back", command=self.staticmainInput1_window,
                                        font=('Poppins', 17, 'bold'), fg='gray', width=20, bg='#4b3621', height=2,
                                        borderwidth=4, relief='sunken')
        self.back_buttonSTATIC.place(x=150, y=initial_y)
        self.basicWidgetList.append(self.back_buttonSTATIC)

        for i in range(self.STATIC_num_jobs):
            y_offset = initial_y + 70 + (i * 40)

            STATIC_job_frame = Frame(root, bg="black")
            STATIC_job_frame.place(x=50, y=y_offset)
            self.basicWidgetList.append(STATIC_job_frame)

            STATIC_job_size_label = Label(STATIC_job_frame, text=f"Job {i + 1} Size", font=('Poppins', 14, 'bold'),
                                          bg="#ecd3bf", width=12, borderwidth=4, relief="raised")
            STATIC_job_size_label.grid(row=0, column=0, padx=5, pady=1)
            STATIC_job_size_entry = Entry(STATIC_job_frame, font=('Poppins', 14, 'bold'), justify="center", width=10)
            STATIC_job_size_entry.grid(row=0, column=1, padx=5, pady=1)

            STATIC_job_arrival_label = Label(STATIC_job_frame, text=f"Job {i + 1} Arrival (hh:mm)",
                                             font=('Poppins', 14, 'bold'), bg="#ecd3bf", width=16, borderwidth=4,
                                             relief="raised")
            STATIC_job_arrival_label.grid(row=0, column=2, padx=5, pady=1)
            STATIC_job_arrival_entry = Entry(STATIC_job_frame, font=('Poppins', 14, 'bold'), justify="center", width=10)
            STATIC_job_arrival_entry.grid(row=0, column=3, padx=5, pady=1)

            STATIC_job_run_label = Label(STATIC_job_frame, text=f"Job {i + 1} Run Time (hh:mm)",
                                         font=('Poppins', 14, 'bold'), bg="#ecd3bf", width=16, borderwidth=4,
                                         relief="raised")
            STATIC_job_run_label.grid(row=0, column=4, padx=5, pady=1)
            STATIC_job_run_entry = Entry(STATIC_job_frame, font=('Poppins', 14, 'bold'), justify="center", width=10)
            STATIC_job_run_entry.grid(row=0, column=5, padx=5, pady=1)

            self.STATIC_job_entries.append((STATIC_job_size_entry, STATIC_job_arrival_entry, STATIC_job_run_entry))

    def static_hide_partition_inputs(self):
        self.STATIC_partition_sizeLBL.place_forget()
        self.STATIC_entry_partition_sizes.place_forget()
        self.STATIC_submit_button.place_forget()

    def STATIC_get_main_input1(self):
        try:
            STATIC_os_size = int(self.STATIC_entry_os_size.get())
            STATIC_memory_size = int(self.STATIC_entry_memory_size.get())
            STATIC_partition_sizes = list(map(int, self.STATIC_entry_partition_sizes.get().split(',')))

            STATIC_jobs = []
            for i, STATIC_job_entry in enumerate(self.STATIC_job_entries):
                STATIC_job_size = int(STATIC_job_entry[0].get())
                STATIC_job_arrival = self.convert_time_to_minutes(STATIC_job_entry[1].get())
                STATIC_job_run = self.convert_time_to_minutes(STATIC_job_entry[2].get())
                STATIC_jobs.append((STATIC_job_size, STATIC_job_arrival, STATIC_job_run, i + 1))  # Add job number

            if sum(STATIC_partition_sizes) + STATIC_os_size > STATIC_memory_size:
                raise ValueError("Sum of partition sizes and OS size cannot exceed the total memory size.")

            # Run the main processing task in a separate thread
            thread = threading.Thread(target=self.run_main_processing,
                                      args=(STATIC_os_size, STATIC_memory_size, STATIC_partition_sizes, STATIC_jobs))
            thread.daemon = True
            thread.start()

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def run_main_processing(self, STATIC_os_size, STATIC_memory_size, STATIC_partition_sizes, STATIC_jobs):
        mainProcessingUI = processingUI1(STATIC_os_size, STATIC_memory_size, STATIC_partition_sizes, STATIC_jobs)
        mainProcessingUI.mainProcesss1()
        self.display_static_table(mainProcessingUI)

    def convert_time_to_minutes(self, time_str):
        hh, mm = map(int, time_str.split(':'))
        return hh * 60 + mm

    def display_static_table(self, mainProcess1):
        self.clearWidgets()
        self.basicWidgetList = []

        self.partition_table = Frame(root, bg="black")
        self.partition_table.pack(padx=20, pady=20)

        self.partition_label = Label(self.partition_table, text="Static Partition Information",
                                     font=('Poppins', 18, 'bold'), bg="#b8804c")
        self.partition_label.grid(row=0, columnspan=4, pady=30)

        self.headers = ["Partition Number", "Partition Size", "Status", "Job"]
        for col_num, header in enumerate(self.headers):
            header_label = Label(self.partition_table, text=header, font=('Poppins', 18, 'bold'), bg="#eec894",
                                 width=15, borderwidth=4, relief="raised")
            header_label.grid(row=1, column=col_num, padx=5, pady=5)

        self.display_partition_info(mainProcess1, 0)

        self.nav_frame = Frame(root)
        self.nav_frame.pack(pady=10)

        self.prev_button = Button(self.nav_frame, text="Previous",
                                  command=lambda: self.navigate_partitions(mainProcess1, -1),
                                  font=('Poppins', 10, 'bold'))
        self.prev_button.grid(row=0, column=0, padx=10)

        self.timestamp_label = Label(self.nav_frame, text=f"Timestamp: 0", font=('Poppins', 10, 'bold'))
        self.timestamp_label.grid(row=0, column=1, padx=10)

        self.next_button = Button(self.nav_frame, text="Next",
                                  command=lambda: self.navigate_partitions(mainProcess1, 1),
                                  font=('Poppins', 10, 'bold'))
        self.next_button.grid(row=0, column=2, padx=10)

        self.current_timestamp = 0
        self.max_timestamp = len(mainProcess1.partition_history) - 1

    def display_partition_info(self, mainProcess1, timestamp):
        for widget in self.partition_table.grid_slaves():
            if int(widget.grid_info()["row"]) > 1:
                widget.grid_forget()

        partition_info = mainProcess1.partition_history[timestamp]['partitions']
        for row_num, (partition, info) in enumerate(partition_info.items(), start=2):
            partition_number_label = Label(self.partition_table, text=partition, font=('Poppins', 10, 'bold'),
                                           bg="#FFFFFF", width=15, borderwidth=4, relief="raised")
            partition_number_label.grid(row=row_num, column=0, padx=5, pady=5)
            partition_size_label = Label(self.partition_table, text=info["size"], font=('Poppins', 10, 'bold'),
                                         bg="#FFFFFF", width=15, borderwidth=4, relief="raised")
            partition_size_label.grid(row=row_num, column=1, padx=5, pady=5)
            partition_status_label = Label(self.partition_table, text=info["status"], font=('Poppins', 10, 'bold'),
                                           bg="#FFFFFF", width=15, borderwidth=4, relief="raised")
            partition_status_label.grid(row=row_num, column=2, padx=5, pady=5)
            job_number = info["job"]["Job Number"] if info["job"] != 'None' else 'None'
            partition_job_label = Label(self.partition_table, text=job_number, font=('Poppins', 10, 'bold'),
                                        bg="#FFFFFF", width=15, borderwidth=4, relief="raised")
            partition_job_label.grid(row=row_num, column=3, padx=5, pady=5)

    def navigate_partitions(self, mainProcess1, direction):
        new_timestamp = self.current_timestamp + direction
        if 0 <= new_timestamp <= self.max_timestamp:
            self.current_timestamp = new_timestamp
            self.timestamp_label.config(
                text=f"Timestamp: {mainProcess1.partition_history[self.current_timestamp]['time']}")
            self.display_partition_info(mainProcess1, self.current_timestamp)


class processingUI1:
    def __init__(self, STATIC_os_size, STATIC_memory_size, STATIC_partition_sizes, STATIC_jobs):
        self.STATIC_os_size = STATIC_os_size
        self.STATIC_memory_size = STATIC_memory_size
        self.STATIC_partition_sizes = STATIC_partition_sizes
        self.STATIC_jobs = STATIC_jobs
        self.STATIC_partition_status = ['Free'] * len(STATIC_partition_sizes)
        self.STATIC_job_allocations = {}
        self.partition_history = []

    def STATIC_display_partition_status(self, time):
        formatted_time = self.format_time(time)
        partition_info = {}
        for i, STATIC_size in enumerate(self.STATIC_partition_sizes):
            STATIC_status = self.STATIC_partition_status[i]
            job_info = self.STATIC_job_allocations.get(i, 'None')
            partition_info[f"Partition {i + 1}"] = {
                "size": STATIC_size,
                "status": STATIC_status,
                "job": job_info
            }
        self.partition_history.append({'time': formatted_time, 'partitions': partition_info})

    def STATIC_allocate_job_to_partition(self, STATIC_job, STATIC_partition_index, current_time):
        self.STATIC_partition_status[STATIC_partition_index] = 'Occupied'
        end_time = current_time + STATIC_job[2]
        self.STATIC_job_allocations[STATIC_partition_index] = {
            "Job Number": STATIC_job[3],
            "end_time": end_time
        }
        self.STATIC_display_partition_status(current_time)  # Job start time

    def STATIC_deallocate_job_from_partition(self, STATIC_partition_index, time):
        self.STATIC_partition_status[STATIC_partition_index] = 'Free'
        del self.STATIC_job_allocations[STATIC_partition_index]
        self.STATIC_display_partition_status(time)

    def format_time(self, minutes):
        hours = minutes // 60
        minutes = minutes % 60
        return f'{hours:02}:{minutes:02}'

    def mainProcesss1(self):
        STATIC_jobs_sorted = sorted(self.STATIC_jobs, key=lambda x: x[1])
        time = 0

        first_job_arrival = STATIC_jobs_sorted[0][1]
        last_job_finish = max(STATIC_jobs_sorted, key=lambda x: x[1] + x[2])[1] + \
                          max(STATIC_jobs_sorted, key=lambda x: x[1] + x[2])[2]

        start_time = first_job_arrival - 5
        end_time = last_job_finish + 5

        time = start_time

        active_jobs = []

        while time <= end_time:
            for job in active_jobs[:]:
                if time >= job["end_time"]:
                    self.STATIC_deallocate_job_from_partition(job["partition_index"], time)
                    active_jobs.remove(job)

            if STATIC_jobs_sorted and time >= STATIC_jobs_sorted[0][1]:
                STATIC_job = STATIC_jobs_sorted.pop(0)
                STATIC_job_size, STATIC_job_arrival, STATIC_job_run, job_number = STATIC_job

                allocated = False
                while not allocated:
                    for i, STATIC_partition_size in enumerate(self.STATIC_partition_sizes):
                        if self.STATIC_partition_status[i] == 'Free' and STATIC_job_size <= STATIC_partition_size:
                            self.STATIC_allocate_job_to_partition(STATIC_job, i, time)
                            self.STATIC_display_partition_status(time)
                            active_jobs.append({
                                "partition_index": i,
                                "end_time": time + STATIC_job_run
                            })
                            allocated = True
                            break
                    if not allocated:
                        next_event_time = min([job["end_time"] for job in active_jobs] + [
                            STATIC_jobs_sorted[0][1] if STATIC_jobs_sorted else float('inf')])
                        time = max(time + 1, next_event_time)
                        break
            else:
                if active_jobs:
                    next_event_time = min([job["end_time"] for job in active_jobs])
                    time = max(time + 1, next_event_time)
                else:
                    time += 1

        self.STATIC_display_partition_status(time)


if __name__ == "__main__":
    BATMAS = mainUI(root)
    BATMAS.mainscreen()
    root.mainloop()
