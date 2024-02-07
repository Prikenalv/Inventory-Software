from customtkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
import sqlite3
from tkinter.filedialog import askopenfilename, asksaveasfilename
import datetime as dt
import os
from fpdf import FPDF

def library_log_content():
    global db_file, library_log_content_mainframe, library_log_content_frame3_loglist_tab_frame_treeview,  library_log_content_information_frame_id_entry, library_log_content_information_frame_control_id_entry, library_log_content_information_frame_name_entry, library_log_content_information_frame_position_entry, library_log_content_information_frame_department_entry, library_log_content_information_frame_timein_entry, library_log_content_information_frame_timeout_entry, library_log_content_information_frame_overtime_entry

    #Mainframe
    library_log_content_mainframe = CTkFrame(master=root, bg_color="white", fg_color="white")
    library_log_content_mainframe.pack(fill=BOTH, expand=True)

    #Frame 1
    ##Back Button
    library_log_content_frame1 = CTkFrame(master=library_log_content_mainframe, bg_color="lightgreen", fg_color="lightgreen", corner_radius=0 ,height=35)
    library_log_content_frame1.pack(fill=X, side=TOP, anchor=N, pady=(0,5))

    library_log_content_frame1_header = CTkLabel(master=library_log_content_frame1, text="Library Attendance Record", text_color="black", font=("Times New Roman", 35, 'bold'), bg_color="transparent", fg_color="transparent")
    library_log_content_frame1_header.pack(side=TOP, anchor=N, padx=5, pady=5)

    #Frame 2
    library_log_content_frame2 = CTkFrame(master=library_log_content_mainframe, bg_color="lightgreen", fg_color="lightgreen", border_color="lightgreen", border_width=1)
    library_log_content_frame2.pack(fill=Y, side=LEFT, anchor=W, padx=(0,2.5))

    ##Header Frame
    library_log_content_frame2_header_frame = CTkFrame(master=library_log_content_frame2, bg_color="lightgreen", fg_color="lightgreen", height=35)
    library_log_content_frame2_header_frame.pack(fill=X, side=TOP, anchor=N)

    library_log_content_frame2_header_frame_content = CTkLabel(master=library_log_content_frame2_header_frame, text="Personal Details", font=("Times New Roman", 40), text_color="black" ,bg_color="lightgreen", fg_color="lightgreen")
    library_log_content_frame2_header_frame_content.pack(padx=10, pady=5)

    ##Information Frame
    library_log_content_information_frame = CTkFrame(master=library_log_content_frame2, bg_color="lightgreen", fg_color="lightgreen")
    library_log_content_information_frame.pack(fill=X, side=TOP, anchor=N)

    library_log_content_information_frame_id_label = CTkLabel(master=library_log_content_information_frame, text="Personal ID:", font=content_label_font, text_color="black", bg_color="lightgreen", fg_color="lightgreen")
    library_log_content_information_frame_id_label.grid(row=0,column=0, padx=(10,5), pady=5, sticky=W)

    library_log_content_information_frame_id_entry = CTkEntry(master=library_log_content_information_frame, width=250, font=content_entry_font, text_color="black", bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5)
    library_log_content_information_frame_id_entry.grid(row=0,column=1, padx=(5,10), pady=5)

    library_log_content_information_frame_control_id_label = CTkLabel(master=library_log_content_information_frame, text="Control ID:", font=content_label_font, text_color="black", bg_color="lightgreen", fg_color="lightgreen")
    library_log_content_information_frame_control_id_label.grid(row=1,column=0, padx=(10,5), pady=5, sticky=W)

    library_log_content_information_frame_control_id_entry = CTkEntry(master=library_log_content_information_frame, width=250, font=content_entry_font, text_color="black", bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5)
    library_log_content_information_frame_control_id_entry.grid(row=1,column=1, padx=(5,10), pady=5)

    library_log_content_information_frame_name_label = CTkLabel(master=library_log_content_information_frame, text="Name:", font=content_label_font, text_color="black", bg_color="lightgreen", fg_color="lightgreen")
    library_log_content_information_frame_name_label.grid(row=2,column=0, padx=(10,5), pady=5, sticky=W)

    library_log_content_information_frame_name_entry = CTkEntry(master=library_log_content_information_frame, width=250, font=content_entry_font, text_color="black", bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5)
    library_log_content_information_frame_name_entry.grid(row=2,column=1, padx=(5,10), pady=5)

    library_log_content_information_frame_position_label = CTkLabel(master=library_log_content_information_frame, text="Position:", font=content_label_font, text_color="black", bg_color="lightgreen", fg_color="lightgreen")
    library_log_content_information_frame_position_label.grid(row=3,column=0, padx=(10,5), pady=5, sticky=W)

    library_log_content_information_frame_position_entry = CTkEntry(master=library_log_content_information_frame, width=250, font=content_entry_font, text_color="black", bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5)
    library_log_content_information_frame_position_entry.grid(row=3,column=1, padx=(5,10), pady=5)

    library_log_content_information_frame_department_label = CTkLabel(master=library_log_content_information_frame, text="Department:", font=content_label_font, text_color="black", bg_color="lightgreen", fg_color="lightgreen")
    library_log_content_information_frame_department_label.grid(row=4,column=0, padx=(10,5), pady=5, sticky=W)

    library_log_content_information_frame_department_entry = CTkEntry(master=library_log_content_information_frame, width=250, font=content_entry_font, text_color="black", bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5)
    library_log_content_information_frame_department_entry.grid(row=4,column=1, padx=(5,10), pady=5)

    library_log_content_information_frame_timein_label = CTkLabel(master=library_log_content_information_frame, text="Time in:", font=content_label_font, text_color="black", bg_color="lightgreen", fg_color="lightgreen")
    library_log_content_information_frame_timein_label.grid(row=5,column=0, padx=(10,5), pady=5, sticky=W)

    library_log_content_information_frame_timein_entry = CTkEntry(master=library_log_content_information_frame, width=250, font=content_entry_font, placeholder_text="Leave this Blank", placeholder_text_color="#8A8A8A", text_color="black", bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5)
    library_log_content_information_frame_timein_entry.grid(row=5,column=1, padx=(5,10), pady=5)

    library_log_content_information_frame_timeout_label = CTkLabel(master=library_log_content_information_frame, text="Time out:", font=content_label_font, text_color="black", bg_color="lightgreen", fg_color="lightgreen")
    library_log_content_information_frame_timeout_label.grid(row=6,column=0, padx=(10,5), pady=5, sticky=W)

    library_log_content_information_frame_timeout_entry = CTkEntry(master=library_log_content_information_frame, width=250, font=content_entry_font, text_color="black", placeholder_text="Leave this Blank", placeholder_text_color="#8A8A8A", bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5)
    library_log_content_information_frame_timeout_entry.grid(row=6,column=1, padx=(5,10), pady=5)

    library_log_content_information_frame_overtime_label = CTkLabel(master=library_log_content_information_frame, text="Overtime:", font=content_label_font, text_color="black", bg_color="lightgreen", fg_color="lightgreen")
    library_log_content_information_frame_overtime_label.grid(row=7, column=0, padx=(10,5), pady=5, sticky=W)

    library_log_content_information_frame_overtime_entry = CTkEntry(master=library_log_content_information_frame, width=250, font=content_entry_font, text_color="black", placeholder_text="Leave this Blank", placeholder_text_color="#8A8A8A", bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5)
    library_log_content_information_frame_overtime_entry.grid(row=7,column=1, padx=(5,10), pady=5)

    ##Buttons Frame
    library_log_content_button_frame = CTkFrame(master=library_log_content_frame2, bg_color="lightgreen", fg_color="lightgreen")
    library_log_content_button_frame.pack(fill=X, side=TOP, anchor=N, pady=(20,0))

    library_log_content_content_search_button_icon = Image.open("library_log_search-icon.png")

    library_log_content_button_frame_search_button = CTkButton(master=library_log_content_button_frame, command=library_log_content_search_by_id, image=CTkImage(dark_image=library_log_content_content_search_button_icon, size=(15,15)), text="Search", text_color="black", font=content_button_font, bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5, hover_color="#52D452", width=110, height=30)
    library_log_content_button_frame_search_button.grid(row=0, column=0, padx=(10,5), pady=5, sticky=W)

    library_log_content_content_timein_button_icon = Image.open("library_log_time-in-icon.png")

    library_log_content_button_frame_timein_button = CTkButton(master=library_log_content_button_frame, command=library_log_content_timein, image=CTkImage(dark_image=library_log_content_content_timein_button_icon, size=(15,15)), text="Time in", text_color="black", font=content_button_font, bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5, hover_color="#52D452", width=110, height=30)
    library_log_content_button_frame_timein_button.grid(row=0, column=1, padx=(10,5), pady=5, sticky=W)

    library_log_content_content_timeout_button_icon = Image.open("library_log_time-out-icon.png")

    library_log_content_button_frame_timeout_button = CTkButton(master=library_log_content_button_frame, command=library_log_content_timeout, image=CTkImage(dark_image=library_log_content_content_timeout_button_icon, size=(15,15)), text="Time out", text_color="black", font=content_button_font, bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5, hover_color="#52D452", width=110, height=30)
    library_log_content_button_frame_timeout_button.grid(row=0, column=2, padx=(10,5), pady=5, sticky=W)

    library_log_content_content_deselect_button_icon = Image.open("library_log_deselect-icon.png")

    library_log_content_button_frame_deselect_button = CTkButton(master=library_log_content_button_frame, command=library_log_content_deselect_data, image=CTkImage(dark_image=library_log_content_content_deselect_button_icon, size=(15,15)), text="De-Select", text_color="black", font=content_button_font, bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5, hover_color="#52D452", width=110, height=30)
    library_log_content_button_frame_deselect_button.grid(row=1, column=0, columnspan=2, padx=(10,5), pady=5, sticky=W)

    library_log_content_content_delete_button_icon = Image.open("library_log_delete-icon.png")

    library_log_content_button_frame_delete_button = CTkButton(master=library_log_content_button_frame, command=library_log_content_delete_data, image=CTkImage(dark_image=library_log_content_content_delete_button_icon, size=(15,15)), text="Delete", text_color="black", font=content_button_font, bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5, hover_color="#52D452", width=110, height=30)
    library_log_content_button_frame_delete_button.grid(row=1, column=1, columnspan=2, padx=(10,5), pady=5, sticky=W)

    library_log_content_content_endlog_button_icon = Image.open("library_log_end-log-icon.png")

    library_log_content_button_frame_endlog_button = CTkButton(master=library_log_content_button_frame, command=library_log_content_delete , image=CTkImage(dark_image=library_log_content_content_endlog_button_icon, size=(15,15)), text="End Log", text_color="black", font=content_button_font, bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5, hover_color="#52D452", width=110, height=30)
    library_log_content_button_frame_endlog_button.grid(row=1, column=2, padx=(10,5), pady=5, sticky=W)

    library_log_content_content_print_button_icon = Image.open("library_log_print-log-icon.png")

    library_log_content_button_frame_print_button = CTkButton(master=library_log_content_button_frame, command=library_log_content_print, image=CTkImage(dark_image=library_log_content_content_print_button_icon, size=(15,15)), text="Print", text_color="black", font=content_button_font, bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5, hover_color="#52D452", width=110, height=30)
    library_log_content_button_frame_print_button.grid(row=2, column=0, padx=(10,5), pady=5, sticky=W)

    #Frame 3
    library_log_content_frame3 = CTkFrame(master=library_log_content_mainframe, bg_color="lightgreen", fg_color="lightgreen")
    library_log_content_frame3.pack(fill=BOTH, expand=True, side=RIGHT,anchor=E, padx=(2.5,0))

    ##Treeview Style 
    style = ttk.Style(root)
    style.theme_use('classic')
    style.configure("Treeview.Heading", background='lightgreen', foreground='black', font=("Comic sans", 10))  # Header
    style.configure("Treeview", font=("Comic sans", 8)) #Body

    library_log_content_frame3_loglist_tab_frame_treeview = ttk.Treeview(library_log_content_frame3, columns=('id', 'controlid','name', 'position', 'department', 'timein', 'timeout', 'overtime'), show='headings', style='Treeview')
    library_log_content_frame3_loglist_tab_frame_treeview.pack(expand=True, fill=BOTH)

    library_log_content_frame3_loglist_tab_frame_treeview.heading('id', text='Personal ID')
    library_log_content_frame3_loglist_tab_frame_treeview.heading('controlid', text='Control ID')
    library_log_content_frame3_loglist_tab_frame_treeview.heading('name', text='Name')
    library_log_content_frame3_loglist_tab_frame_treeview.heading('position', text='Position')
    library_log_content_frame3_loglist_tab_frame_treeview.heading('department', text='Department')
    library_log_content_frame3_loglist_tab_frame_treeview.heading('timein', text='Time in')
    library_log_content_frame3_loglist_tab_frame_treeview.heading('timeout', text='Time out')
    library_log_content_frame3_loglist_tab_frame_treeview.heading('overtime', text='Overtime')

    library_log_content_frame3_loglist_tab_frame_treeview.column('id', width=60)
    library_log_content_frame3_loglist_tab_frame_treeview.column('controlid', width=60)
    library_log_content_frame3_loglist_tab_frame_treeview.column('name', width=200)
    library_log_content_frame3_loglist_tab_frame_treeview.column('position', width=50)
    library_log_content_frame3_loglist_tab_frame_treeview.column('department', width=50)
    library_log_content_frame3_loglist_tab_frame_treeview.column('timein', width=100)
    library_log_content_frame3_loglist_tab_frame_treeview.column('timeout', width=100)
    library_log_content_frame3_loglist_tab_frame_treeview.column('overtime', width=70)

    library_log_content_display_loglist_data()
    library_log_content_frame3_loglist_tab_frame_treeview.bind('<ButtonRelease>', library_log_select_data)

