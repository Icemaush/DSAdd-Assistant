from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os
import csv

window = Tk()
window.title("DSAdd Assistant")
frame = Frame(window)
frame.pack()

mode_frame = Frame(window)
mode_frame.pack(pady=5)
top_frame = Frame(window)
top_frame.pack(pady=10, padx=10)
input_frame = Frame(top_frame)
input_frame.pack()
parameter_frame = Frame(top_frame)
parameter_frame.pack()
text_frame = Frame(window)
text_frame.pack(padx=15, expand=True, fill=BOTH)
topbtn_frame = Frame(window)
topbtn_frame.pack(pady=0)
btmbtn_frame = Frame(window)
btmbtn_frame.pack(pady=0)
status_frame = Frame(window)
status_frame.pack(side=LEFT)

desktop = os.path.expanduser("~/Desktop")

mode = StringVar()
firstname = StringVar()
lastname = StringVar()
groupname = StringVar()
computername = StringVar()
ouname = StringVar()
orgunit = StringVar()
domain = StringVar()
s = StringVar()

# START OF USER VARIABLES #

# Variables for User Options
u_empid = StringVar()
u_pwd = StringVar()
u_groups = StringVar()
u_tel = StringVar()
u_email = StringVar()
u_mob = StringVar()
u_fax = StringVar()
u_title = StringVar()
u_dept = StringVar()
u_comp = StringVar()
u_mgr = StringVar()
u_homedir = StringVar()
u_homedrv = StringVar()
u_profile = StringVar()
u_logonscript = StringVar()
u_mustchgpwd = StringVar()
u_canchgpwd = StringVar()
u_pwdneverexp = StringVar()
u_acctexp = StringVar()
u_acctdisabled = StringVar()

# User filter checkbox variables
u_firstnamechkbox = IntVar()
u_lastnamechkbox = IntVar()
u_empidchkbox = IntVar()
u_pwdchkbox = IntVar()
u_groupschkbox = IntVar()
u_telchkbox = IntVar()
u_emailchkbox = IntVar()
u_mobchkbox = IntVar()
u_faxchkbox = IntVar()
u_titlechkbox = IntVar()
u_deptchkbox = IntVar()
u_compchkbox = IntVar()
u_mgrchkbox = IntVar()
u_homedirchkbox = IntVar()
u_homedrvchkbox = IntVar()
u_profilechkbox = IntVar()
u_logonscriptchkbox = IntVar()
u_mustchgpwdchkbox = IntVar()
u_canchgpwdchkbox = IntVar()
u_pwdneverexpchkbox = IntVar()
u_acctexpchkbox = IntVar()
u_acctdisabledchkbox = IntVar()


# User filter checkbox reset
def reset_user_chkbox():
    u_firstnamechkbox.set("0")
    u_lastnamechkbox.set("0")
    u_empidchkbox.set("0")
    u_pwdchkbox.set("0")
    u_groupschkbox.set("0")
    u_telchkbox.set("0")
    u_emailchkbox.set("0")
    u_mobchkbox.set("0")
    u_faxchkbox.set("0")
    u_titlechkbox.set("0")
    u_deptchkbox.set("0")
    u_compchkbox.set("0")
    u_mgrchkbox.set("0")
    u_homedirchkbox.set("0")
    u_homedrvchkbox.set("0")
    u_profilechkbox.set("0")
    u_logonscriptchkbox.set("0")
    u_mustchgpwdchkbox.set("0")
    u_canchgpwdchkbox.set("0")
    u_pwdneverexpchkbox.set("0")
    u_acctexpchkbox.set("0")
    u_acctdisabledchkbox.set("0")


# END OF USER VARIABLES #

# START OF GROUP VARIABLES #

# Variables for Group Options
g_secgrp = StringVar()
g_scope = StringVar()
g_desc = StringVar()
g_groups = StringVar()
g_members = StringVar()

# Group filter checkbox variables
g_secgrpchkbox = IntVar()
g_scopechkbox = IntVar()
g_descchkbox = IntVar()
g_groupschkbox = IntVar()
g_memberschkbox = IntVar()


# Group filter checkbox reset
def reset_group_chkbox():
    g_secgrpchkbox.set("1")
    g_scopechkbox.set("0")
    g_descchkbox.set("0")
    g_groupschkbox.set("0")
    g_memberschkbox.set("0")


# END OF GROUP VARIABLES #

# START OF COMPUTER VARIABLES #

# Variables for Computer Options
c_desc = StringVar()
c_loc = StringVar()
c_groups = StringVar()

# Computer filter checkbox variables
c_descchkbox = IntVar()
c_locchkbox = IntVar()
c_groupschkbox = IntVar()


# Computer filter checkbox reset
def reset_computer_chkbox():
    c_descchkbox.set("0")
    c_locchkbox.set("0")
    c_groupschkbox.set("0")


# END OF COMPUTER VARIABLES #

# START OF COMPUTER VARIABLES #

# Variables for OU Options
o_desc = StringVar()

# OU filter checkbox variables
o_descchkbox = IntVar()


# OU filter checkbox reset
def reset_ou_chkbox():
    o_descchkbox.set("0")


# END OF OU VARIABLES #

def destroy_widgets():
    for widget in input_frame.winfo_children():
        widget.destroy()
    for widget in parameter_frame.winfo_children():
        widget.destroy()


def get_mode(event=None):
    print("Mode = " + mode.get())
    destroy_widgets()
    if mode.get() == "User":
        add_user(self=window)
    if mode.get() == "Group":
        add_group(self=window)
    if mode.get() == "Computer":
        add_computer(self=window)
    if mode.get() == "OU":
        add_ou(self=window)
    # if mode == "Contact":
    # add_contact(self=window)


# START OF USER FIELDS


def cr_u_empid():
    global empidlbl
    global empident
    if u_empidchkbox.get() == 1:
        empidlbl = Label(parameter_frame, text="Employee ID: ")
        empidlbl.pack(side=LEFT, padx=4, pady=2)
        empident = Entry(parameter_frame, width=15, textvariable=u_empid)
        empident.pack(side=LEFT, pady=2)
    elif u_empidchkbox.get() == 0:
        empidlbl.destroy()
        empident.destroy()


def cr_u_pwd():
    global pwdlbl
    global pwdent
    if u_pwdchkbox.get() == 1:
        pwdlbl = Label(parameter_frame, text="Password: ")
        pwdlbl.pack(side=LEFT, padx=4, pady=2)
        pwdent = Entry(parameter_frame, width=15, textvariable=u_pwd)
        pwdent.pack(side=LEFT, pady=2)
    elif u_pwdchkbox.get() == 0:
        pwdlbl.destroy()
        pwdent.destroy()


def cr_u_groups():
    global groupslbl
    global groupsent
    if u_groupschkbox.get() == 1:
        groupslbl = Label(parameter_frame, text="Groups: ")
        groupslbl.pack(side=LEFT, padx=4, pady=2)
        groupsent = Entry(parameter_frame, width=15, textvariable=u_groups)
        groupsent.pack(side=LEFT, pady=2)
    elif u_groupschkbox.get() == 0:
        groupslbl.destroy()
        groupsent.destroy()


def cr_u_tel():
    global tellbl
    global telent
    if u_telchkbox.get() == 1:
        tellbl = Label(parameter_frame, text="Telephone: ")
        tellbl.pack(side=LEFT, padx=4, pady=2)
        telent = Entry(parameter_frame, width=15, textvariable=u_tel)
        telent.pack(side=LEFT, pady=2)
    elif u_telchkbox.get() == 0:
        tellbl.destroy()
        telent.destroy()


def cr_u_email():
    global emaillbl
    global emailent
    if u_emailchkbox.get() == 1:
        emaillbl = Label(parameter_frame, text="Email: ")
        emaillbl.pack(side=LEFT, padx=4, pady=2)
        emailent = Entry(parameter_frame, width=15, textvariable=u_email)
        emailent.pack(side=LEFT, pady=2)
    elif u_emailchkbox.get() == 0:
        emaillbl.destroy()
        emailent.destroy()


def cr_u_mob():
    global moblbl
    global mobent
    if u_mobchkbox.get() == 1:
        moblbl = Label(parameter_frame, text="Mobile: ")
        moblbl.pack(side=LEFT, padx=4, pady=2)
        mobent = Entry(parameter_frame, width=15, textvariable=u_mob)
        mobent.pack(side=LEFT, pady=2)
    elif u_mobchkbox.get() == 0:
        moblbl.destroy()
        mobent.destroy()


