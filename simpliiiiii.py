import tkinter as tk
from tkinter import messagebox, Label, Entry, Button, Frame, Canvas
import pandas as pd


class mainUI:
    def __init__(self):
        self.basicWidgetList = []
        self.STATIC_job_entries = []

    def mainscreen(self):
        global root
        root = tk.Tk()
        root.title("Memory Management Simulation")
        root.geometry("1000x600")
        root.configure(bg="#ecd3bf")

        self.os_size_label = Label(root, text="OS Size:", font=('Poppins', 10, 'bold'), bg="#ecd3bf")
        self.os_size_label.place(x=50, y=50)
        self.os_size_entry = Entry(root)
        self.os_size_entry.place(x=150, y=50)

        self.memory_size_label = Label(root, text="Memory Size:", font=('Poppins', 10, 'bold'), bg="#ecd3bf")
        self.memory_size_label.place(x=50, y=100)
        self.memory_size_entry = Entry(root)
        self.memory_size_entry.place(x=150, y=100)

        self.partition_sizes_label = Label(root, text="Partition Sizes (comma separated):",
                                           font=('Poppins', 10, 'bold'), bg="#ecd3bf")
        self.partition_sizes_label.place(x=50, y=150)
        self.partition_sizes_entry = Entry(root)
        self.partition_sizes_entry.place(x=280, y=150)

        self.num_jobs_label = Label(root, text="Number of Jobs:", font=('Poppins', 10, 'bold'), bg="#ecd3bf")
        self.num_jobs_label.place(x=50, y=200)
        self.num_jobs_entry = Entry(root)
        self.num_jobs_entry.place(x=200, y=200)

        self.create_jobs_button = Button(root, text="Create Job Entries", command=self.STATIC_create_job_entries)
        self.create_jobs_button.place(x=400, y=200)

        self.back_button = Button(root, text="Back", command=self.go_back)
        self.back_button.place(x=900, y=20)

    def clearWidgets(self):
        for widget in self.basicWidgetList:
            widget.destroy()
        self.basicWidgetList = []

    def STATIC_create_job_entries(self):
        try:
            num_jobs = int(self.num_jobs_entry.get())
            self.STATIC_job_entries = []

            self.jobs_label = Label(root, text="Job Size, Arrival Time, Runtime", font=('Poppins', 10, 'bold'),
                                    bg="#ecd3bf")
            self.jobs_label.place(x=50, y=250)
            self.basicWidgetList.append(self.jobs_label)

            for i in range(num_jobs):
                job_size_entry = Entry(root)
                job_size_entry.place(x=50, y=280 + i * 30)
                self.basicWidgetList.append(job_size_entry)

                arrival_time_entry = Entry(root)
                arrival_time_entry.place(x=200, y=280 + i * 30)
                self.basicWidgetList.append(arrival_time_entry)

                runtime_entry = Entry(root)
                runtime_entry.place(x=350, y=280 + i * 30)
                self.basicWidgetList.append(runtime_entry)

                self.STATIC_job_entries.append((job_size_entry, arrival_time_entry, runtime_entry))

            self.process_button = Button(root, text="Process", command=self.process_static)
            self.process_button.place(x=500, y=280 + num_jobs * 30)
            self.basicWidgetList.append(self.process_button)

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for the number of jobs.")

    def process_static(self):
        try:
            STATIC_os_size = int(self.os_size_entry.get())
            STATIC_memory_size = int(self.memory_size_entry.get())
            STATIC_partition_sizes = list(map(int, self.partition_sizes_entry.get().split(',')))

            if sum(STATIC_partition_sizes) > STATIC_memory_size:
                messagebox.showerror("Input Error", "Total partition sizes exceed memory size.")
                return

            STATIC_jobs = []
            for entry_job_size, entry_arrival, entry_runtime in self.STATIC_job_entries:
                job_size = int(entry_job_size.get())
                arrival_time = entry_arrival.get()
                runtime = entry_runtime.get()
                STATIC_jobs.append(
                    {"Job Number": len(STATIC_jobs) + 1, "Job Size": job_size, "Arrival Time": arrival_time,
                     "Runtime": runtime})

            self.STATIC_summary_table(STATIC_os_size, STATIC_memory_size, STATIC_partition_sizes, STATIC_jobs)

        except ValueError:
            messagebox.showerror("Input Error",
                                 "Please enter valid numbers for OS size, memory size, partition sizes, and job details.")

    def STATIC_summary_table(self, os_size, memory_size, partition_sizes, jobs):
        try:
            self.clearWidgets()

            memory_map = ["OS" for _ in range(os_size)] + ["Free" for _ in range(memory_size - os_size)]

            job_memory = []
            for partition in partition_sizes:
                job_memory.append({"Partition Size": partition, "Job": None})

            def allocate_memory(job):
                for partition in job_memory:
                    if partition["Job"] is None and partition["Partition Size"] >= job["Job Size"]:
                        partition["Job"] = job
                        return True
                return False

            for job in jobs:
                if not allocate_memory(job):
                    job["Status"] = "Not Allocated"
                else:
                    job["Status"] = "Allocated"

            df = pd.DataFrame(jobs)
            self.display_static_table(df)

            for partition in job_memory:
                start_index = memory_map.index("Free")
                end_index = start_index + partition["Partition Size"]
                for i in range(start_index, end_index):
                    if partition["Job"]:
                        memory_map[i] = f"Job {partition['Job']['Job Number']}"
                    else:
                        memory_map[i] = "Free"

            self.display_memory_map(memory_map)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def display_static_table(self, df):
        self.clearWidgets()
        self.basicWidgetList = []

        self.sumtablelabel = Label(root, text="Summary Table", font=('Poppins', 18, 'bold'), bg="#ecd3bf", height=2,
                                   width=19, borderwidth=4, relief="raised")
        self.sumtablelabel.place(x=140, y=15)
        self.basicWidgetList.append(self.sumtablelabel)

        self.memmaplabel = Label(root, text="Memory Map", font=('Poppins', 18, 'bold'), bg="#ecd3bf", height=2,
                                 width=19, borderwidth=4, relief="raised")
        self.memmaplabel.place(x=600, y=15)
        self.basicWidgetList.append(self.memmaplabel)

        headers = ["Job Number", "Job Size", "Arrival Time", "Runtime", "Status"]
        for col_num, header in enumerate(headers):
            header_label = Label(root, text=header, font=('Poppins', 10, 'bold'), bg="#eec894", width=10, borderwidth=4,
                                 relief="raised")
            header_label.grid(row=0, column=col_num, padx=(7, 3), pady=(85, 1))
            self.basicWidgetList.append(header_label)

        for row_num, row in df.iterrows():
            for col_num, value in enumerate(row):
                cell_label = Label(root, text=value, font=('Poppins', 10, 'bold'), bg="#FFFFFF", width=10,
                                   borderwidth=4, relief="raised")
                cell_label.grid(row=row_num + 1, column=col_num, padx=(7, 3))
                self.basicWidgetList.append(cell_label)

    def display_memory_map(self, memory_map):
        self.memory_map_frame = Frame(root, bg='black')
        self.memory_map_frame.place(x=650, y=90)
        self.basicWidgetList.append(self.memory_map_frame)

        self.canvas = Canvas(self.memory_map_frame, width=400, height=200, bg='white')
        self.canvas.pack()
        self.basicWidgetList.append(self.canvas)

        y_offset = 10
        for index, block in enumerate(memory_map):
            self.canvas.create_rectangle(10, y_offset, 390, y_offset + 20,
                                         fill='gray' if block == "OS" else 'green' if block == "Free" else 'blue')
            self.canvas.create_text(200, y_offset + 10, text=block, fill='white')
            y_offset += 20

    def go_back(self):
        self.back_button.place_forget()
        self.clearWidgets()


if __name__ == "__main__":
    ui = mainUI()
    ui.mainscreen()
    root.mainloop()