def library_log_content_display_loglist_data():
    global library_log_content_frame3_loglist_tab_frame_treeview, db_file

    connlog = sqlite3.connect(db_file)  # Create a new connection to the selected file
    cursorlog = connlog.cursor()
    cursorlog.execute("SELECT * FROM LibraryLog")
    rows = cursorlog.fetchall()
    
    # Clear existing data
    library_log_content_frame3_loglist_tab_frame_treeview.delete(*library_log_content_frame3_loglist_tab_frame_treeview.get_children())

    # Insert fetched rows at the bottom by setting index='end'
    for row in rows:
        library_log_content_frame3_loglist_tab_frame_treeview.insert('', END, values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

    connlog.close()

def create_new_library_log():
    global db_file

    print("New Log Button is Clicked")   
    
    db_file = asksaveasfilename(defaultextension=".db", filetypes=[("SQLite Database", "*.db")])
    if db_file:
        connlog = sqlite3.connect(db_file)  # Create a new connection to the selected file
        
        connlog.execute('''
        CREATE TABLE IF NOT EXISTS "LibraryLog" (
            "masterid"	INTEGER NOT NULL,
            "id"	varchar(255) NOT NULL,
            "controlid"	varchar(255) NOT NULL,
            "name"	varchar(255) NOT NULL,
            "position"	varchar(255) NOT NULL,
            "department"	varchar(255) NOT NULL,
            "timein"	varchar(255) DEFAULT 'TIMESTAMP',
            "timeout"	varchar(255),
            "overtime"	varchar(255) DEFAULT '-----',
            PRIMARY KEY("masterid" AUTOINCREMENT)
            )
        ''')  # Create a new Student table
        mainframe1.pack_forget()
        mainframe2.pack_forget()

        connhistory = sqlite3.connect("SoftwareData.db")
        cursorhistory = connhistory.cursor()

        data_insert_query = '''
        INSERT INTO HistoryLog ("name", "date") VALUES (?, strftime('%m-%d-%Y | %H:%M:%S', 'now', 'localtime'))
        '''

        filename = os.path.basename(db_file)
        data_insert_list = [filename]

        cursorhistory.execute(data_insert_query, data_insert_list)
        connhistory.commit()

        library_log_content()
        print("Database Created and Connected")
        print("File is saved to History Log")

def open_existing_library_log():
    global db_file

    db_file = askopenfilename(filetypes=[("SQLite Database", "*.db")])
    print("Existing Log Button is Clicked") 

    if db_file:
        connlog = sqlite3.connect(db_file)  # Connect to the selected database file
        connlog.execute('''
        CREATE TABLE IF NOT EXISTS "LibraryLog" (
            "masterid"	INTEGER NOT NULL,
            "id"	varchar(255) NOT NULL,
            "controlid"	varchar(255) NOT NULL,
            "name"	varchar(255) NOT NULL,
            "position"	varchar(255) NOT NULL,
            "department"	varchar(255) NOT NULL,
            "timein"	varchar(255) DEFAULT 'TIMESTAMP',
            "timeout"	varchar(255),
            "overtime"	varchar(255) DEFAULT '-----',
            PRIMARY KEY("masterid" AUTOINCREMENT)
            )
        ''')  # Create a new Student table
        mainframe1.pack_forget()
        mainframe2.pack_forget()

        library_log_content()
        print("Database Connected")

def library_log_content_search_by_id():
    global library_log_content_information_frame_id_entry,  library_log_content_information_frame_control_id_entry, library_log_content_information_frame_name_entry, library_log_content_information_frame_position_entry, library_log_content_information_frame_department_entry, library_log_content_information_frame_id_entry_value, library_log_content_information_frame_control_id_entry_value

    print("Search Button has been clicked")

    library_log_content_information_frame_id_entry_value = library_log_content_information_frame_id_entry.get()
    library_log_content_information_frame_control_id_entry_value = library_log_content_information_frame_control_id_entry.get()

    if not (library_log_content_information_frame_id_entry_value.strip() and library_log_content_information_frame_control_id_entry_value.strip()):
        messagebox.showinfo("Missing Information", "Please enter Personal and Control ID")
        return

    connlist = sqlite3.connect('SoftwareData.db')  # Create a new connection to the selected file
    cursorlist = connlist.cursor()
    cursorlist.execute("SELECT * FROM StudentsList WHERE id=? UNION SELECT * FROM ProfessorsList WHERE id=?", (library_log_content_information_frame_id_entry_value, library_log_content_information_frame_id_entry_value))
    combined_result = cursorlist.fetchall()

    if combined_result:
        # Data found in StudentsList and ProfessorsList
        data = combined_result[0]
        library_log_content_information_frame_id_entry.delete(0, END)
        library_log_content_information_frame_id_entry.insert(0, data[0])

        library_log_content_information_frame_name_entry.delete(0,END)
        library_log_content_information_frame_name_entry.insert(0,data[1])

        library_log_content_information_frame_position_entry.delete(0,END)
        library_log_content_information_frame_position_entry.insert(0,data[2])

        library_log_content_information_frame_department_entry.delete(0,END)
        library_log_content_information_frame_department_entry.insert(0,data[3])

    else:
        messagebox.showinfo("Not Found", "Personal ID doesn't exist.")
    connlist.close()

def library_log_content_timein():
    global db_file, library_log_content_frame3_loglist_tab_frame_treeview

    library_log_content_information_frame_id_entry_value = library_log_content_information_frame_id_entry.get()
    library_log_content_information_frame_control_id_entry_value = library_log_content_information_frame_control_id_entry.get()
    library_log_content_information_frame_name_entry_value = library_log_content_information_frame_name_entry.get()
    library_log_content_information_frame_position_entry_value = library_log_content_information_frame_position_entry.get()
    library_log_content_information_frame_department_entry_value = library_log_content_information_frame_department_entry.get()
    library_log_content_information_frame_timein_entry_value = library_log_content_information_frame_timein_entry.get()
    library_log_content_information_frame_timeout_entry_value = library_log_content_information_frame_timeout_entry.get()
    library_log_content_information_frame_overtime_entry_value = library_log_content_information_frame_overtime_entry.get()

    if not (library_log_content_information_frame_id_entry_value.strip() and library_log_content_information_frame_control_id_entry_value.strip() and library_log_content_information_frame_name_entry_value.strip() and library_log_content_information_frame_position_entry_value.strip() and library_log_content_information_frame_department_entry_value.strip()):
        messagebox.showinfo("Missing Information", "Please fill in all Personal Details.")
        return

    if (library_log_content_information_frame_timein_entry_value.strip() and library_log_content_information_frame_timeout_entry_value.strip() and library_log_content_information_frame_overtime_entry_value.strip() == "N/A"):
        messagebox.showinfo("Timed in", "This user is already Timed in.")
        return

    connlog = sqlite3.connect(db_file)
    cursorlog = connlog.cursor()

    data_insert_query_library = '''
        INSERT INTO LibraryLog ("id", "controlid", "name", "position", "department", "timein", "timeout", "overtime") VALUES (?, ?, ?, ?, ?,  strftime('%m-%d-%Y | %H:%M:%S', 'now', 'localtime'), strftime('%m-%d-%Y | %H:%M:%S', 'now', '+5 seconds', 'localtime'), ?)
        '''

    data_insert_list_library  = [library_log_content_information_frame_id_entry_value, library_log_content_information_frame_control_id_entry_value, library_log_content_information_frame_name_entry_value, library_log_content_information_frame_position_entry_value, library_log_content_information_frame_department_entry_value, "N/A"]

    try:
        cursorlog.execute(data_insert_query_library, data_insert_list_library)
        connlog.commit()

        # Clear the entry fields after successful submission
        library_log_content_information_frame_id_entry.delete(0, END)
        library_log_content_information_frame_control_id_entry.delete(0, END)
        library_log_content_information_frame_name_entry.delete(0, END)
        library_log_content_information_frame_position_entry.delete(0, END) 
        library_log_content_information_frame_department_entry.delete(0, END) 
        library_log_content_information_frame_timein_entry.delete(0, END) 
        library_log_content_information_frame_timeout_entry.delete(0, END) 
        library_log_content_information_frame_overtime_entry.delete(0, END) 

    except sqlite3.Error as e:
        connlog.rollback()
        print("Error occurred: insert", e)

    library_log_content_display_loglist_data()
    
    connlog.close()

def library_log_content_timeout():
    global db_file

    library_log_content_information_frame_timein_entry_value = library_log_content_information_frame_timein_entry.get()
    library_log_content_information_frame_timeout_entry_value = library_log_content_information_frame_timeout_entry.get()
    library_log_content_information_frame_timein_entry_value = library_log_content_information_frame_timein_entry.get()
    library_log_content_information_frame_timeout_entry_value = library_log_content_information_frame_timeout_entry.get()
    library_log_content_information_frame_overtime_entry_value = library_log_content_information_frame_overtime_entry.get()

    if not (library_log_content_information_frame_timein_entry_value.strip() and library_log_content_information_frame_timeout_entry_value.strip()):
        messagebox.showinfo("Not Timed in", "This user hadn't timed in yet.")
        return

    if (library_log_content_information_frame_overtime_entry_value.strip() != "N/A"):
        messagebox.showinfo("Timed out", "This user has already timed out")
        return

    try:
        # Fixed timeout
        timeout_value = library_log_content_information_frame_timeout_entry_value
        timeout_format = "%m-%d-%Y | %H:%M:%S"

        timeout_obj = dt.datetime.strptime(timeout_value, timeout_format)

        timeout_remove_date = (timeout_obj - timeout_obj.replace(hour=0, minute=0, second=0)).total_seconds()
        timeout_mins = timeout_remove_date / 60

        # Real Timeout - Get current time
        timelogout_obj = dt.datetime.now()
        timelogout_remove_date = (timelogout_obj - timelogout_obj.replace(hour=0, minute=0, second=0)).total_seconds()
        timelogout_mins = timelogout_remove_date / 60

        result = timelogout_mins - timeout_mins

        connlog = sqlite3.connect(db_file)
        cursorlog = connlog.cursor()
    except ValueError as e:
        messagebox.showinfo("Error", "Invalid Time in and Time out value")
        return

    if timelogout_mins > timeout_mins:
        # Update database with overtime value
        update_query = '''UPDATE LibraryLog SET overtime = ? WHERE timein = ?'''
        overtime_value = str(int(result)) + " min/s"  # Convert result to int and add " mins" after the number
        data_update_list = [overtime_value, library_log_content_information_frame_timein_entry_value]

        try:
            cursorlog.execute(update_query, data_update_list)
            connlog.commit()
            print("Overtime updated in the database:", overtime_value)
        except sqlite3.Error as e:
            connlog.rollback()
            print("Error occurred while updating overtime:", e)
    else:
        # Update database with '----' for overtime value
        update_query = '''UPDATE LibraryLog SET overtime = '----' WHERE timein = ?'''
        data_update_list = [library_log_content_information_frame_timein_entry_value]

        try:
            cursorlog.execute(update_query, data_update_list)
            connlog.commit()
            print("Overtime set to '----' in the database")
        except sqlite3.Error as e:
            connlog.rollback()
            print("Error occurred while setting overtime to '----':", e)

    library_log_content_information_frame_id_entry.delete(0, END)
    library_log_content_information_frame_control_id_entry.delete(0, END)
    library_log_content_information_frame_name_entry.delete(0, END)
    library_log_content_information_frame_position_entry.delete(0, END) 
    library_log_content_information_frame_department_entry.delete(0, END) 
    library_log_content_information_frame_timein_entry.delete(0, END) 
    library_log_content_information_frame_timeout_entry.delete(0, END) 
    library_log_content_information_frame_overtime_entry.delete(0, END) 

    connlog.close()
    library_log_content_display_loglist_data()  # Refresh displayed data

def library_log_select_data(event):
    global library_log_content_frame3_loglist_tab_frame_treeview
    selected_item = library_log_content_frame3_loglist_tab_frame_treeview.focus()
    if selected_item:
        library_log_content_frame3_loglist_tab_frame_treeview.selection_set(selected_item)
        library_log_content_frame3_loglist_tab_frame_treeview_row = library_log_content_frame3_loglist_tab_frame_treeview.item(selected_item)['values']

        library_log_content_information_frame_id_entry.delete(0, END)
        library_log_content_information_frame_id_entry.insert(0,library_log_content_frame3_loglist_tab_frame_treeview_row[0])
        
        library_log_content_information_frame_control_id_entry.delete(0, END)
        library_log_content_information_frame_control_id_entry.insert(0,library_log_content_frame3_loglist_tab_frame_treeview_row[1])

        library_log_content_information_frame_name_entry.delete(0, END)
        library_log_content_information_frame_name_entry.insert(0,library_log_content_frame3_loglist_tab_frame_treeview_row[2])

        library_log_content_information_frame_position_entry.delete(0, END)
        library_log_content_information_frame_position_entry.insert(0,library_log_content_frame3_loglist_tab_frame_treeview_row[3])

        library_log_content_information_frame_department_entry.delete(0, END) 
        library_log_content_information_frame_department_entry.insert(0,library_log_content_frame3_loglist_tab_frame_treeview_row[4])

        library_log_content_information_frame_timein_entry.delete(0, END) 
        library_log_content_information_frame_timein_entry.insert(0,library_log_content_frame3_loglist_tab_frame_treeview_row[5])

        library_log_content_information_frame_timeout_entry.delete(0, END) 
        library_log_content_information_frame_timeout_entry.insert(0,library_log_content_frame3_loglist_tab_frame_treeview_row[6])

        library_log_content_information_frame_overtime_entry.delete(0, END) 
        library_log_content_information_frame_overtime_entry.insert(0,library_log_content_frame3_loglist_tab_frame_treeview_row[7])
    else: 
        pass

def library_log_content_deselect_data(*clicked):
    global library_log_content_frame3_loglist_tab_frame_treeview

    selected_item = library_log_content_frame3_loglist_tab_frame_treeview.focus()
    if selected_item:
        library_log_content_frame3_loglist_tab_frame_treeview.selection_remove(selected_item)

        library_log_content_information_frame_id_entry.delete(0, END)
        library_log_content_information_frame_control_id_entry.delete(0, END)
        library_log_content_information_frame_name_entry.delete(0, END)
        library_log_content_information_frame_position_entry.delete(0, END)
        library_log_content_information_frame_department_entry.delete(0, END) 
        library_log_content_information_frame_timein_entry.delete(0, END) 
        library_log_content_information_frame_timeout_entry.delete(0, END) 
        library_log_content_information_frame_overtime_entry.delete(0, END) 

    print("Personal Details Deelected")

def library_log_content_delete_data():

    delete_timein_value = library_log_content_information_frame_timein_entry.get()

    result = messagebox.askokcancel('Warning', 'Are you sure you want to delete this person\'s log?')

    if result:  # User clicked "OK"
        library_log_content_delete_person(delete_timein_value)
        library_log_content_deselect_data()
        library_log_content_display_loglist_data()
        print("Person's log has been deleted")

def library_log_content_delete_person(timein_value):
    global db_file

    connlog = sqlite3.connect(db_file)  # Create a new connection to the selected file
    cursorlog = connlog.cursor()

    cursorlog.execute('DELETE FROM LibraryLog WHERE timein = ?', (timein_value,))

    connlog.commit()
    connlog.close()

def library_log_content_delete():
    global library_log_content_mainframe, db_file

    confirm = messagebox.askokcancel("Confirmation", "Are you sure you want to end this log?")
    conn = sqlite3.connect(db_file)
    conn.close()
    if confirm:
        print("Library Log Back Button is Clicked")
        library_log_content_mainframe.pack_forget()
        mainframe1.pack(fill=BOTH, expand=True)
        mainframe2.pack(fill=BOTH, expand=True)

    else:
        # Do nothing if user cancels the action
        pass

def library_log_content_print():
    global db_file

    result = messagebox.askokcancel('Print', 'Do you want to print your Library Log as pdf?')
    if result:  # User clicked "OK"

        filename = os.path.basename(db_file)
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", f"{filename}.pdf")  # Path to the Downloads directory

        # Fetch data from the database 
        connhistory = sqlite3.connect(db_file)
        cursorhistory = connhistory.cursor()
        cursorhistory.execute("SELECT * FROM LibraryLog")
        rows = cursorhistory.fetchall()
        connhistory.close()

        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=1)

        # Add a page and set font
        pdf.add_page()
        pdf.set_font("Arial", size=7)

        # Set column widths and heights
        col_widths = [16, 13, 60, 18, 16, 28, 28, 13]  # Adjust these widths according to your data
        col_height = 6

        # Add headers
        headers = ['id', 'controlid', 'name', 'position', 'department', 'timein', 'timeout', 'overtime']

        if len(headers) == len(col_widths):
            for header, width in zip(headers, col_widths):
                pdf.cell(width, col_height, header, border=1)
            pdf.ln(col_height)  # Move to the next line

            # Add data rows
            for row in rows:
                for item, width in zip(row[1:], col_widths):
                    pdf.cell(width, col_height, str(item), border=1)
                pdf.ln(col_height)

            pdf.output(downloads_path)  # Save the PDF file in the Downloads directory

            # Open the generated PDF file
            if os.path.exists(downloads_path):
                os.startfile(downloads_path)

        else:
            print("The number of headers does not match the number of column widths.")
    else:
        return