def cr_u_fax():
    global faxlbl
    global faxent
    if u_faxchkbox.get() == 1:
        faxlbl = Label(parameter_frame, text="Fax: ")
        faxlbl.pack(side=LEFT, padx=4, pady=2)
        faxent = Entry(parameter_frame, width=15, textvariable=u_fax)
        faxent.pack(side=LEFT, pady=2)
    elif u_faxchkbox.get() == 0:
        faxlbl.destroy()
        faxent.destroy()


def cr_u_title():
    global titlelbl
    global titleent
    if u_titlechkbox.get() == 1:
        titlelbl = Label(parameter_frame, text="Title: ")
        titlelbl.pack(side=LEFT, padx=4, pady=2)
        titleent = Entry(parameter_frame, width=15, textvariable=u_title)
        titleent.pack(side=LEFT, pady=2)
    elif u_titlechkbox.get() == 0:
        titlelbl.destroy()
        titleent.destroy()


def cr_u_dept():
    global deptlbl
    global deptent
    if u_deptchkbox.get() == 1:
        deptlbl = Label(parameter_frame, text="Department: ")
        deptlbl.pack(side=LEFT, padx=4, pady=2)
        deptent = Entry(parameter_frame, width=15, textvariable=u_dept)
        deptent.pack(side=LEFT, pady=2)
    elif u_deptchkbox.get() == 0:
        deptlbl.destroy()
        deptent.destroy()


def cr_u_comp():
    global complbl
    global compent
    if u_compchkbox.get() == 1:
        complbl = Label(parameter_frame, text="Company: ")
        complbl.pack(side=LEFT, padx=4, pady=2)
        compent = Entry(parameter_frame, width=15, textvariable=u_comp)
        compent.pack(side=LEFT, pady=2)
    elif u_compchkbox.get() == 0:
        complbl.destroy()
        compent.destroy()


def cr_u_mgr():
    global mgrlbl
    global mgrent
    if u_mgrchkbox.get() == 1:
        mgrlbl = Label(parameter_frame, text="Manager: ")
        mgrlbl.pack(side=LEFT, padx=4, pady=2)
        mgrent = Entry(parameter_frame, width=15, textvariable=u_mgr)
        mgrent.pack(side=LEFT, pady=2)
    elif u_mgrchkbox.get() == 0:
        mgrlbl.destroy()
        mgrent.destroy()


def cr_u_homedir():
    global homedirlbl
    global homedirent
    if u_homedirchkbox.get() == 1:
        homedirlbl = Label(parameter_frame, text="Home Directory: ")
        homedirlbl.pack(side=LEFT, padx=4, pady=2)
        homedirent = Entry(parameter_frame, width=15, textvariable=u_homedir)
        homedirent.pack(side=LEFT, pady=2)
    elif u_homedirchkbox.get() == 0:
        homedirlbl.destroy()
        homedirent.destroy()


def cr_u_homedrv():
    global homedrvlbl
    global homedrvent
    if u_homedrvchkbox.get() == 1:
        homedrvlbl = Label(parameter_frame, text="Home Drive: ")
        homedrvlbl.pack(side=LEFT, padx=4, pady=2)
        homedrvent = Entry(parameter_frame, width=15, textvariable=u_homedrv)
        homedrvent.pack(side=LEFT, pady=2)
    elif u_homedrvchkbox.get() == 0:
        homedrvlbl.destroy()
        homedrvent.destroy()


def cr_u_profile():
    global profilelbl
    global profileent
    if u_profilechkbox.get() == 1:
        profilelbl = Label(parameter_frame, text="Profile: ")
        profilelbl.pack(side=LEFT, padx=4, pady=2)
        profileent = Entry(parameter_frame, width=15, textvariable=u_profile)
        profileent.pack(side=LEFT, pady=2)
    elif u_profilechkbox.get() == 0:
        profilelbl.destroy()
        profileent.destroy()


def cr_u_logonscript():
    global logonscriptlbl
    global logonscriptent
    if u_logonscriptchkbox.get() == 1:
        logonscriptlbl = Label(parameter_frame, text="Logon Script: ")
        logonscriptlbl.pack(side=LEFT, padx=4, pady=2)
        logonscriptent = Entry(parameter_frame, width=15, textvariable=u_logonscript)
        logonscriptent.pack(side=LEFT, pady=2)
    elif u_logonscriptchkbox.get() == 0:
        logonscriptlbl.destroy()
        logonscriptent.destroy()


def cr_u_acctexp():
    global acctexplbl
    global acctexpent
    if u_acctexpchkbox.get() == 1:
        acctexplbl = Label(parameter_frame, text="Account Expires (days): ")
        acctexplbl.pack(side=LEFT, padx=4, pady=2)
        acctexpent = Entry(parameter_frame, width=15, textvariable=u_acctexp)
        acctexpent.pack(side=LEFT, pady=2)
    elif u_acctexpchkbox.get() == 0:
        acctexplbl.destroy()
        acctexpent.destroy()


# END OF USER FIELDS #

# START OF GROUP FIELDS #


def cr_g_scope():
    global scopelbl
    global scopecb
    if g_scopechkbox.get() == 1:
        scopelbl = Label(parameter_frame, text="Scope: ")
        scopelbl.pack(side=LEFT, padx=4, pady=2)
        scopecb = ttk.Combobox(parameter_frame, state="readonly", values=["Domain Local", "Global", "Universal"],
                               textvariable=g_scope, width=10)
        scopecb.current(1)
        scopecb.pack(side=LEFT, padx=4, pady=2)
    elif g_scopechkbox.get() == 0:
        scopelbl.destroy()
        scopecb.destroy()


def cr_g_desc():
    global desclbl
    global descent
    if g_descchkbox.get() == 1:
        desclbl = Label(parameter_frame, text="Description: ")
        desclbl.pack(side=LEFT, padx=4, pady=2)
        descent = Entry(parameter_frame, width=15, textvariable=g_desc)
        descent.pack(side=LEFT, pady=2)
    elif g_descchkbox.get() == 0:
        desclbl.destroy()
        descent.destroy()


def cr_g_groups():
    global groupslbl
    global groupsent
    if g_groupschkbox.get() == 1:
        groupslbl = Label(parameter_frame, text="Groups: ")
        groupslbl.pack(side=LEFT, padx=4, pady=2)
        groupsent = Entry(parameter_frame, width=15, textvariable=g_groups)
        groupsent.pack(side=LEFT, pady=2)
    elif g_groupschkbox.get() == 0:
        groupslbl.destroy()
        groupsent.destroy()


def cr_g_members():
    global memberslbl
    global membersent
    if g_memberschkbox.get() == 1:
        memberslbl = Label(parameter_frame, text="Members: ")
        memberslbl.pack(side=LEFT, padx=4, pady=2)
        membersent = Entry(parameter_frame, width=15, textvariable=g_members)
        membersent.pack(side=LEFT, pady=2)
    elif g_memberschkbox.get() == 0:
        memberslbl.destroy()
        membersent.destroy()


# END OF GROUP FIELDS #

# START OF COMPUTER FIELDS #

def cr_c_desc():
    global desclbl
    global descent
    if c_descchkbox.get() == 1:
        desclbl = Label(parameter_frame, text="Description: ")
        desclbl.pack(side=LEFT, padx=4, pady=2)
        descent = Entry(parameter_frame, width=15, textvariable=c_desc)
        descent.pack(side=LEFT, pady=2)
    elif c_descchkbox.get() == 0:
        desclbl.destroy()
        descent.destroy()


def cr_c_loc():
    global loclbl
    global locent
    if c_locchkbox.get() == 1:
        loclbl = Label(parameter_frame, text="Location: ")
        loclbl.pack(side=LEFT, padx=4, pady=2)
        locent = Entry(parameter_frame, width=15, textvariable=c_loc)
        locent.pack(side=LEFT, pady=2)
    elif c_locchkbox.get() == 0:
        loclbl.destroy()
        locent.destroy()


def cr_c_groups():
    global groupslbl
    global groupsent
    if c_groupschkbox.get() == 1:
        groupslbl = Label(parameter_frame, text="Groups: ")
        groupslbl.pack(side=LEFT, padx=4, pady=2)
        groupsent = Entry(parameter_frame, width=15, textvariable=c_groups)
        groupsent.pack(side=LEFT, pady=2)
    elif c_groupschkbox.get() == 0:
        groupslbl.destroy()
        groupsent.destroy()