def history_log_content():
    global history_log_content_mainframe, history_log_content_frame3_history_table_treeview, history_log_content_frame3_function_frame_entry

    print("History Log Button is Clicked")

    mainframe1.pack_forget()
    mainframe2.pack_forget()

    #Mainframe
    history_log_content_mainframe = CTkFrame(master=root, bg_color="white", fg_color="white")
    history_log_content_mainframe.pack(fill=BOTH, expand=True)

    #Frame 1
    history_log_content_frame1 = CTkFrame(master=history_log_content_mainframe, bg_color="lightgreen", fg_color="lightgreen", corner_radius=0 ,height=35)
    history_log_content_frame1.pack(fill=X, side=TOP, anchor=N, pady=(0,5))

    history_log_content_frame1_back_button_icon = Image.open("back-button.png")

    history_log_content_frame1_back_button = CTkButton(master=history_log_content_frame1, command=history_log_content_delete, image=CTkImage(dark_image=history_log_content_frame1_back_button_icon, size=(15,15)), text="Back", text_color="black", width=40, height=20, bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5, hover_color="#52D452")
    history_log_content_frame1_back_button.pack(side=LEFT, anchor=W, padx=5, pady=5)

    #Frame 2
    history_log_content_frame2 = CTkFrame(master=history_log_content_mainframe, bg_color="lightgreen", fg_color="lightgreen", corner_radius=0, height=60)
    history_log_content_frame2.pack(fill=X, side=TOP, anchor=N)

    history_log_content_frame2_book_icon = Image.open("book_icon.png")
    
    history_log_content_frame2_book_logo = CTkLabel(history_log_content_frame2, image=CTkImage(dark_image=history_log_content_frame2_book_icon, size=(90,90)), text="", fg_color="transparent", bg_color="transparent")
    history_log_content_frame2_book_logo.pack(side=LEFT, anchor=W, padx=5, pady=5)

    history_log_content_frame2_header = CTkLabel(master=history_log_content_frame2, text="History Log", text_color="black", font=header_font, width=40, height=20, bg_color="lightgreen", fg_color="lightgreen")
    history_log_content_frame2_header.pack(side=LEFT, anchor=W, padx=5, pady=(5,0))

    #Frame 3
    history_log_content_frame3 = CTkFrame(master=history_log_content_mainframe, bg_color="lightgreen", fg_color="lightgreen")
    history_log_content_frame3.pack(fill=BOTH, expand=True, side=TOP, anchor=N)

    ##Search Frame
    history_log_content_frame3_function_frame = CTkFrame(master=history_log_content_frame3, bg_color="lightgreen", fg_color="lightgreen")
    history_log_content_frame3_function_frame.pack(side=TOP, anchor=W, padx=(20,5), pady=5)

    history_log_content_frame3_function_frame_entry = CTkEntry(master=history_log_content_frame3_function_frame,  width=200, font=content_entry_font, text_color="black", bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5)
    history_log_content_frame3_function_frame_entry.grid(row=0, column=0, sticky=W)

    history_log_content_frame3_function_frame_search_button = CTkButton(master=history_log_content_frame3_function_frame,  command=history_search_history_log,text="Search", text_color="black", font=content_button_font, bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5, hover_color="#52D452", width=110, height=30)
    history_log_content_frame3_function_frame_search_button.grid(row=0, column=1, padx=5, pady=5, sticky=W), 

    history_log_content_frame3_function_frame_open_button = CTkButton(master=history_log_content_frame3_function_frame, command=confirm_open, text="Open", text_color="black", font=content_button_font, bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5, hover_color="#52D452", width=110, height=30)
    history_log_content_frame3_function_frame_open_button.grid(row=0, column=2, padx=5, pady=5, sticky=W), 

    history_log_content_frame3function_frame_delete_button = CTkButton(master=history_log_content_frame3_function_frame, command=history_log_delete_file_by_name, text="Delete", text_color="black", font=content_button_font, bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5, hover_color="#52D452", width=110, height=30)
    history_log_content_frame3function_frame_delete_button.grid(row=0, column=3, padx=5, pady=5, sticky=W), 

    ##History Frame
    history_log_content_frame3_table_frame = CTkFrame(master=history_log_content_frame3, bg_color="lightgreen", fg_color="lightgreen")
    history_log_content_frame3_table_frame.pack(fill=BOTH, expand=True, side=TOP, anchor=W, padx=20, pady=(5,20))

    history_log_content_frame3_history_table = CTkFrame(master=history_log_content_frame3_table_frame, bg_color="transparent", fg_color="transparent", corner_radius=10, border_color="black", border_width=2)
    history_log_content_frame3_history_table.pack(fill=BOTH, expand=True, side=TOP, anchor=CENTER)

    style = ttk.Style(root)
    style.theme_use('classic')
    style.configure("Treeview.Heading", background='lightgreen', foreground='black', font=("Times New Roman", 16))  # Header
    style.configure("Treeview", font=("Times New Roman", 14)) #Body

    history_log_content_frame3_history_table_treeview = ttk.Treeview(history_log_content_frame3_history_table, columns=('name', 'date'), show='headings', style='Treeview')
    history_log_content_frame3_history_table_treeview.pack(expand=True, fill=BOTH)

    history_log_content_frame3_history_table_treeview.heading('name', text="NAME", anchor=W)
    history_log_content_frame3_history_table_treeview.heading('date', text="DATE CREATED", anchor=W)

    history_log_content_frame3_history_table_treeview.column('name', width=150, anchor=W)
    history_log_content_frame3_history_table_treeview.column('date', width=50, anchor=W)

    history_log_content_frame3_history_table_treeview.bind('<ButtonRelease>', open_selected_file)

    historylog_content_display_history_data()

def historylog_content_display_history_data():
    global history_log_content_frame3_history_table_treeview

    connlist = sqlite3.connect('SoftwareData.db')  # Create a new connection to the selected file
    cursorlist = connlist.cursor()
    cursorlist.execute("SELECT * FROM HistoryLog")
    rows = cursorlist.fetchall()
    
    # Clear existing data
    history_log_content_frame3_history_table_treeview.delete(*history_log_content_frame3_history_table_treeview.get_children())

    # Insert fetched rows at the bottom by setting index='end'
    for row in rows:
        history_log_content_frame3_history_table_treeview.insert('', END, values=(row[1], row[2]))

    connlist.close()

def history_search_history_log():
    search_text = history_log_content_frame3_function_frame_entry.get().lower()  # Get the text from the entry
    if search_text:  # If there's text in the search entry
        found = False
        for row_id in history_log_content_frame3_history_table_treeview.get_children():
            values = history_log_content_frame3_history_table_treeview.item(row_id)['values']
            if search_text in [str(value).lower() for value in values]:
                history_log_content_frame3_history_table_treeview.selection_set(row_id)  # Select the matching row
                history_log_content_frame3_history_table_treeview.focus(row_id)  # Focus on the matching row
                found = True
                break  # Exit loop once a match is found

        if not found:
            messagebox.showinfo("Not Found", f"File '{search_text}' doesn't exist.")
    else:
        messagebox.showinfo("Warning", "Please enter text to search.")