# END OF COMPUTER FIELDS #

# START OF OU FIELDS #


def cr_o_desc():
    global desclbl
    global descent
    if o_descchkbox.get() == 1:
        desclbl = Label(parameter_frame, text="Description: ")
        desclbl.pack(side=LEFT, padx=4, pady=2)
        descent = Entry(parameter_frame, width=15, textvariable=o_desc)
        descent.pack(side=LEFT, pady=2)
    elif o_descchkbox.get() == 0:
        desclbl.destroy()
        descent.destroy()


# END OF OU FIELDS #

# START OF USER OPTIONS WINDOW #


def user_options_window():
    window.wm_attributes("-disabled", True)

    options = Toplevel()
    options.title("DSADD User Options")
    options.geometry("500x450")
    options.resizable(0, 0)
    optionsframe = Frame(options)
    optionsframe.pack()
    options_bottomframe = Frame(options)
    options_bottomframe.pack()

    selparamlbl = Label(optionsframe, text="Select parameters:")
    selparamlbl.grid(sticky="w", row=0, column=0, pady=10)
    firstnamechk = Checkbutton(optionsframe, text="First Name", variable=u_firstnamechkbox)
    firstnamechk.grid(sticky="w", row=1, column=0, padx=10, pady=2)
    lastnamechk = Checkbutton(optionsframe, text="Last Name", variable=u_lastnamechkbox)
    lastnamechk.grid(sticky="w", row=2, column=0, padx=10, pady=2)
    employeeidchk = Checkbutton(optionsframe, text="Employee ID", variable=u_empidchkbox, command=cr_u_empid)
    employeeidchk.grid(sticky="w", row=3, column=0, padx=10, pady=2)
    passwordchk = Checkbutton(optionsframe, text="Password", variable=u_pwdchkbox, command=cr_u_pwd)
    passwordchk.grid(sticky="w", row=4, column=0, padx=10, pady=2)
    groupchk = Checkbutton(optionsframe, text="Groups", variable=u_groupschkbox, command=cr_u_groups)
    groupchk.grid(sticky="w", row=5, column=0, padx=10, pady=2)
    telchk = Checkbutton(optionsframe, text="Telephone", variable=u_telchkbox, command=cr_u_tel)
    telchk.grid(sticky="w", row=6, column=0, padx=10, pady=2)
    emailchk = Checkbutton(optionsframe, text="Email", variable=u_emailchkbox, command=cr_u_email)
    emailchk.grid(sticky="w", row=7, column=0, padx=10, pady=2)
    mobilechk = Checkbutton(optionsframe, text="Mobile", variable=u_mobchkbox, command=cr_u_mob)
    mobilechk.grid(sticky="w", row=8, column=0, padx=10, pady=2)
    faxchk = Checkbutton(optionsframe, text="Fax", variable=u_faxchkbox, command=cr_u_fax)
    faxchk.grid(sticky="w", row=9, column=0, padx=10, pady=2)
    titlechk = Checkbutton(optionsframe, text="Title", variable=u_titlechkbox, command=cr_u_title)
    titlechk.grid(sticky="w", row=10, column=0, padx=10, pady=2)
    deptchk = Checkbutton(optionsframe, text="Department", variable=u_deptchkbox, command=cr_u_dept)
    deptchk.grid(sticky="w", row=11, column=0, padx=10, pady=2)
    companychk = Checkbutton(optionsframe, text="Company", variable=u_compchkbox, command=cr_u_comp)
    companychk.grid(sticky="w", row=1, column=2, padx=10, pady=2)
    managerchk = Checkbutton(optionsframe, text="Manager", variable=u_mgrchkbox, command=cr_u_mgr)
    managerchk.grid(sticky="w", row=2, column=2, padx=10, pady=2)
    homedirchk = Checkbutton(optionsframe, text="Home Directory", variable=u_homedirchkbox, command=cr_u_homedir)
    homedirchk.grid(sticky="w", row=3, column=2, padx=10, pady=2)
    homedrivechk = Checkbutton(optionsframe, text="Home Directory Drive", variable=u_homedrvchkbox,
                               command=cr_u_homedrv)
    homedrivechk.grid(sticky="w", row=4, column=2, padx=10, pady=2)
    profilechk = Checkbutton(optionsframe, text="Profile Path", variable=u_profilechkbox, command=cr_u_profile)
    profilechk.grid(sticky="w", row=5, column=2, padx=10, pady=2)
    logonpathchk = Checkbutton(optionsframe, text="Logon Script Path", variable=u_logonscriptchkbox,
                               command=cr_u_logonscript)
    logonpathchk.grid(sticky="w", row=6, column=2, padx=10, pady=2)
    mustchpwdchk = Checkbutton(optionsframe, text="Must Change Password", variable=u_mustchgpwdchkbox)
    mustchpwdchk.grid(sticky="w", row=7, column=2, padx=10, pady=2)
    canchpwdchk = Checkbutton(optionsframe, text="Can Change Password", variable=u_canchgpwdchkbox)
    canchpwdchk.grid(sticky="w", row=8, column=2, padx=10, pady=2)
    pwdneverexpchk = Checkbutton(optionsframe, text="Password Never Expires", variable=u_pwdneverexpchkbox)
    pwdneverexpchk.grid(sticky="w", row=9, column=2, padx=10, pady=2)
    accountexpchk = Checkbutton(optionsframe, text="Account Expires", variable=u_acctexpchkbox, command=cr_u_acctexp)
    accountexpchk.grid(sticky="w", row=10, column=2, padx=10, pady=2)
    disabledchk = Checkbutton(optionsframe, text="Disabled", variable=u_acctdisabledchkbox)
    disabledchk.grid(sticky="w", row=11, column=2, padx=10, pady=2)

    def close_options_btn():
        window.wm_attributes("-disabled", False)
        options.destroy()

    optionsclosebtn = Button(options_bottomframe, width=15, text="Close", command=close_options_btn)
    optionsclosebtn.pack(pady=15)


# END OF USER OPTIONS WINDOW #

# START OF GROUP OPTIONS WINDOW #

def group_options_window():
    window.wm_attributes("-disabled", True)

    options = Toplevel()
    options.title("DSADD Group Options")
    options.geometry("300x250")
    options.resizable(0, 0)
    optionsframe = Frame(options)
    optionsframe.pack()
    options_bottomframe = Frame(options)
    options_bottomframe.pack()

    selparamlbl = Label(optionsframe, text="Select parameters:")
    selparamlbl.grid(sticky="w", row=0, column=0, pady=10)
    secgrpchk = Checkbutton(optionsframe, text="Security Group", variable=g_secgrpchkbox)
    secgrpchk.grid(sticky="w", row=1, column=0, padx=10, pady=2)
    scopechk = Checkbutton(optionsframe, text="Scope", variable=g_scopechkbox, command=cr_g_scope)
    scopechk.grid(sticky="w", row=2, column=0, padx=10, pady=2)
    descchk = Checkbutton(optionsframe, text="Description", variable=g_descchkbox, command=cr_g_desc)
    descchk.grid(sticky="w", row=3, column=0, padx=10, pady=2)
    groupchk = Checkbutton(optionsframe, text="Groups", variable=g_groupschkbox, command=cr_g_groups)
    groupchk.grid(sticky="w", row=4, column=0, padx=10, pady=2)
    memberschk = Checkbutton(optionsframe, text="Members", variable=g_memberschkbox, command=cr_g_members)
    memberschk.grid(sticky="w", row=5, column=0, padx=10, pady=2)

    def close_options_btn():
        window.wm_attributes("-disabled", False)
        options.destroy()

    optionsclosebtn = Button(options_bottomframe, width=15, text="Close", command=close_options_btn)
    optionsclosebtn.pack(pady=15)


# END OF GROUP OPTIONS WINDOW #

# START OF COMPUTER OPTIONS WINDOW #