def open_selected_db_file():
    global db_file

    if db_file:
        print("Trying to open:", db_file)  # Check the filename for troubleshooting

        # Check if the file exists at the specified path
        if os.path.exists(db_file):
            try:
                open_base_on_filename(db_file)
            except OSError:
                print("Failed to open the file", db_file)
        else:
            messagebox.showinfo("Error", "File doesn't exist.")
    else:
        messagebox.showinfo("Error", "No file selected.")

def open_selected_file(event, confirmation):
    global db_file
    
    if confirmation == 1:
        selected_item = history_log_content_frame3_history_table_treeview.focus()

        if selected_item:
            # Get the file name from the selected item
            db_file = history_log_content_frame3_history_table_treeview.item(selected_item)['values'][0]
            open_selected_db_file()
        else:
            messagebox.showinfo("Error", "No file selected.")
    else:
        return

def history_log_delete_file_by_name():
    global history_log_content_frame3_history_table_treeview

    result = messagebox.askokcancel('Warning', 'Are you sure you want to delete this file, this can never be retrieved?')

    selected_item = history_log_content_frame3_history_table_treeview.focus()

    if result:
        if selected_item:
            db_file = history_log_content_frame3_history_table_treeview.item(selected_item)['values'][0]
            
            conn = sqlite3.connect('SoftwareData.db')
            cursor = conn.cursor()

            # Delete the selected file from the database
            cursor.execute("DELETE FROM HistoryLog WHERE name = ?", (db_file,))
            conn.commit()

            conn.close()

            # Refresh the displayed data after deletion
            historylog_content_display_history_data()
        else:
            print("No file selected for deletion.")

def confirm_open():
    confirmation = 1
    open_selected_file(None, confirmation)

def open_base_on_filename(db_file):
    connhistory = sqlite3.connect(db_file)  # Connect to the selected database file
    connhistory.execute('''
    CREATE TABLE IF NOT EXISTS "LibraryLog" (
        "masterid"	INTEGER NOT NULL,
        "id"	varchar(255) NOT NULL,
        "controlid"	varchar(255) NOT NULL,
        "name"	varchar(255) NOT NULL,
        "position"	varchar(255) NOT NULL,
        "department"	varchar(255) NOT NULL,
        "timein"	varchar(255) DEFAULT 'TIMESTAMP',
        "timeout"	varchar(255),
        "overtime"	varchar(255) DEFAULT '-----',
        PRIMARY KEY("masterid" AUTOINCREMENT)
        )
    ''')  # Create a new Student table

    history_log_content_mainframe.pack_forget()

    library_log_content()
    print("Database Opened")

def history_log_content_delete():
    global history_log_content_mainframe

    print("History Log Back Button is Clicked.")
    history_log_content_mainframe.pack_forget()
    mainframe1.pack(fill=BOTH, expand=True)
    mainframe2.pack(fill=BOTH, expand=True)

def SP_list_content():
    global SP_list_content_mainframe, SP_list_content_professor_tree_frame_treeview, SP_list_content_student_tree_frame_treeview, SP_list_content_frame3_tab, SP_list_content_information_frame2_id_entry, SP_list_content_information_frame2_name_entry, SP_list_content_information_frame2_position_entry, SP_list_content_information_frame2_department_entry

    print("Students and Professors List Button is Clicked")
    mainframe1.pack_forget()
    mainframe2.pack_forget() 

    connlist.execute('''
    CREATE TABLE IF NOT EXISTS "StudentsList" (
        "id"	INTEGER NOT NULL UNIQUE,
        "name"	varchar(255) NOT NULL,
        "position"	varchar(255) NOT NULL,
        "department"	varchar(255) NOT NULL
        );
    ''') 

    connlist.execute('''
    CREATE TABLE IF NOT EXISTS "ProfessorsList" (
        "id"	INTEGER NOT NULL UNIQUE,
        "name"	varchar(255) NOT NULL,
        "position"	varchar(255) NOT NULL,
        "department"	varchar(255) NOT NULL
        );
    ''') 

    SP_list_content_mainframe = CTkFrame(master=root, bg_color="white", fg_color="white")
    SP_list_content_mainframe.pack(fill=BOTH, expand=True)

    #Back Button
    SP_list_content_frame1 = CTkFrame(master=SP_list_content_mainframe, bg_color="lightgreen", fg_color="lightgreen", corner_radius=0 ,height=35)
    SP_list_content_frame1.pack(fill=X, side=TOP, anchor=N, pady=(0,5))

    SP_list_content_back_button_icon = Image.open("back-button.png")

    SP_list_content_frame1_back_button = CTkButton(master=SP_list_content_frame1, command=SP_list_content_delete, image=CTkImage(dark_image=SP_list_content_back_button_icon, size=(15,15)), text="Back", text_color="black", font=content_button_font, width=40, height=20, bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5, hover_color="#52D452")
    SP_list_content_frame1_back_button.pack(side=LEFT, anchor=W, padx=5, pady=5)

    SP_list_content_frame1_header = CTkLabel(master=SP_list_content_frame1, text="Students and Professors Lists", text_color="black", font=("Times New Roman", 35, 'bold'), bg_color="transparent", fg_color="transparent")
    SP_list_content_frame1_header.pack(side=TOP, anchor=N, padx=5, pady=5)

    #Informations
    SP_list_content_frame2 = CTkFrame(master=SP_list_content_mainframe, bg_color="lightgreen", fg_color="lightgreen", border_color="lightgreen", border_width=1)
    SP_list_content_frame2.pack(fill=Y, side=LEFT, anchor=W, padx=(0,2.5))

    ##Header Frame
    SP_list_content_frame2_header_frame = CTkFrame(master=SP_list_content_frame2, bg_color="lightgreen", fg_color="lightgreen", height=35)
    SP_list_content_frame2_header_frame.pack(fill=X, side=TOP, anchor=N)

    SP_list_content_frame2_header_frame_content = CTkLabel(master=SP_list_content_frame2_header_frame, text="Personal Details", font=("Times New Roman", 40), text_color="black" ,bg_color="lightgreen", fg_color="lightgreen")
    SP_list_content_frame2_header_frame_content.pack(padx=10, pady=5)

    ##Information Frame
    SP_list_content_information_frame2 = CTkFrame(master=SP_list_content_frame2, bg_color="lightgreen", fg_color="lightgreen")
    SP_list_content_information_frame2.pack(fill=BOTH, expand=True,side=TOP, anchor=N)

    SP_list_content_information_frame2_id_label = CTkLabel(master=SP_list_content_information_frame2, text="Personal ID:", font=content_label_font, text_color="black", bg_color="lightgreen", fg_color="lightgreen")
    SP_list_content_information_frame2_id_label.grid(row=0,column=0, padx=(10,5), pady=5, sticky=W)

    SP_list_content_information_frame2_id_entry = CTkEntry(master=SP_list_content_information_frame2, width=250, font=content_entry_font, text_color="black", bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5)
    SP_list_content_information_frame2_id_entry.grid(row=0,column=1, padx=(5,10), pady=5)

    SP_list_content_information_frame2_name_label = CTkLabel(master=SP_list_content_information_frame2, text="Name:", font=content_label_font, text_color="black", bg_color="lightgreen", fg_color="lightgreen")
    SP_list_content_information_frame2_name_label.grid(row=1,column=0, padx=(10,5), pady=5, sticky=W)

    SP_list_content_information_frame2_name_entry = CTkEntry(master=SP_list_content_information_frame2, font=content_entry_font, width=250, text_color="black", bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5)
    SP_list_content_information_frame2_name_entry.grid(row=1,column=1, padx=(5,10), pady=5)

    SP_list_content_information_frame2_position_label = CTkLabel(master=SP_list_content_information_frame2, text="Position:", font=content_label_font, text_color="black", bg_color="lightgreen", fg_color="lightgreen")
    SP_list_content_information_frame2_position_label.grid(row=2,column=0, padx=(10,5), pady=5, sticky=W)

    SP_list_content_information_frame2_position_entry = CTkEntry(master=SP_list_content_information_frame2, font=content_entry_font, width=250, text_color="black", bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5)
    SP_list_content_information_frame2_position_entry.grid(row=2,column=1, padx=(5,10), pady=5)

    SP_list_content_information_frame2_department_label = CTkLabel(master=SP_list_content_information_frame2, text="Department:", font=content_label_font, text_color="black", bg_color="lightgreen", fg_color="lightgreen")
    SP_list_content_information_frame2_department_label.grid(row=3,column=0, padx=(10,5), pady=5, sticky=W)

    SP_list_content_information_frame2_department_entry = CTkEntry(master=SP_list_content_information_frame2, font=content_entry_font, width=250, text_color="black", bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5)
    SP_list_content_information_frame2_department_entry.grid(row=3,column=1, padx=(5,10), pady=5)

    SP_list_content_information_frame2_button_submit = CTkButton(master=SP_list_content_information_frame2, command=SP_list_content_submit_data, text="Submit", text_color="black", font=content_button_font, bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5, hover_color="#52D452")
    SP_list_content_information_frame2_button_submit.grid(row=4, column=0, padx=(20,5), pady=(30,5))

    SP_list_content_information_frame2_button_update = CTkButton(master=SP_list_content_information_frame2, command=SP_list_content_update_data, text="Update", text_color="black", font=content_button_font, fg_color="white", border_color="black", border_width=1.5, hover_color="#52D452")
    SP_list_content_information_frame2_button_update.grid(row=4, column=1, padx=(5,10), pady=(30,5))

    SP_list_content_information_frame2_button_deselect = CTkButton(master=SP_list_content_information_frame2, command=SP_list_content_deselect_data, text="De-Select", text_color="black", font=content_button_font, bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5, hover_color="#52D452")
    SP_list_content_information_frame2_button_deselect.grid(row=5, column=0, padx=(20,5), pady=5)

    SP_list_content_information_frame2_button_delete = CTkButton(master=SP_list_content_information_frame2, command=SP_list_content_delete_data, text="Delete", text_color="black", font=content_button_font, bg_color="lightgreen", fg_color="white", border_color="black", border_width=1.5, hover_color="#52D452")
    SP_list_content_information_frame2_button_delete.grid(row=5, column=1, padx=(5,10), pady=5)

    #Frame 3
    SP_list_content_frame3 = CTkFrame(master=SP_list_content_mainframe, bg_color="lightgreen", fg_color="lightgreen")
    SP_list_content_frame3.pack(fill=BOTH, expand=True, side=RIGHT,anchor=E, padx=(2.5,0))

    SP_list_content_frame3_tab = CTkTabview(master=SP_list_content_frame3, text_color="black",bg_color="lightgreen", fg_color="white", border_color="lightgreen", border_width=5, segmented_button_fg_color="lightgreen", segmented_button_selected_hover_color="#52D452", segmented_button_unselected_hover_color="#52D452", segmented_button_unselected_color="lightgreen", segmented_button_selected_color="#52D452")
    SP_list_content_frame3_tab.pack(fill=BOTH, expand=True)

    ##Student Tab 
    style = ttk.Style(root)
    style.theme_use('classic')
    style.configure("Treeview.Heading", background='lightgreen', foreground='black', font=("Comic sans", 12))  # Header color
    style.configure("Treeview", font=("Comic sans", 10))  # Body color

    ###Treeview
    SP_list_content_frame3_tab.add("Student")
    SP_list_content_student_tree_frame = CTkFrame(master=SP_list_content_frame3_tab.tab("Student"))
    SP_list_content_student_tree_frame.pack(expand=True, fill=BOTH)

    SP_list_content_student_tree_frame_treeview = ttk.Treeview(SP_list_content_student_tree_frame, columns=('id', 'name', 'position', 'department'), show='headings', style='Treeview')
    SP_list_content_student_tree_frame_treeview.pack(expand=True, fill=BOTH)

    SP_list_content_student_tree_frame_treeview.heading('id', text='STUDENT ID')
    SP_list_content_student_tree_frame_treeview.heading('name', text='NAME')
    SP_list_content_student_tree_frame_treeview.heading('position', text='POSITION')
    SP_list_content_student_tree_frame_treeview.heading('department', text='DEPARTMENT')
    SP_list_content_student_tree_frame_treeview.bind('<ButtonRelease>', SP_list_content_select_student_data)

    ##Professor Tab
    SP_list_content_frame3_tab.add("Professor")

    SP_list_content_professor_tree_frame = CTkFrame(master=SP_list_content_frame3_tab.tab("Professor"))
    SP_list_content_professor_tree_frame.pack(expand=True, fill=BOTH)

    SP_list_content_professor_tree_frame_treeview = ttk.Treeview(SP_list_content_professor_tree_frame, columns=('id', 'name', 'position', 'department'), show='headings', style='Treeview')
    SP_list_content_professor_tree_frame_treeview.pack(expand=True, fill=BOTH)

    SP_list_content_professor_tree_frame_treeview.heading('id', text='PROFESSOR ID')
    SP_list_content_professor_tree_frame_treeview.heading('name', text='NAME')
    SP_list_content_professor_tree_frame_treeview.heading('position', text='POSITION')
    SP_list_content_professor_tree_frame_treeview.heading('department', text='DEPARTMENT')
    SP_list_content_professor_tree_frame_treeview.bind('<ButtonRelease>', SP_list_content_select_professor_data)

    SP_list_content_display_student_data()
    SP_list_content_display_professor_data()