def computer_options_window():
    window.wm_attributes("-disabled", True)

    options = Toplevel()
    options.title("DSADD Computer Options")
    options.geometry("300x250")
    options.resizable(0, 0)
    optionsframe = Frame(options)
    optionsframe.pack()
    options_bottomframe = Frame(options)
    options_bottomframe.pack()

    selparamlbl = Label(optionsframe, text="Select parameters:")
    selparamlbl.grid(sticky="w", row=0, column=0, pady=10)
    descchk = Checkbutton(optionsframe, text="Description", variable=c_descchkbox, command=cr_c_desc)
    descchk.grid(sticky="w", row=1, column=0, padx=10, pady=2)
    locchk = Checkbutton(optionsframe, text="Location", variable=c_locchkbox, command=cr_c_loc)
    locchk.grid(sticky="w", row=2, column=0, padx=10, pady=2)
    groupchk = Checkbutton(optionsframe, text="Groups", variable=c_groupschkbox, command=cr_c_groups)
    groupchk.grid(sticky="w", row=4, column=0, padx=10, pady=2)

    def close_options_btn():
        window.wm_attributes("-disabled", False)
        options.destroy()

    optionsclosebtn = Button(options_bottomframe, width=15, text="Close", command=close_options_btn)
    optionsclosebtn.pack(pady=15)


# END OF COMPUTER OPTIONS WINDOW #

# START OF OU OPTIONS WINDOW #

def ou_options_window():
    window.wm_attributes("-disabled", True)

    options = Toplevel()
    options.title("DSADD OU Options")
    options.geometry("300x250")
    options.resizable(0, 0)
    optionsframe = Frame(options)
    optionsframe.pack()
    options_bottomframe = Frame(options)
    options_bottomframe.pack()

    selparamlbl = Label(optionsframe, text="Select parameters:")
    selparamlbl.grid(sticky="w", row=0, column=0, pady=10)
    descchk = Checkbutton(optionsframe, text="Description", variable=o_descchkbox, command=cr_o_desc)
    descchk.grid(sticky="w", row=1, column=0, padx=10, pady=2)

    def close_options_btn():
        window.wm_attributes("-disabled", False)
        options.destroy()

    optionsclosebtn = Button(options_bottomframe, width=15, text="Close", command=close_options_btn)
    optionsclosebtn.pack(pady=15)


# END OF COMPUTER OPTIONS WINDOW #

def add_user(self):
    reset_user_chkbox()
    user_options_window()
    firstnamelbl = Label(input_frame, text="*First Name:")
    firstnamelbl.grid(row=0, column=0, padx=4, pady=2)
    self.firstnameent = Entry(input_frame, width=15, textvariable=firstname)
    self.firstnameent.grid(row=0, column=1, pady=2)
    lastnamelbl = Label(input_frame, text="*Last Name:")
    lastnamelbl.grid(row=0, column=2, padx=4, pady=2)
    lastnameent = Entry(input_frame, width=15, textvariable=lastname)
    lastnameent.grid(row=0, column=3, pady=2)
    orgunitlbl = Label(input_frame, text="Organisational Unit: ")
    orgunitlbl.grid(row=0, column=4, padx=4, pady=2)
    orgunitent = Entry(input_frame, width=15, textvariable=orgunit)
    orgunitent.grid(row=0, column=5, pady=2)
    domainlbl = Label(input_frame, text="*Domain Name:")
    domainlbl.grid(row=0, column=6, padx=4, pady=2)
    domainent = Entry(input_frame, width=15, textvariable=domain)
    domainent.grid(row=0, column=7, pady=2)


def add_group(self):
    reset_group_chkbox()
    group_options_window()
    groupnamelbl = Label(input_frame, text="*Group Name:")
    groupnamelbl.grid(row=0, column=0, padx=4, pady=2)
    self.groupnameent = Entry(input_frame, width=15, textvariable=groupname)
    self.groupnameent.grid(row=0, column=1, pady=2)
    orgunitlbl = Label(input_frame, text="Organisational Unit: ")
    orgunitlbl.grid(row=0, column=4, padx=4, pady=2)
    orgunitent = Entry(input_frame, width=15, textvariable=orgunit)
    orgunitent.grid(row=0, column=5, pady=2)
    domainlbl = Label(input_frame, text="*Domain Name:")
    domainlbl.grid(row=0, column=6, padx=4, pady=2)
    domainent = Entry(input_frame, width=15, textvariable=domain)
    domainent.grid(row=0, column=7, pady=2)


def add_computer(self):
    reset_computer_chkbox()
    computer_options_window()
    computernamelbl = Label(input_frame, text="*Computer Name:")
    computernamelbl.grid(row=0, column=0, padx=4, pady=2)
    self.computernameent = Entry(input_frame, width=15, textvariable=computername)
    self.computernameent.grid(row=0, column=1, pady=2)
    orgunitlbl = Label(input_frame, text="Organisational Unit: ")
    orgunitlbl.grid(row=0, column=4, padx=4, pady=2)
    orgunitent = Entry(input_frame, width=15, textvariable=orgunit)
    orgunitent.grid(row=0, column=5, pady=2)
    domainlbl = Label(input_frame, text="*Domain Name:")
    domainlbl.grid(row=0, column=6, padx=4, pady=2)
    domainent = Entry(input_frame, width=15, textvariable=domain)
    domainent.grid(row=0, column=7, pady=2)


def add_ou(self):
    reset_ou_chkbox()
    ou_options_window()
    ounamelbl = Label(input_frame, text="*OU Name:")
    ounamelbl.grid(row=0, column=0, padx=4, pady=2)
    self.ounameent = Entry(input_frame, width=15, textvariable=ouname)
    self.ounameent.grid(row=0, column=1, pady=2)
    domainlbl = Label(input_frame, text="*Domain Name:")
    domainlbl.grid(row=0, column=2, padx=4, pady=2)
    domainent = Entry(input_frame, width=15, textvariable=domain)
    domainent.grid(row=0, column=3, pady=2)