def SP_list_content_delete():
    global SP_list_content_mainframe

    print("Students and Professors List Back Button is Clicked")
    SP_list_content_mainframe.pack_forget()
    mainframe1.pack(fill=BOTH, expand=True)
    mainframe2.pack(fill=BOTH, expand=True)

def SP_list_content_frame3_get_selected_tab():
    SP_list_content_frame3_current_tab = SP_list_content_frame3_tab.get()
    return SP_list_content_frame3_tab.index(SP_list_content_frame3_current_tab)

def SP_list_content_submit_data():
    global SP_list_content_frame3_tab, SP_list_content_information_frame2_id_entry, SP_list_content_information_frame2_name_entry, SP_list_content_information_frame2_position_entry, SP_list_content_information_frame2_department_entry

    # Get values from entry fields
    id_value = SP_list_content_information_frame2_id_entry.get()
    name_value = SP_list_content_information_frame2_name_entry.get()
    position_value = SP_list_content_information_frame2_position_entry.get()
    department_value = SP_list_content_information_frame2_department_entry.get()

    if not (id_value.strip() and name_value.strip() and position_value.strip() and department_value.strip()):
        messagebox.showinfo("Missing Information", "Please fill in all fields.")
        return

    connlist = sqlite3.connect('SoftwareData.db')  # Create a new connection to the selected file
    cursorlist = connlist.cursor()

    SP_list_content_frame3_current_tab = SP_list_content_frame3_get_selected_tab()

    if SP_list_content_frame3_current_tab == 0: #Student Tab
        # Check if the student ID already exists
        cursorlist.execute("SELECT * FROM StudentsList WHERE id=?", (id_value,))
        existing_student_id = cursorlist.fetchone()

        cursorlist.execute("SELECT * FROM ProfessorsList WHERE id=?", (id_value,))
        existing_professor_id = cursorlist.fetchone()

        if existing_student_id or existing_professor_id:
            messagebox.showinfo("Personal ID Exists", "This Personal ID already exists.")
            return

        data_insert_query = '''
        INSERT INTO StudentsList ("id", "name", "position", "department") VALUES (?, ?, ?, ?)
        '''

    elif SP_list_content_frame3_current_tab == 1: #Student Tab
        # Check if the professor ID already exists
        cursorlist.execute("SELECT * FROM ProfessorsList WHERE id=?", (id_value,))
        existing_professor_id = cursorlist.fetchone()

        cursorlist.execute("SELECT * FROM StudentsList WHERE id=?", (id_value,))
        existing_student_id = cursorlist.fetchone()

        if existing_professor_id or existing_student_id:
            messagebox.showinfo("Personal ID Exists", "This Personal ID already exists.")
            return

        data_insert_query = '''
        INSERT INTO ProfessorsList ("id", "name", "position", "department") VALUES (?, ?, ?, ?)
        '''

    data_insert_list = [id_value, name_value, position_value, department_value]

    try:
        cursorlist.execute(data_insert_query, data_insert_list)
        connlist.commit()

        # Display the submitted data in the respective Treeview (Student or Professor)
        if SP_list_content_frame3_current_tab == 0:
            SP_list_content_display_student_data()
            print("Student's data inserted")

        elif SP_list_content_frame3_current_tab == 1:
            SP_list_content_display_professor_data()
            print("Professor's data inserted")

        # Clear the entry fields after successful submission
        SP_list_content_information_frame2_id_entry.delete(0, END)
        SP_list_content_information_frame2_name_entry.delete(0, END)
        SP_list_content_information_frame2_position_entry.delete(0, END)
        SP_list_content_information_frame2_department_entry.delete(0, END) 

    except sqlite3.Error as e:
        connlist.rollback()
        print("Error occurred:", e)
    connlist.close()

def SP_list_content_update_data():
    SP_list_content_frame3_current_tab = SP_list_content_frame3_get_selected_tab()

    update_id = SP_list_content_information_frame2_id_entry.get()
    update_name = SP_list_content_information_frame2_name_entry.get()
    update_position = SP_list_content_information_frame2_position_entry.get()
    update_department = SP_list_content_information_frame2_department_entry.get()

    if not (update_id.strip() and update_name.strip() and update_position.strip() and update_department.strip()):
        messagebox.showinfo("Missing Information", "Please fill in all fields.")
        return

    if SP_list_content_frame3_current_tab == 0:  # Student Tab

        # Call the update function with the old ID, new ID, and other updated fields
        SP_list_content_update_person(update_id, update_name, update_position, update_department)
        SP_list_content_display_student_data()
        SP_list_content_deselect_data()
        messagebox.showinfo('Data Updated', 'The data has been updated')
        print("The student's data has been updated")

    elif SP_list_content_frame3_current_tab == 1:  # Professor Tab

        # Call the update function with the old ID, new ID, and other updated fields
        SP_list_content_update_person(update_id, update_name, update_position, update_department)
        SP_list_content_display_professor_data()
        SP_list_content_deselect_data()
        messagebox.showinfo('Data Updated', 'The data has been updated')
        print("The professor's data has been updated")
    

def SP_list_content_update_person(old_id, new_name, new_position, new_department):
    connlist = sqlite3.connect('SoftwareData.db')  # Create a new connection to the selected file
    cursorlist = connlist.cursor()
    SP_list_content_frame3_current_tab = SP_list_content_frame3_get_selected_tab()

    if SP_list_content_frame3_current_tab == 0:  # Student Tab
        # Update the existing record with new information
        cursorlist.execute('UPDATE StudentsList SET name=?, position=?, department=? WHERE id=?', (new_name, new_position, new_department, old_id))
        connlist.commit()

    elif SP_list_content_frame3_current_tab == 1:  # Professor Tab
        # Update the existing record with new information
        cursorlist.execute('UPDATE ProfessorsList SET name=?, position=?, department=? WHERE id=?', (new_name, new_position, new_department, old_id))
        connlist.commit()
    connlist.close()

def SP_list_content_select_student_data(event):
    global SP_list_content_student_tree_frame_treeview

    selected_item = SP_list_content_student_tree_frame_treeview.focus()
    if selected_item:
        SP_list_content_student_tree_frame_treeview.selection_set(selected_item)
        SP_list_content_student_tree_frame_treeview_row = SP_list_content_student_tree_frame_treeview.item(selected_item)['values']
        SP_list_content_information_frame2_id_entry.delete(0, END)
        SP_list_content_information_frame2_id_entry.insert(0,SP_list_content_student_tree_frame_treeview_row[0])
        SP_list_content_information_frame2_name_entry.delete(0, END)
        SP_list_content_information_frame2_name_entry.insert(0,SP_list_content_student_tree_frame_treeview_row[1])
        SP_list_content_information_frame2_position_entry.delete(0, END)
        SP_list_content_information_frame2_position_entry.insert(0,SP_list_content_student_tree_frame_treeview_row[2])
        SP_list_content_information_frame2_department_entry.delete(0, END)
        SP_list_content_information_frame2_department_entry.insert(0,SP_list_content_student_tree_frame_treeview_row[3])
    else:
        pass

def SP_list_content_select_professor_data(event):
    global SP_list_content_professor_tree_frame_treeview

    selected_item = SP_list_content_professor_tree_frame_treeview.focus()
    if selected_item:
        SP_list_content_professor_tree_frame_treeview.selection_set(selected_item)
        SP_list_content_professor_tree_frame_treeview_row = SP_list_content_professor_tree_frame_treeview.item(selected_item)['values']
        SP_list_content_information_frame2_id_entry.delete(0, END)
        SP_list_content_information_frame2_id_entry.insert(0,SP_list_content_professor_tree_frame_treeview_row[0])
        SP_list_content_information_frame2_name_entry.delete(0, END)
        SP_list_content_information_frame2_name_entry.insert(0,SP_list_content_professor_tree_frame_treeview_row[1])
        SP_list_content_information_frame2_position_entry.delete(0, END)
        SP_list_content_information_frame2_position_entry.insert(0,SP_list_content_professor_tree_frame_treeview_row[2])
        SP_list_content_information_frame2_department_entry.delete(0, END)
        SP_list_content_information_frame2_department_entry.insert(0,SP_list_content_professor_tree_frame_treeview_row[3])
    else: 
        pass