def submit_btn(self=window):
    # SUBMIT USER SETTINGS #

    if mode.get() == "User":
        # Main field variables
        login = firstname.get().lower().replace(" ", "") + lastname.get().lower().replace(" ", "")

        if orgunit.get() != "":
            ou = (",ou=" + orgunit.get())
        else:
            ou = ""

        domainlist = domain.get().split(".")
        domaininput1 = (",dc=" + domainlist[0])
        domaininput2 = (",dc=" + domainlist[1])

        if len(domainlist) == 3:
            domaininput3 = (",dc=" + domainlist[2])
        else:
            domaininput3 = ""

        distinguishedname = '"cn=' + login + ou + domaininput1 + domaininput2 + domaininput3 + '"'

        # First Name variable
        if u_firstnamechkbox.get() == 1:
            fname = (" -fn " + firstname.get())
        else:
            fname = ""

        # Last Name variable
        if u_lastnamechkbox.get() == 1:
            lname = (" -ln " + lastname.get())
        else:
            lname = ""

        # Employee ID variable
        if u_empid.get() != "":
            empid = (" -empid " + u_empid.get())
        else:
            empid = ""

        # Password variable
        if u_pwd.get() != "":
            pwd = (" -pwd " + u_pwd.get())
        else:
            pwd = ""

        # Group variables
        if u_groups.get() == "":
            group1 = ""
            group2 = ""
            group3 = ""
        else:
            grouplist = u_groups.get().split(", ")
            group1 = (' -memberof "cn=' + grouplist[0] + domaininput1 + domaininput2 + domaininput3 + '"')

            if len(grouplist) == 2:
                group2 = (' "cn=' + grouplist[1] + domaininput1 + domaininput2 + domaininput3 + '"')
            else:
                group2 = ""

            if len(grouplist) == 3:
                group2 = (' "cn=' + grouplist[1] + domaininput1 + domaininput2 + domaininput3 + '"')
                group3 = (' "cn=' + grouplist[2] + domaininput1 + domaininput2 + domaininput3 + '"')
            else:
                group3 = ""

        # Telephone variable
        if u_tel.get() != "":
            tel = (" -tel " + u_tel.get().replace(" ", ""))
        else:
            tel = ""

        # Email variable
        if u_email.get() != "":
            email = (" -email " + u_email.get())
        else:
            email = ""

        # Mobile variable
        if u_mob.get() != "":
            mob = (" -mob " + u_mob.get().replace(" ", ""))
        else:
            mob = ""

        # Fax variable
        if u_fax.get() != "":
            fax = (" -fax " + u_fax.get().replace(" ", ""))
        else:
            fax = ""

        # Title variable
        if u_title.get() != "":
            title = (" -title " + u_title.get())
        else:
            title = ""

        # Department variable
        if u_dept.get() != "":
            dept = (" -dept " + u_dept.get())
        else:
            dept = ""

        # Company variable
        if u_comp.get() != "":
            company = (" -company " + u_comp.get())
        else:
            company = ""

        # Manager variable
        if u_mgr.get() != "":
            mgr = (' -mgr "cn=' + u_mgr.get() + domaininput1 + domaininput2 + domaininput3 + '"')
        else:
            mgr = ""

        # Home directory variable
        if u_homedir.get() != "":
            if " " in u_homedir.get():
                homedir = (' -hmdir "' + u_homedir.get() + '"')
            else:
                homedir = (' -hmdir ' + u_homedir.get())
        else:
            homedir = ""

        # Home drive variable
        if r"\\" in u_homedir.get():
            homedrv = (' -hmdrv ' + u_homedrv.get())
        else:
            homedrv = ""

        # Profile path variable
        if u_profile.get() != "":
            if " " in u_profile.get():
                profile = (' -profile "' + u_profile.get() + '"')
            else:
                profile = (" -profile " + u_profile.get())
        else:
            profile = ""

        # Logon script variable
        if u_logonscript.get() != "":
            if " " in u_logonscript.get():
                loscr = (' -loscr "' + u_logonscript.get() + '"')
            else:
                loscr = (" -loscr " + u_logonscript.get())
        else:
            loscr = ""

        # Must change password variable
        if u_mustchgpwdchkbox.get() == 1:
            mustchgpwd = " -mustchgpwd yes"
        else:
            mustchgpwd = ""

        # Can change password variable
        if u_mustchgpwdchkbox.get() == 1:
            canchgpwd = " -canchgpwd yes"
        elif u_canchgpwdchkbox.get() == 1:
            canchgpwd = " -canchgpwd yes"
        else:
            canchgpwd = ""

        # Password never expires variable
        if u_pwdneverexp.get() == 1:
            pwdneverexp = " -pwdneverexpires yes"
        else:
            pwdneverexp = ""

        # Account expires variable
        if u_acctexpchkbox.get() == 1:
            acctexp = (" -acctexpires " + u_acctexp.get())
        else:
            acctexp = ""

        # Account disabled variable
        if u_acctdisabledchkbox.get() == 1:
            acctdisabled = " -disabled yes"
        else:
            acctdisabled = " -disabled no"

        txtbox.insert(END, "dsadd user " + distinguishedname)
        txtbox.insert(END, fname + lname + empid + pwd + group1 + group2 + group3 + tel + email + mob + fax + title +
                      dept + company + mgr + homedir + homedrv + profile + loscr + mustchgpwd + canchgpwd + pwdneverexp
                      + acctexp + acctdisabled + "\n")

    # SUBMIT GROUP SETTINGS #

    if mode.get() == "Group":
        # Main field variables
        group = groupname.get()

        if orgunit.get() != "":
            ou = (",ou=" + orgunit.get())
        else:
            ou = ""

        domainlist = domain.get().split(".")
        domaininput1 = (",dc=" + domainlist[0])
        domaininput2 = (",dc=" + domainlist[1])

        if len(domainlist) == 3:
            domaininput3 = (",dc=" + domainlist[2])
        else:
            domaininput3 = ""

        distinguishedname = '"cn=' + group + ou + domaininput1 + domaininput2 + domaininput3 + '"'

        # Security group variable
        if g_secgrpchkbox.get() == 0:
            secgrp = " -secgrp no"
        else:
            secgrp = ""

        # Scope variable
        if g_scope.get() == "Domain Local":
            scope = " -scope l"
        elif g_scope.get() == "Global":
            scope = " -scope g"
        elif g_scope.get() == "Universal":
            scope = " -scope u"
        else:
            scope = ""

        # Description variable
        if g_desc.get() != "":
            desc = ' -desc "' + g_desc.get() + '"'
        else:
            desc = ""

        # Group variables
        grouplist = g_groups.get().split(", ")

        if len(grouplist) == 1:
            group1 = ' -memberof "cn=' + grouplist[0] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            group2 = ""
            group3 = ""
            group4 = ""
        elif len(grouplist) == 2:
            group1 = ' -memberof "cn=' + grouplist[0] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            group2 = ' "cn=' + grouplist[1] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            group3 = ""
            group4 = ""
        elif len(grouplist) == 3:
            group1 = ' -memberof "cn=' + grouplist[0] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            group2 = ' "cn=' + grouplist[1] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            group3 = ' "cn=' + grouplist[2] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            group4 = ""
        elif len(grouplist) == 4:
            group1 = ' -memberof "cn=' + grouplist[0] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            group2 = ' "cn=' + grouplist[1] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            group3 = ' "cn=' + grouplist[2] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            group4 = ' "cn=' + grouplist[3] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
        else:
            group1 = ""
            group2 = ""
            group3 = ""
            group4 = ""

        # Members variables
        memberlist = g_members.get().split(", ")

        if len(memberlist) == 1:
            member1 = ' -member "cn=' + memberlist[0] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member2 = ""
            member3 = ""
            member4 = ""
            member5 = ""
            member6 = ""
            member7 = ""
            member8 = ""
            member9 = ""
            member10 = ""
        elif len(memberlist) == 2:
            member1 = ' -member "cn=' + memberlist[0] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member2 = ' "cn=' + memberlist[1] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member3 = ""
            member4 = ""
            member5 = ""
            member6 = ""
            member7 = ""
            member8 = ""
            member9 = ""
            member10 = ""
        elif len(memberlist) == 3:
            member1 = ' -member "cn=' + memberlist[0] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member2 = ' "cn=' + memberlist[1] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member3 = ' "cn=' + memberlist[2] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member4 = ""
            member5 = ""
            member6 = ""
            member7 = ""
            member8 = ""
            member9 = ""
            member10 = ""
        elif len(memberlist) == 4:
            member1 = ' -member "cn=' + memberlist[0] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member2 = ' "cn=' + memberlist[1] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member3 = ' "cn=' + memberlist[2] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member4 = ' "cn=' + memberlist[3] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member5 = ""
            member6 = ""
            member7 = ""
            member8 = ""
            member9 = ""
            member10 = ""
        elif len(memberlist) == 5:
            member1 = ' -member "cn=' + memberlist[0] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member2 = ' "cn=' + memberlist[1] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member3 = ' "cn=' + memberlist[2] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member4 = ' "cn=' + memberlist[3] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member5 = ' "cn=' + memberlist[4] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member6 = ""
            member7 = ""
            member8 = ""
            member9 = ""
            member10 = ""
        elif len(memberlist) == 6:
            member1 = ' -member "cn=' + memberlist[0] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member2 = ' "cn=' + memberlist[1] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member3 = ' "cn=' + memberlist[2] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member4 = ' "cn=' + memberlist[3] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member5 = ' "cn=' + memberlist[4] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member6 = ' "cn=' + memberlist[5] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member7 = ""
            member8 = ""
            member9 = ""
            member10 = ""
        elif len(memberlist) == 7:
            member1 = ' -member "cn=' + memberlist[0] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member2 = ' "cn=' + memberlist[1] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member3 = ' "cn=' + memberlist[2] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member4 = ' "cn=' + memberlist[3] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member5 = ' "cn=' + memberlist[4] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member6 = ' "cn=' + memberlist[5] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member7 = ' "cn=' + memberlist[6] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member8 = ""
            member9 = ""
            member10 = ""
        elif len(memberlist) == 8:
            member1 = ' -member "cn=' + memberlist[0] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member2 = ' "cn=' + memberlist[1] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member3 = ' "cn=' + memberlist[2] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member4 = ' "cn=' + memberlist[3] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member5 = ' "cn=' + memberlist[4] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member6 = ' "cn=' + memberlist[5] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member7 = ' "cn=' + memberlist[6] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member8 = ' "cn=' + memberlist[7] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member9 = ""
            member10 = ""
        elif len(memberlist) == 9:
            member1 = ' -member "cn=' + memberlist[0] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member2 = ' "cn=' + memberlist[1] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member3 = ' "cn=' + memberlist[2] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member4 = ' "cn=' + memberlist[3] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member5 = ' "cn=' + memberlist[4] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member6 = ' "cn=' + memberlist[5] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member7 = ' "cn=' + memberlist[6] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member8 = ' "cn=' + memberlist[7] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member9 = ' "cn=' + memberlist[8] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member10 = ""
        elif len(memberlist) == 10:
            member1 = ' -member "cn=' + memberlist[0] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member2 = ' "cn=' + memberlist[1] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member3 = ' "cn=' + memberlist[2] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member4 = ' "cn=' + memberlist[3] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member5 = ' "cn=' + memberlist[4] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member6 = ' "cn=' + memberlist[5] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member7 = ' "cn=' + memberlist[6] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member8 = ' "cn=' + memberlist[7] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member9 = ' "cn=' + memberlist[8] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            member10 = ' "cn=' + memberlist[9] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
        else:
            member1 = ""
            member2 = ""
            member3 = ""
            member4 = ""
            member5 = ""
            member6 = ""
            member7 = ""
            member8 = ""
            member9 = ""
            member10 = ""

        txtbox.insert(END, "dsadd group " + distinguishedname)
        txtbox.insert(END, secgrp + scope + desc + group1 + group2 + group3 + group4 + member1 + member2 +
                      member3 + member4 + member5 + member6 + member7 + member8 + member9 + member10 + "\n")

    # SUBMIT COMPUTER SETTINGS #

    if mode.get() == "Computer":
        # Main field variables
        computer = computername.get()

        if orgunit.get() != "":
            ou = (",ou=" + orgunit.get())
        else:
            ou = ""

        domainlist = domain.get().split(".")
        domaininput1 = (",dc=" + domainlist[0])
        domaininput2 = (",dc=" + domainlist[1])

        if len(domainlist) == 3:
            domaininput3 = (",dc=" + domainlist[2])
        else:
            domaininput3 = ""

        distinguishedname = '"cn=' + computer + ou + domaininput1 + domaininput2 + domaininput3 + '"'

        # Description variable
        if c_desc.get() != "":
            desc = ' -desc "' + c_desc.get() + '"'
        else:
            desc = ""

        # Location variable
        if c_loc.get() != "":
            loc = ' -loc "' + c_loc.get() + '"'
        else:
            loc = ""

        # Group variables
        grouplist = g_groups.get().split(", ")

        if len(grouplist) == 1:
            group1 = ' -memberof "cn=' + grouplist[0] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            group2 = ""
            group3 = ""
            group4 = ""
        elif len(grouplist) == 2:
            group1 = ' -memberof "cn=' + grouplist[0] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            group2 = ' "cn=' + grouplist[1] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            group3 = ""
            group4 = ""
        elif len(grouplist) == 3:
            group1 = ' -memberof "cn=' + grouplist[0] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            group2 = ' "cn=' + grouplist[1] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            group3 = ' "cn=' + grouplist[2] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            group4 = ""
        elif len(grouplist) == 4:
            group1 = ' -memberof "cn=' + grouplist[0] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            group2 = ' "cn=' + grouplist[1] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            group3 = ' "cn=' + grouplist[2] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
            group4 = ' "cn=' + grouplist[3] + ou + domaininput1 + domaininput2 + domaininput3 + '"'
        else:
            group1 = ""
            group2 = ""
            group3 = ""
            group4 = ""

        txtbox.insert(END, "dsadd computer " + distinguishedname)
        txtbox.insert(END, desc + loc + group1 + group2 + group3 + group4 + "\n")

    # SUBMIT OU SETTINGS #

    if mode.get() == "OU":
        ou = ouname.get()

        domainlist = domain.get().split(".")
        domaininput1 = (",dc=" + domainlist[0])
        domaininput2 = (",dc=" + domainlist[1])

        if len(domainlist) == 3:
            domaininput3 = (",dc=" + domainlist[2])
        else:
            domaininput3 = ""

        distinguishedname = '"ou=' + ou + domaininput1 + domaininput2 + domaininput3 + '"'

        # Description variable
        if o_desc.get() != "":
            desc = ' -desc "' + o_desc.get() + '"'
        else:
            desc = ""

        txtbox.insert(END, "dsadd ou " + distinguishedname)
        txtbox.insert(END, desc + "\n")

    clrentry_btn()

    if mode.get() == "User":
        self.firstnameent.focus_set()
    if mode.get() == "Group":
        self.groupnameent.focus_set()
    if mode.get() == "Computer":
        self.computernameent.focus_set()
    if mode.get() == "OU":
        self.ounameent.focus_set()