def SP_list_content_deselect_data(*clicked):
    global SP_list_content_professor_tree_frame_treeview, SP_list_content_student_tree_frame_treeview

    SP_list_content_frame3_current_tab = SP_list_content_frame3_get_selected_tab()

    if SP_list_content_frame3_current_tab == 0: #Student Tab
        selected_item = SP_list_content_student_tree_frame_treeview.focus()
        if selected_item:
            SP_list_content_student_tree_frame_treeview.selection_remove(selected_item)
            print("Student Information Deselected")
        
    elif SP_list_content_frame3_current_tab == 1:  # Professor Tab
        selected_item = SP_list_content_professor_tree_frame_treeview.focus()
        if selected_item:
            SP_list_content_professor_tree_frame_treeview.selection_remove(selected_item)
            print("Professor Information Deselected")

    SP_list_content_information_frame2_id_entry.delete(0, END)
    SP_list_content_information_frame2_name_entry.delete(0, END)
    SP_list_content_information_frame2_position_entry.delete(0, END)
    SP_list_content_information_frame2_department_entry.delete(0, END)

def SP_list_content_delete_data():
    SP_list_content_frame3_current_tab = SP_list_content_frame3_get_selected_tab()

    delete_id = SP_list_content_information_frame2_id_entry.get()
    delete_name = SP_list_content_information_frame2_name_entry.get()
    delete_position = SP_list_content_information_frame2_position_entry.get()
    delete_department = SP_list_content_information_frame2_department_entry.get()

    if not (delete_id.strip() and delete_name.strip() and delete_position.strip() and delete_department.strip()):
        messagebox.showinfo("Missing Information", "Please fill in all fields.")
        return

    if SP_list_content_frame3_current_tab == 0:  # Student Tab
        delete_id_value = SP_list_content_information_frame2_id_entry.get()
        result = messagebox.askokcancel('Warning', 'Are you sure you want to delete this student\'s data?')
        if result:  # User clicked "OK"
            SP_list_content_delete_person(delete_id_value)
            SP_list_content_deselect_data()
            SP_list_content_display_student_data()
            print("Student's data has been deleted")

    elif SP_list_content_frame3_current_tab == 1:  # Professor Tab
        delete_id_value = SP_list_content_information_frame2_id_entry.get()
        result = messagebox.askokcancel('Warning', 'Are you sure you want to delete this professor\'s data?')
        if result:  # User clicked "OK"
            SP_list_content_delete_person(delete_id_value)
            SP_list_content_deselect_data()
            SP_list_content_display_professor_data()
            print("Professor's data has been deleted")

def SP_list_content_delete_person(id):
    connlist = sqlite3.connect('SoftwareData.db')  # Create a new connection to the selected file
    cursorlist = connlist.cursor()
    SP_list_content_frame3_current_tab = SP_list_content_frame3_get_selected_tab()

    if SP_list_content_frame3_current_tab == 0: #Student Tab
        cursorlist.execute('DELETE FROM StudentsList WHERE id = ?', (id,))
    elif SP_list_content_frame3_current_tab == 1:  # Professor Tab
        cursorlist.execute('DELETE FROM ProfessorsList WHERE id = ?', (id,))
    connlist.commit()
    connlist.close()

def SP_list_content_display_student_data():
    global SP_list_content_student_tree_frame_treeview
    connlist = sqlite3.connect('SoftwareData.db')  # Create a new connection to the selected file
    cursorlist = connlist.cursor()
    cursorlist.execute("SELECT * FROM StudentsList")
    rows = cursorlist.fetchall()
    
    # Clear existing data
    SP_list_content_student_tree_frame_treeview.delete(*SP_list_content_student_tree_frame_treeview.get_children())

    # Insert fetched rows at the bottom by setting index='end'
    for row in rows:
        SP_list_content_student_tree_frame_treeview.insert('', END, values=(row[0], row[1], row[2], row[3]))

    connlist.close()

def SP_list_content_display_professor_data():
    global SP_list_content_professor_tree_frame_treeview
    connlist = sqlite3.connect('SoftwareData.db')  # Create a new connection to the selected file
    cursorlist = connlist.cursor()
    cursorlist.execute("SELECT * FROM ProfessorsList")
    rows = cursorlist.fetchall()
    
    # Clear existing data
    SP_list_content_professor_tree_frame_treeview.delete(*SP_list_content_professor_tree_frame_treeview.get_children())

    # Insert fetched rows at the bottom by setting index='end'
    for row in rows:
        SP_list_content_professor_tree_frame_treeview.insert('', END, values=(row[0], row[1], row[2], row[3]))
    
    connlist.close()


root = CTk()
root.title("Library Log")
root.geometry("1100x800")

header_font = ("Times New Roman", 45)
body_font = ("Times New Roman", 28)
header_font_color = "black"
body_font_color = "black"
button_border_color = "#55DE2F"
content_button_font = ("Times New Roman", 15)
content_label_font = ("Times New Roman", 20)
content_entry_font = ("Times New Roman", 15)


# Upper Frame
mainframe1 = CTkFrame(master=root, bg_color="white", fg_color="white")
mainframe1.pack(fill=BOTH, expand=True)

homepage_title = CTkLabel(master=mainframe1, text="Library Attendance Monitoring System" ,font=header_font, text_color=header_font_color)
homepage_title.pack(fill=BOTH, side=BOTTOM)

# Lower Frame
mainframe2 = CTkFrame(master=root, bg_color="white", fg_color="white")
mainframe2.pack(fill=BOTH, expand=True)

#New log frames
new_log_frame = CTkFrame(master=mainframe2, fg_color="transparent")
new_log_frame.pack(side=LEFT, expand=True, fill=BOTH)

new_log_icon = Image.open("homepage_new-log-icon.png")

new_log_button = CTkButton(master=new_log_frame, command=create_new_library_log, text="", image=CTkImage(dark_image=new_log_icon, size=(40,40)), width=100, height=100, fg_color="transparent", border_color=button_border_color , border_width=2, corner_radius=20, hover_color="#55C636")
new_log_button.pack(pady=(50,0))

new_log_label = CTkLabel(master=new_log_frame, text="New Log", font=body_font, text_color=body_font_color)
new_log_label.pack()

#Existing log frames
existing_log_frame = CTkFrame(master=mainframe2, fg_color="transparent")
existing_log_frame.pack(side=LEFT, expand=True, fill=BOTH)

existing_log_icon = Image.open("homepage_existing-log-icon.png")

existing_log_button = CTkButton(master=existing_log_frame, command=open_existing_library_log, text="", image=CTkImage(dark_image=existing_log_icon, size=(40,40)), width=100, height=100, fg_color="transparent", border_color=button_border_color , border_width=2, corner_radius=20, hover_color="#55C636")
existing_log_button.pack(pady=(50,0))

existing_log_label = CTkLabel(master=existing_log_frame, text="Existing Log", font=body_font, text_color=body_font_color)
existing_log_label.pack()

#SP frames
SP_list_frame = CTkFrame(master=mainframe2, fg_color="transparent")
SP_list_frame.pack(side=LEFT, expand=True, fill=BOTH)

SP_list_icon = Image.open("homepage_SP-icon.png")

SP_list_button = CTkButton(master=SP_list_frame, command=SP_list_content, text="", image=CTkImage(dark_image=SP_list_icon, size=(40,40)), width=100, height=100, fg_color="transparent", border_color=button_border_color , border_width=2, corner_radius=20, hover_color="#55C636")
SP_list_button.pack(pady=(50,0))

SP_list_label = CTkLabel(master=SP_list_frame, text="List of Students\n& Professors", font=body_font, text_color=body_font_color)
SP_list_label.pack()

#History Log frames
history_log_frame = CTkFrame(master=mainframe2, fg_color="transparent")
history_log_frame.pack(side=LEFT, expand=True, fill=BOTH)

history_log_icon = Image.open("homepage_history-log-icon.png")

history_log_button = CTkButton(master=history_log_frame, command=history_log_content, text="", image=CTkImage(dark_image=history_log_icon, size=(40,40)), width=100, height=100, fg_color="transparent", border_color=button_border_color , border_width=2, corner_radius=20, hover_color="#55C636")
history_log_button.pack(pady=(50,0))

history_log_label = CTkLabel(master=history_log_frame, text="History Log", font=body_font, text_color=body_font_color)
history_log_label.pack()

connlist = sqlite3.connect('SoftwareData.db')  # Create a new connection to the selected file
connlist.execute('''
    CREATE TABLE IF NOT EXISTS "HistoryLog" (
        "masterid"	INTEGER NOT NULL,
        "name"	varchar(255) NOT NULL,
        "date"	TEXT NOT NULL,
        PRIMARY KEY("masterid" AUTOINCREMENT)
    );
''') # Create a new history log table

print("History Log Database are connected by default")

root.mainloop()