def copy_btn():
    global s
    window.clipboard_clear()
    window.clipboard_append(txtbox.get(1.0, END))
    s.set("Copied to clipboard")


def imp_btn():
    global s
    with open(filedialog.askopenfilename()) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        next(csv_file)

        # START OF USER IMPORT SETTINGS #

        if mode.get() == "User":
            for row in csv_reader:
                name = row[0].lower()
                login = name.replace(" ", "")
                print(login)

                if row[1] != "":
                    ou = (",ou=" + row[1])
                else:
                    ou = ""

                domainlist = row[2].split(".")
                domaininput1 = (",dc=" + domainlist[0])
                domaininput2 = (",dc=" + domainlist[1])

                if len(domainlist) == 3:
                    domaininput3 = (",dc=" + domainlist[2])
                else:
                    domaininput3 = ""

                distinguishedname = '"cn=' + login + ou + domaininput1 + domaininput2 + domaininput3 + '"'

                # Employee ID variable
                if row[3] != "":
                    empid = (" -empid " + row[3])
                else:
                    empid = ""

                # Password variable
                if row[4] != "":
                    pwd = (" -pwd " + row[4])
                else:
                    pwd = ""

                # Group variables
                if row[5] == "":
                    group1 = ""
                    group2 = ""
                    group3 = ""
                else:
                    grouplist = row[5].split(", ")
                    group1 = (' -memberof "cn=' + grouplist[0] + domaininput1 + domaininput2 + domaininput3 + '"')

                    if len(grouplist) == 2:
                        group2 = (' "cn=' + grouplist[1] + domaininput1 + domaininput2 + domaininput3 + '"')
                    else:
                        group2 = ""

                    if len(grouplist) == 3:
                        group2 = (' "cn=' + grouplist[1] + domaininput1 + domaininput2 + domaininput3 + '"')
                        group3 = (' "cn=' + grouplist[2] + domaininput1 + domaininput2 + domaininput3 + '"')
                    else:
                        group3 = ""

                # Telephone variable
                if row[6] != "":
                    tel = (" -tel " + row[6].replace(" ", ""))
                else:
                    tel = ""

                # Email variable
                if row[7] != "":
                    email = (" -email " + row[7])
                else:
                    email = ""

                # Mobile variable
                if row[8] != "":
                    mob = (" -mob " + row[8].replace(" ", ""))
                else:
                    mob = ""

                # Fax variable
                if row[9] != "":
                    fax = (" -fax " + row[9].replace(" ", ""))
                else:
                    fax = ""

                # Title variable
                if row[10] != "":
                    title = (" -title " + row[10])
                else:
                    title = ""

                # Department variable
                if row[11] != "":
                    dept = (" -dept " + row[11])
                else:
                    dept = ""

                # Company variable
                if row[12] != "":
                    company = (" -company " + row[12])
                else:
                    company = ""

                # Manager variable
                if row[13] != "":
                    mgr = (' -mgr "cn=' + row[13] + domaininput1 + domaininput2 + domaininput3 + '"')
                else:
                    mgr = ""

                # Home directory variable
                if row[14] != "":
                    if " " in row[14]:
                        homedir = (' -hmdir "' + row[14] + '"')
                    else:
                        homedir = (' -hmdir ' + row[14])
                else:
                    homedir = ""

                # Home drive variable
                if r"\\" in row[14]:
                    homedrv = (' -hmdrv ' + row[15])
                else:
                    homedrv = ""

                # Profile path variable
                if row[16] != "":
                    if " " in row[16]:
                        profile = (' -profile "' + row[16] + '"')
                    else:
                        profile = (" -profile " + row[16])
                else:
                    profile = ""

                # Logon script variable
                if row[17] != "":
                    if " " in row[17]:
                        loscr = (' -loscr "' + row[17] + '"')
                    else:
                        loscr = (" -loscr " + row[17])
                else:
                    loscr = ""

                # Must change password variable
                if row[18] == "yes":
                    mustchgpwd = " -mustchgpwd yes"
                else:
                    mustchgpwd = ""

                # Can change password variable
                if row[18] == "yes":
                    canchgpwd = " -canchgpwd yes"
                elif row[19] == "yes":
                    canchgpwd = " -canchgpwd yes"
                else:
                    canchgpwd = ""

                # Password never expires variable
                if row[20] == "yes":
                    pwdneverexp = " -pwdneverexpires yes"
                else:
                    pwdneverexp = ""

                # Account expires variable
                if row[21] == "yes":
                    acctexp = (" -acctexpires " + row[21])
                else:
                    acctexp = ""

                # Account disabled variable
                if row[22] == "yes":
                    acctdisabled = " -disabled yes"
                else:
                    acctdisabled = " -disabled no"

                txtbox.insert(END, 'dsadd user ' + distinguishedname + empid + pwd + group1 + group2 + group3 + tel
                              + email + mob + fax + title + dept + company + mgr + homedir + homedrv + profile + loscr
                              + mustchgpwd + canchgpwd + pwdneverexp + acctexp + acctdisabled + "\n")

                line_count += 1
            # print(f'Processed {line_count} lines.')
        s.set(f"Processed {line_count} lines")

        # END OF USER IMPORT SETTINGS #

        # START OF GROUP IMPORT SETTINGS #

        if mode.get() == "Group":
            for row in csv_reader:
                name = row[0]

                if row[1] != "":
                    ou = (",ou=" + row[1])
                else:
                    ou = ""

                domainlist = row[2].split(".")
                domaininput1 = (",dc=" + domainlist[0])
                domaininput2 = (",dc=" + domainlist[1])

                if len(domainlist) == 3:
                    domaininput3 = (",dc=" + domainlist[2])
                else:
                    domaininput3 = ""

                distinguishedname = '"cn=' + name + ou + domaininput1 + domaininput2 + domaininput3 + '"'

                # Security Group variable
                if row[3] != "":
                    secgrp = (" -secgrp " + row[3])
                else:
                    secgrp = ""

                # Scope variable
                if row[4] != "":
                    scope = (" -scope " + row[4])
                else:
                    scope = ""

                # Dexcription variable
                if row[5] != "":
                    desc = (" -desc " + row[4])
                else:
                    desc = ""

                # Group variables
                if row[6] == "":
                    group1 = ""
                    group2 = ""
                    group3 = ""
                    group4 = ""
                else:
                    grouplist = row[6].split(", ")
                    group1 = (' -memberof "cn=' + grouplist[0] + domaininput1 + domaininput2 + domaininput3 + '"')

                    if len(grouplist) == 2:
                        group2 = (' "cn=' + grouplist[1] + domaininput1 + domaininput2 + domaininput3 + '"')
                    else:
                        group2 = ""

                    if len(grouplist) == 3:
                        group2 = (' "cn=' + grouplist[1] + domaininput1 + domaininput2 + domaininput3 + '"')
                        group3 = (' "cn=' + grouplist[2] + domaininput1 + domaininput2 + domaininput3 + '"')
                    else:
                        group3 = ""

                    if len(grouplist) == 4:
                        group2 = (' "cn=' + grouplist[1] + domaininput1 + domaininput2 + domaininput3 + '"')
                        group3 = (' "cn=' + grouplist[2] + domaininput1 + domaininput2 + domaininput3 + '"')
                        group4 = (' "cn=' + grouplist[3] + domaininput1 + domaininput2 + domaininput3 + '"')
                    else:
                        group4 = ""

                # Member variables
                if row[7] == "":
                    member1 = ""
                    member2 = ""
                    member3 = ""
                    member4 = ""
                    member5 = ""
                    member6 = ""
                    member7 = ""
                    member8 = ""
                    member9 = ""
                    member10 = ""
                else:
                    memberlist = row[7].split(", ")
                    member1 = (' -memberof "cn=' + memberlist[0] + domaininput1 + domaininput2 + domaininput3 + '"')
                    member2 = ""
                    member3 = ""
                    member4 = ""
                    member5 = ""
                    member6 = ""
                    member7 = ""
                    member8 = ""
                    member9 = ""
                    member10 = ""

                    if len(memberlist) == 1:
                        member2 = (' "cn=' + memberlist[1] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member3 = ""
                        member4 = ""
                        member5 = ""
                        member6 = ""
                        member7 = ""
                        member8 = ""
                        member9 = ""
                        member10 = ""
                    if len(memberlist) == 2:
                        member2 = (' "cn=' + memberlist[1] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member3 = ""
                        member4 = ""
                        member5 = ""
                        member6 = ""
                        member7 = ""
                        member8 = ""
                        member9 = ""
                        member10 = ""

                    if len(memberlist) == 3:
                        member2 = (' "cn=' + memberlist[1] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member3 = (' "cn=' + memberlist[2] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member4 = ""
                        member5 = ""
                        member6 = ""
                        member7 = ""
                        member8 = ""
                        member9 = ""
                        member10 = ""

                    if len(memberlist) == 4:
                        member2 = (' "cn=' + memberlist[1] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member3 = (' "cn=' + memberlist[2] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member4 = (' "cn=' + memberlist[3] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member5 = ""
                        member6 = ""
                        member7 = ""
                        member8 = ""
                        member9 = ""
                        member10 = ""

                    if len(memberlist) == 5:
                        member2 = (' "cn=' + memberlist[1] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member3 = (' "cn=' + memberlist[2] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member4 = (' "cn=' + memberlist[3] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member5 = (' "cn=' + memberlist[4] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member6 = ""
                        member7 = ""
                        member8 = ""
                        member9 = ""
                        member10 = ""

                    if len(memberlist) == 6:
                        member2 = (' "cn=' + memberlist[1] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member3 = (' "cn=' + memberlist[2] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member4 = (' "cn=' + memberlist[3] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member5 = (' "cn=' + memberlist[4] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member6 = (' "cn=' + memberlist[5] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member7 = ""
                        member8 = ""
                        member9 = ""
                        member10 = ""

                    if len(memberlist) == 7:
                        member2 = (' "cn=' + memberlist[1] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member3 = (' "cn=' + memberlist[2] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member4 = (' "cn=' + memberlist[3] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member5 = (' "cn=' + memberlist[4] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member6 = (' "cn=' + memberlist[5] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member7 = (' "cn=' + memberlist[6] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member8 = ""
                        member9 = ""
                        member10 = ""

                    if len(memberlist) == 8:
                        member2 = (' "cn=' + memberlist[1] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member3 = (' "cn=' + memberlist[2] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member4 = (' "cn=' + memberlist[3] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member5 = (' "cn=' + memberlist[4] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member6 = (' "cn=' + memberlist[5] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member7 = (' "cn=' + memberlist[6] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member8 = (' "cn=' + memberlist[7] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member9 = ""
                        member10 = ""

                    if len(memberlist) == 9:
                        member2 = (' "cn=' + memberlist[1] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member3 = (' "cn=' + memberlist[2] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member4 = (' "cn=' + memberlist[3] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member5 = (' "cn=' + memberlist[4] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member6 = (' "cn=' + memberlist[5] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member7 = (' "cn=' + memberlist[6] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member8 = (' "cn=' + memberlist[7] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member9 = (' "cn=' + memberlist[8] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member10 = ""

                    if len(memberlist) == 10:
                        member2 = (' "cn=' + memberlist[1] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member3 = (' "cn=' + memberlist[2] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member4 = (' "cn=' + memberlist[3] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member5 = (' "cn=' + memberlist[4] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member6 = (' "cn=' + memberlist[5] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member7 = (' "cn=' + memberlist[6] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member8 = (' "cn=' + memberlist[7] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member9 = (' "cn=' + memberlist[8] + domaininput1 + domaininput2 + domaininput3 + '"')
                        member10 = (' "cn=' + memberlist[8] + domaininput1 + domaininput2 + domaininput3 + '"')

                txtbox.insert(END, 'dsadd group ' + distinguishedname + secgrp + scope + desc + group1 + group2 +
                              group3 + group4 + member1 + member2 + member3 + member4 + member5 + member6 + member7 +
                              member8 + member9 + member10 + "\n")

        # END OF GROUP IMPORT SETTINGS #

        # START OF COMPUTER IMPORT SETTINGS #

        if mode.get() == "Computer":
            for row in csv_reader:
                name = row[0]

                if row[1] != "":
                    ou = (",ou=" + row[1])
                else:
                    ou = ""

                domainlist = row[2].split(".")
                domaininput1 = (",dc=" + domainlist[0])
                domaininput2 = (",dc=" + domainlist[1])

                if len(domainlist) == 3:
                    domaininput3 = (",dc=" + domainlist[2])
                else:
                    domaininput3 = ""

                distinguishedname = '"cn=' + name + ou + domaininput1 + domaininput2 + domaininput3 + '"'

                # Description variable
                if row[3] != "":
                    desc = (" -desc " + row[3])
                else:
                    desc = ""

                # Location variable
                if row[4] != "":
                    loc = (" -loc " + row[4])
                else:
                    loc = ""

                # Group variables
                if row[5] == "":
                    group1 = ""
                    group2 = ""
                    group3 = ""
                    group4 = ""
                else:
                    grouplist = row[5].split(", ")
                    group1 = (' -memberof "cn=' + grouplist[0] + domaininput1 + domaininput2 + domaininput3 + '"')
                    group2 = ""
                    group3 = ""
                    group4 = ""

                    if len(grouplist) == 2:
                        group2 = (' "cn=' + grouplist[1] + domaininput1 + domaininput2 + domaininput3 + '"')
                        group3 = ""
                        group4 = ""

                    if len(grouplist) == 3:
                        group2 = (' "cn=' + grouplist[1] + domaininput1 + domaininput2 + domaininput3 + '"')
                        group3 = (' "cn=' + grouplist[2] + domaininput1 + domaininput2 + domaininput3 + '"')
                        group4 = ""

                    if len(grouplist) == 4:
                        group2 = (' "cn=' + grouplist[1] + domaininput1 + domaininput2 + domaininput3 + '"')
                        group3 = (' "cn=' + grouplist[2] + domaininput1 + domaininput2 + domaininput3 + '"')
                        group4 = (' "cn=' + grouplist[3] + domaininput1 + domaininput2 + domaininput3 + '"')

                txtbox.insert(END, 'dsadd group ' + distinguishedname + desc + loc + group1 + group2 +
                              group3 + group4 + "\n")

        # END OF COMPUTER IMPORT SETTINGS #

        # START OF OU IMPORT SETTINGS #

        if mode.get() == "OU":
            for row in csv_reader:
                name = row[0]

                domainlist = row[1].split(".")
                domaininput1 = (",dc=" + domainlist[0])
                domaininput2 = (",dc=" + domainlist[1])

                if len(domainlist) == 3:
                    domaininput3 = (",dc=" + domainlist[2])
                else:
                    domaininput3 = ""

                distinguishedname = '"ou=' + name + domaininput1 + domaininput2 + domaininput3 + '"'

                # Description variable
                if row[2] != "":
                    desc = (" -desc " + row[2])
                else:
                    desc = ""

                txtbox.insert(END, 'dsadd ou ' + distinguishedname + desc + "\n")

        # END OF OU IMPORT SETTINGS #


def exp_btn():
    global s
    if mode.get() == "User":
        with open(os.path.join(desktop, 'dsadduser.bat'), 'w') as OPATH:
            OPATH.writelines([txtbox.get(1.0, END)])
    if mode.get() == "Computer":
        with open(os.path.join(desktop, 'dsaddcomputer.bat'), 'w') as OPATH:
            OPATH.writelines([txtbox.get(1.0, END)])
    if mode.get() == "Group":
        with open(os.path.join(desktop, 'dsaddgroup.bat'), 'w') as OPATH:
            OPATH.writelines([txtbox.get(1.0, END)])
    if mode.get() == "Organizational Unit":
        with open(os.path.join(desktop, 'dsaddou.bat'), 'w') as OPATH:
            OPATH.writelines([txtbox.get(1.0, END)])
    if mode.get() == "Contact":
        with open(os.path.join(desktop, 'dsaddcontact.bat'), 'w') as OPATH:
            OPATH.writelines([txtbox.get(1.0, END)])
    s.set("Batch file saved to desktop")


def options_btn():
    if modeselect_cb.get() == "User":
        user_options_window()
    if modeselect_cb.get() == "Group":
        group_options_window()
    if modeselect_cb.get() == "Computer":
        computer_options_window()
    if modeselect_cb.get() == "OU":
        ou_options_window()


def csv_template_btn():
    userheaders = "name", "ou", "domain", "employee id", "password", "groups", "telephone", "email", "mobile", "fax", \
                  "title", "department", "company", "manager", "home dir", "home drv", "profile", "logon script", \
                  "must change pwd", "can change pwd", "pwd never expires", "acct expires", "disabled"
    groupheaders = "name", "ou", "domain", "secgrp", "scope", "desc", "groups", "members"
    computerheaders = "name", "ou", "domain", "desc", "loc", "groups"
    ouheaders = "name", "domain", "desc"
    if mode.get() == "User":
        with open(os.path.join(desktop, "dsadduser.csv"), 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(userheaders)
    if mode.get() == "Groups":
        with open(os.path.join(desktop, "dsaddgroup.csv"), 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(groupheaders)
    if mode.get() == "Computer":
        with open(os.path.join(desktop, "dsaddcomputer.csv"), 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(computerheaders)
    if mode.get() == "OU":
        with open(os.path.join(desktop, "dsaddou.csv"), 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(ouheaders)


def clrentry_btn(self=window):
    global s
    for widget in input_frame.winfo_children():
        if "ent" in str(widget):
            widget.delete(0, END)
    for widget in parameter_frame.winfo_children():
        if "ent" in str(widget):
            widget.delete(0, END)
    s.set("Entries cleared")

    if mode.get() == "User":
        self.firstnameent.focus_set()
    if mode.get() == "Group":
        self.groupnameent.focus_set()
    if mode.get() == "Computer":
        self.computernameent.focus_set()
    if mode.get() == "OU":
        self.ounameent.focus_set()


def clrall_btn(self=window):
    global s
    clrentry_btn()
    txtbox.delete(1.0, END)
    s.set("All cleared")

    if mode.get() == "User":
        self.firstnameent.focus_set()
    if mode.get() == "Group":
        self.groupnameent.focus_set()
    if mode.get() == "Computer":
        self.computernameent.focus_set()
    if mode.get() == "OU":
        self.ounameent.focus_set()


def close_btn():
    window.quit()


def resetstatus():
    global s
    s.set("Ready")


modeselect_lbl = Label(mode_frame, text="Select mode: ").grid(row=0, column=0)
modeselect_cb = ttk.Combobox(mode_frame, state="readonly", values=["", "User", "Computer", "Group", "OU", "Contact"],
                             textvariable=mode)
modeselect_cb.current(0)
modeselect_cb.grid(row=0, column=1)
modeselect_cb.bind("<<ComboboxSelected>>", get_mode)
txtbox = Text(text_frame)
txtbox.pack(expand=True, fill=BOTH)

submitbtn = Button(topbtn_frame, width=14, text="Submit", command=submit_btn)
submitbtn.pack(side=LEFT, padx=5, pady=5)
copybtn = Button(topbtn_frame, width=14, text="Copy to Clipboard", command=copy_btn)
copybtn.pack(side=LEFT, padx=5, pady=5)
impbtn = Button(topbtn_frame, width=14, text="Import", command=imp_btn)
impbtn.pack(side=LEFT, padx=5, pady=5)
expbtn = Button(topbtn_frame, width=14, text="Export", command=exp_btn)
expbtn.pack(side=LEFT, padx=5, pady=5)
optionsbtn = Button(topbtn_frame, width=14, text="Options", command=options_btn)
optionsbtn.pack(side=LEFT, padx=5, pady=5)
createcsvbtn = Button(btmbtn_frame, width=14, text="CSV Template", command=csv_template_btn)
createcsvbtn.pack(side=LEFT, padx=5, pady=5)
clrentrybtn = Button(btmbtn_frame, width=14, text="Clear Entries", command=clrentry_btn)
clrentrybtn.pack(side=LEFT, padx=5, pady=5)
clrallbtn = Button(btmbtn_frame, width=14, text="Clear All", command=clrall_btn)
clrallbtn.pack(side=LEFT, padx=5, pady=5)
closebtn = Button(btmbtn_frame, width=14, text="Close", command=close_btn)
closebtn.pack(side=LEFT, padx=5, pady=5)

stat1 = Label(status_frame, textvariable=s)
stat1.pack(side=LEFT, pady=5, padx=5)

mainloop()
