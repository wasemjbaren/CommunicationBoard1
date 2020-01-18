import Requests
import tkinter.messagebox as tkMessageBox
from tkinter import filedialog
import shutil
import os
import glob
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
user = 0
try:
    file = open('connected.txt', 'r')
    user = int(file.read())
except (FileNotFoundError, ValueError):
    user = 0


root = tk.Tk()
root.title('Communication board')
main = tk.Frame(root)

class variables:
    def __init__(self):
        self.USERNAME = tk.StringVar()
        self.PASSWORD = tk.StringVar()
        self.FIRSTNAME = tk.StringVar()
        self.LASTNAME = tk.StringVar()
        self.ISADMIN = tk.StringVar()
        self.PHONE = tk.StringVar()
        self.NAME = tk.StringVar()
        self.CITY = tk.StringVar()
        self.BIRTHDAY = tk.StringVar()
        self.SITS = tk.StringVar()
        self.ENTRY = tk.StringVar()
        self.DATE = tk.StringVar()

    def resetVariables(self):
        self.USERNAME.set("")
        self.PASSWORD.set("")
        self.FIRSTNAME.set("")
        self.LASTNAME.set("")
        self.ISADMIN.set("")
        self.PHONE.set("")
        self.PHONE.set("")
        self.NAME.set("")
        self.CITY.set("")
        self.BIRTHDAY.set("")
        self.SITS.set("")
        self.ENTRY.set("")
        self.DATE.set("")
vars = variables()


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = screen_width
height =screen_height
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

def RegisterForm(flag):
    RegisterFrame = tk.Frame(root)
    RegisterFrame.pack(side=tk.TOP, pady=40)
    lbl_username = tk.Label(RegisterFrame, text="Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=1)
    lbl_password = tk.Label(RegisterFrame, text="Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=2)
    lbl_firstname = tk.Label(RegisterFrame, text="Firstname:", font=('arial', 18), bd=18)
    lbl_firstname.grid(row=3)
    lbl_lastname = tk.Label(RegisterFrame, text="Lastname:", font=('arial', 18), bd=18)
    lbl_lastname.grid(row=4)
    lbl_rule = tk.Label(RegisterFrame, text="Is Admin?:", font=('arial', 18), bd=18)
    lbl_rule.grid(row=5)
    lbl_phone = tk.Label(RegisterFrame, text="Phone", font=('arial', 18), bd=18)
    lbl_phone.grid(row=6)
    lbl_result2 = tk.Label(RegisterFrame, text="", font=('arial', 18))
    lbl_result2.grid(row=7, columnspan=2)
    username = tk.Entry(RegisterFrame, font=('arial', 20), textvariable=vars.USERNAME, width=15)
    username.grid(row=1, column=1)
    password = tk.Entry(RegisterFrame, font=('arial', 20), textvariable=vars.PASSWORD, width=15, show="*")
    password.grid(row=2, column=1)
    firstname = tk.Entry(RegisterFrame, font=('arial', 20), textvariable=vars.FIRSTNAME, width=15)
    firstname.grid(row=3, column=1)
    lastname = tk.Entry(RegisterFrame, font=('arial', 20), textvariable=vars.LASTNAME, width=15)
    lastname.grid(row=4, column=1)
    rule = tk.Entry(RegisterFrame, font=('arial', 20), textvariable=vars.ISADMIN, width=15)
    rule.grid(row=5, column=1)
    rule = tk.Entry(RegisterFrame, font=('arial', 20), textvariable=vars.PHONE, width=15)
    rule.grid(row=6, column=1)
    register = tk.Button(RegisterFrame, text="Register", font=('arial', 18), width=35)#need command
    register.bind('<Button-1>', lambda event, frame=RegisterFrame, flag=flag: Register(frame, flag))
    register.grid(row=7, columnspan=2, pady=20)
    if flag:
        login = tk.Button(RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
        login.grid(row=0, sticky=tk.W)
        login.bind('<Button-1>', lambda event, frame=RegisterFrame: ToggleToLogin(RegisterFrame))
    else:
        back_button(RegisterFrame)


def LoginForm():
    LoginFrame = tk.Frame(root)
    LoginFrame.pack(side=tk.TOP, pady=80)
    s=0
    try:
        f = open('connected.txt', 'r')
        f = f.read()
        s = int(f)
    except (FileNotFoundError, ValueError):
        s = 0
    if s != 0:
        toggle_to_main_page(LoginFrame, False)
    else:
        l = tk.Label(LoginFrame, text="Communication Board", fg='red', font=('arial', 40), bd=18)
        l.grid(row=0)
        lbl_username = tk.Label(LoginFrame, text="Username:", font=('arial', 25), bd=18)
        lbl_username.grid(row=1)
        lbl_password = tk.Label(LoginFrame, text="Password:", font=('arial', 25), bd=18)
        lbl_password.grid(row=2)
        lbl_result1 = tk.Label(LoginFrame, text="", font=('arial', 18))
        lbl_result1.grid(row=3, columnspan=2)
        username = tk.Entry(LoginFrame, font=('arial', 20), textvariable=vars.USERNAME, width=15)
        username.grid(row=1, column=1)
        password = tk.Entry(LoginFrame, font=('arial', 20), textvariable=vars.PASSWORD, width=15, show="*")
        password.grid(row=2, column=1)
        btn_login = tk.Button(LoginFrame, text="Login", font=('arial', 18), width=35)#updated
        btn_login.grid(row=4, columnspan=2, pady=20)
        btn_reg = tk.Button(LoginFrame, text="Forgot Password", font=('arial', 18), width=35)
        btn_reg.grid(row=5, columnspan=2, pady=20)
        lbl_register = tk.Button(LoginFrame, text="Register", font=('arial', 18), width=35)
        lbl_register.grid(row=6, columnspan=2)
        lbl_register.bind('<Button-1>', lambda event, frame=LoginFrame: ToggleToRegister(frame, True))
        btn_login.bind('<Button-1>', lambda event, frame=LoginFrame, flag=True: toggle_to_main_page(LoginFrame, True))
        btn_reg.bind('<Button-1>', lambda event, frame=LoginFrame: toggle_to_forgot(LoginFrame))


def ForgotForm():
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=80)
    lbl_message = tk.Label(frame, text='Please Enter the following information', font=('arial', 25), bd=18)
    lbl_message.grid(row=1)
    lbl_username = tk.Label(frame, text="Username:", font=('arial', 25), bd=18)
    lbl_username.grid(row=2)
    lbl_phone = tk.Label(frame, text="Phone: ", font=('arial', 25), bd=18)
    lbl_phone.grid(row=3)
    lbl_pass = tk.Label(frame, text="new password", font=('arial', 25), bd=18)
    lbl_pass.grid(row=4)
    username = tk.Entry(frame, font=('arial', 20), textvariable=vars.USERNAME, width=15)
    username.grid(row=2, column=1)
    phone = tk.Entry(frame, font=('arial', 20), textvariable=vars.PHONE, width=15)
    phone.grid(row=3, column=1)
    password = tk.Entry(frame, font=('arial', 20), textvariable=vars.PASSWORD, width=15)
    password.grid(row=4, column=1)
    login = tk.Button(frame, text="Login", fg="Blue", font=('arial', 12))
    login.grid(row=0, sticky=tk.W)
    login.bind('<Button-1>', lambda event, frame=frame: ToggleToLogin(frame))



    reset = tk.Button(frame, text="Reset Password", font=('arial', 12), width=35)
    reset.grid(row=5, sticky=tk.W)
    reset.bind('<Button-1>', lambda event, frame=frame: resetPass(frame))


def resetPass(frame):
    if(Requests.ResetPass(vars.USERNAME.get(), vars.PHONE.get(), vars.PASSWORD.get())):
        vars.resetVariables()
        frame.destroy()
        LoginForm()
    else:
        result = tkMessageBox.askokcancel('Incoreect data', 'Please correct data')





def ToggleToLogin(frame):
    frame.destroy()
    LoginForm()


def toggle_to_forgot(frame):
    frame.destroy()
    ForgotForm()


def ToggleToRegister(frame, flag):
    frame.destroy()
    RegisterForm(flag)


def Register(frame, flag):
    a = 0
    if(vars.ISADMIN.get() == 'yes'):
        a = 1
    if(Requests.AddUser(vars.FIRSTNAME.get(), vars.LASTNAME.get(), vars.PHONE.get(), vars.USERNAME.get(), vars.PASSWORD.get(), a)):
        vars.resetVariables()
        frame.destroy()
        if flag:
            LoginForm()
        else:
            main_frame()

    else:
        result = tkMessageBox.askokcancel('Incoreect data', 'Please correct data')


def toggle_to_main_page(LoginFrame, flag, event=None):
    global user
    u = Requests.CheckLogin(vars.USERNAME.get(), vars.PASSWORD.get())
    if u == -1 and flag:
        result = tkMessageBox.askokcancel('Incoreect data', 'user name or password isnt correct')
    else:
        if flag:
            user = u
            vars.resetVariables()
            with open('connected.txt', 'w') as file:
                file.write(str(user))
        LoginFrame.destroy()
        main_frame()

def add_child_to_db(frame, event=None):
    result = Requests.AddChild(vars.NAME.get(), vars.CITY.get(), vars.BIRTHDAY.get(), vars.SITS.get())
    if result:
        vars.resetVariables()
        frame.destroy()
        main_frame()
    else:
        result = tkMessageBox.askokcancel('Incoreect data', 'Please correct data')


def add_child():
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=80)
    l_name = tk.Label(frame, text="Full Name:", font=('arial', 18), bd=18)
    l_name.grid(row=1)
    name = tk.Entry(frame, font=('arial', 20), textvariable=vars.NAME, width=15)
    name.grid(row=1, column=1)
    l_city = tk.Label(frame, text="City:", font=('arial', 18), bd=18)
    l_city.grid(row=2)
    city = tk.Entry(frame, font=('arial', 20), textvariable=vars.CITY, width=15)
    city.grid(row=2, column=1)
    l_birth = tk.Label(frame, text="Birth day:", font=('arial', 18), bd=18)
    l_birth.grid(row=3)
    birth = tk.Entry(frame, font=('arial', 20), textvariable=vars.BIRTHDAY, width=15)
    birth.grid(row=3, column=1)
    l_sits = tk.Label(frame, text="Number of sittings:", font=('arial', 18), bd=18)
    l_sits.grid(row=4)
    sits = tk.Entry(frame, font=('arial', 20), textvariable=vars.SITS, width=15)
    sits.grid(row=4, column=1)
    add = tk.Button(frame, text="Add Child", font=('arial', 18), width=35)  # need command
    add.bind('<Button-1>', lambda event, frame=frame: add_child_to_db(frame))
    add.grid(row=7, columnspan=2, pady=20)
    back_button(frame)


def toggle_to_add_child(frame, event=None):
    frame.destroy()
    add_child()

def a():
    result = tkMessageBox.askokcancel('Incoreect data', 'Please correct data')


def edit_image(frame):
    frame.destroy()
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=80)
    file = ""
    def select():
        nonlocal file
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", defaultextension=
        (("jpeg files", "*.jpg"), ("all files", "*.*")))
    def update():
        if Requests.UpdateImage(file, vars.ENTRY.get()):
            result = tkMessageBox.askokcancel('Add', 'Image edited successfully')
        else:
            result = tkMessageBox.askokcancel('Add', 'Error in edit image')
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=80)

    remove = tk.Button(frame, text="Select Image", font=('arial', 18), width=35)
    remove.bind('<Button-1>', lambda event, flag=False: select())
    remove.grid(row=1, columnspan=2, pady=20)
    l_name = tk.Label(frame, text="Description: ", font=('arial', 18), bd=18)
    l_name.grid(row=2)
    desc = tk.Entry(frame, font=('arial', 20), textvariable=vars.ENTRY, width=15)
    desc.grid(row=2, column=1)

    u = tk.Button(frame, text="Update", font=('arial', 18), width=35)
    u.bind('<Button-1>', lambda event, flag=False: update())
    u.grid(row=3, columnspan=2, pady=20)
    back_button(frame)




def load_images():
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=80)

    def new_image():
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", defaultextension=
        (("jpeg files", "*.jpg"), ("all files", "*.*")))
        try:
            os.mkdir('images')
        except FileExistsError:
            print(filename)
        finally:
            try:
                shutil.copy(filename, 'images')
            except shutil.SameFileError:
                print('a')
            s = filename.split('/')
            s = s[len(s) - 1]
            print(s)
            if Requests.AddImage('images/' + s):
                result = tkMessageBox.askokcancel('Add', 'Image added successfully')
            else:
                result = tkMessageBox.askokcancel('Add', 'Error in Adding image')


        print('s')

    def remove_image():
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", defaultextension=
        (("jpeg files", "*.jpg"), ("all files", "*.*")))
        if Requests.DeleteImage(filename):
            os.remove(filename)
            result = tkMessageBox.askokcancel('Remove', 'Image removed successfully')
        else:
            result = tkMessageBox.askokcancel('Remove', 'Error in removing image')


    add_image = tk.Button(frame, text="Add New Image", font=('arial', 18), width=35)
    add_image.bind('<Button-1>', lambda event: new_image())
    add_image.grid(row=1, columnspan=2, pady=20)

    edit = tk.Button(frame, text="Edit Image", font=('arial', 18), width=35)
    edit.bind('<Button-1>', lambda event, flag=False, frame=frame: edit_image(frame))
    edit.grid(row=2, columnspan=2, pady=20)

    remove = tk.Button(frame, text="Remove image", font=('arial', 18), width=35)
    remove.bind('<Button-1>', lambda event, flag=False: remove_image())
    remove.grid(row=3, columnspan=2, pady=20)

    back_button(frame)


def toggle_to_images(frame, event=None):
    frame.destroy()
    load_images()

def toggle_to_rec(frame, event=None):
    def recommed():
        global user
        text = vars.ENTRY.get()
        vars.resetVariables()
        Requests.SendRecommend(user, text)

    frame.destroy()
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=80)
    label = tk.Label(frame, text="Recommendation: ", font=('arial', 18), bd=18)
    label.grid(row=1)
    entry = tk.Entry(frame, font=('arial', 20), textvariable=vars.ENTRY, width=60)
    entry.grid(row=2)
    but = tk.Button(frame, text="Send Recommendation", font=('arial', 18), width=35)  # need command
    but.bind('<Button-1>', lambda event, frame=frame: recommed())
    but.grid(row=3, columnspan=2, pady=20)
    back_button(frame)



def toggle_to_child_com(frame, event=None):
    def write_comment():
        text = vars.ENTRY.get()
        flag = Requests.AddCommentForChild(user, vars.FIRSTNAME.get(), text)
        vars.resetVariables()
        if not flag:
            result = tkMessageBox.askokcancel('Incoreect data', 'invalid child name')

    frame.destroy()
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=80)
    label = tk.Label(frame, text="Write comment for child: ", font=('arial', 18), bd=18)
    label.grid(row=1)
    e_label = tk.Label(frame, text="child name: ", font=('arial', 18), bd=18)
    e_label.grid(row=2)
    entry = tk.Entry(frame, font=('arial', 20), textvariable=vars.FIRSTNAME, width=15)
    entry.grid(row=3)
    e_labe = tk.Label(frame, text="comment: ", font=('arial', 18), bd=18)
    e_labe.grid(row=4)
    entry = tk.Entry(frame, font=('arial', 20), textvariable=vars.ENTRY, width=60)
    entry.grid(row=5)
    but = tk.Button(frame, text="Send comment", font=('arial', 18), width=35)  # need command
    but.bind('<Button-1>', lambda event, frame=frame: write_comment())
    but.grid(row=6, columnspan=2, pady=20)
    back_button(frame)

def back_button(frame, flag=False):
    btn = tk.Button(frame, text="Back to main page", font=('arial', 18), width=35)
    btn.bind('<Button-1>', lambda event, frame=frame: return_to_main_page(frame))
    if flag:
        btn.pack(side=tk.BOTTOM)
    else:
        btn.grid(row=10)

def return_to_main_page(frame):
    frame.destroy()
    main_frame()


def toggle_to_guide(frame, event=None):
    frame.destroy()
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=80)
    label_guide = tk.Label(frame, text="This is user guide, write here all the guides for the user", font=('arial', 18), bd=18)
    label_guide.grid(row=1)
    back_button(frame)

def toggle_to_contact(frame,event=None):
    frame.destroy()
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=80)
    label_guide = tk.Label(frame, text="Write here all information about developer", font=('arial', 18),bd=18)
    label_guide.grid(row=1)
    back_button(frame)

def ask_holiday(frame, event=None):
    frame.destroy()
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=80)
    def ask():
        if not Requests.AskForHoliday(user, vars.DATE.get()):
            result = tkMessageBox.askokcancel('Incoreect data', 'This date already packed')
        else:
            l = tk.Label(frame, text="Holiday saved", font=('arial', 18), bd=18)
            l.grid(row=3)

    frame.pack(side=tk.TOP, pady=80)
    label = tk.Label(frame, text="Type date for holiday: ", font=('arial', 18),bd=18)
    label.grid(row=1)
    e = tk.Entry(frame, font=('arial', 20), textvariable=vars.DATE, width=15)
    e.grid(row=1, column=1)
    btn = tk.Button(frame, text="Ask", font=('arial', 18), width=35)
    btn.bind('<Button-1>', lambda event: ask())
    btn.grid(row=2, columnspan=2, pady=20)
    back_button(frame)


def view_rec(frame, event=None):
    frame.destroy()
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=40)
    tree = ttk.Treeview(frame)
    tree["columns"] = ("one", "two")
    tree.column("one", stretch=tk.NO)
    tree.column("two", width=400, stretch=tk.YES)
    tree.heading("one", text='Name', anchor=tk.W)
    tree.heading("two", text='Recommendation', anchor=tk.W)
    tree.pack(side=tk.TOP, fill=tk.X)
    lst = Requests.GetRecommendations()
    for line in lst:
        r = Requests.GetUser(line['UserID'])
        name = r['FirstName'] + ' ' + r['LastName']
        comment = line['Comment']
        tree.insert("",tk.END, values=(name, comment))

    back_button(frame, True)

def view_holidays(frame, event=None):
    frame.destroy()
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=40)
    tree = ttk.Treeview(frame)
    tree["columns"] = ("one", "two")
    tree.column("one", stretch=tk.NO)
    tree.column("two", width=400, stretch=tk.YES)
    tree.heading("one", text='Name', anchor=tk.W)
    tree.heading("two", text='Date', anchor=tk.W)
    tree.pack(side=tk.TOP, fill=tk.X)
    lst = Requests.GetHolidays()
    for line in lst:
        r = Requests.GetUser(line['UserID'])
        name = r['FirstName'] + ' ' + r['LastName']
        comment = line['Date']
        tree.insert("", tk.END, values=(name, comment))

    back_button(frame, True)
def child_data(frame, r):
    frame.destroy()
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=40)
    tk.Label(frame, text="Child name: " + r[0]['FullName'], font=('arial', 18), bd=18).grid(row=1)
    tk.Label(frame, text="City: " + r[0]['City'], font=('arial', 18), bd=18).grid(row=2)
    tk.Label(frame, text="Birthday: " + r[0]['Birthday'], font=('arial', 18), bd=18).grid(row=3)
    tk.Label(frame, text="Sitting: " + str(r[0]['Sitting']), font=('arial', 18), bd=18).grid(row=4)

    j=6
    tk.Label(frame, text="Comments:", font=('arial', 18), bd=18).grid(row=5)
    for i in range(min(len(r[1]), 4)):
        comment = r[1][i]['Comment']
        print(r[1][i]['UserID'])
        user = Requests.GetUser(r[1][i]['UserID'])
        name = user['FirstName'] + ' ' + user['LastName']
        tk.Label(frame, text=name + ': ' + comment, font=('arial', 18), bd=18).grid(row=j)
        j += 1

    back_button(frame, True)

def toggle_to_child(frame):
    frame.destroy()
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=40)

    def get():
        r = Requests.GetChild(vars.FIRSTNAME.get())
        if r is None:
            result = tkMessageBox.askokcancel('Incoreect data', 'Please correct data')
            vars.resetVariables()
        else:
            child_data(frame, r)
            back_button(frame, True)

    label = tk.Label(frame, text="Enter child name: ", font=('arial', 18), bd=18)
    label.grid(row=1)
    e = tk.Entry(frame, font=('arial', 20), textvariable=vars.FIRSTNAME, width=15)
    e.grid(row=1, column=1)
    btn = tk.Button(frame, text="Ask", font=('arial', 18), width=35)
    btn.bind('<Button-1>', lambda event: get())
    btn.grid(row=2, columnspan=2, pady=20)

def checkPlay(frame, value):
    if(value == int(str(vars.DATE.get()))):
        result = tkMessageBox.askokcancel('coreect data', 'Correct answer')
        play(frame)
    else:
        result = tkMessageBox.askokcancel('incoreect data', 'inCorrect answer')
    vars.resetVariables()

def play(frame):
    import random
    frame.destroy()
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=80)

    first = random.randint(1,20)
    second = random.randint(1,20)
    operator = random.choice(["-","+","*"])
    if(operator ==  "-" and  first <  second):
        temp= first
        first = second
        second = temp

    value =  0
    if operator == "+" :
        value = first + second
    elif operator == "-":
        value = first - second
    else:
        value = first * second

    label = tk.Label(frame, text=str(first) + " " + operator + " " + str(second) + " = ", font=('arial', 30), bd=18)
    label.grid(row=1)
    e = tk.Entry(frame, font=('arial', 30), textvariable=vars.DATE, width=10)
    e.grid(row=1, column=1)
    btn = tk.Button(frame, text="Answer", font=('arial', 30), width=10)
    btn.grid(row=2, columnspan=2, pady=20)
    btn.bind('<Button-1>', lambda event, value=value, frame=frame: checkPlay(frame, value))

def child_window():
    def messageWindow():
        win = tk.Toplevel(pady=80)
        win.geometry("%dx%d+%d+%d" % (width, height, x, y))
        def action():
            result = tkMessageBox.askokcancel('Help', 'The consultant will come in two minutes')

        path = 'images'
        COLUMNS = 10
        image_count = 0
        for infile in glob.glob(os.path.join(path, '*.jpeg')):
            image_count += 1
            r, c = divmod(image_count - 1, COLUMNS)
            im = Image.open(infile)
            resized = im.resize((200, 200), Image.ANTIALIAS)
            tkimage = ImageTk.PhotoImage(resized)
            myvar = tk.Button(win, image=tkimage, command=action)
            myvar.image = tkimage
            myvar.grid(row=r, column=c)
    messageWindow()

def main_frame():
    global user, main
    frame = tk.Frame(root)
    main = frame
    frame.pack(side=tk.TOP, pady=10)
    u = Requests.GetUser(user)
    if int(u['isAdmin']) == 1:
        register = tk.Button(frame, text="Add New Worker", font=('arial', 18), width=35)  # need command
        register.bind('<Button-1>', lambda event, frame=frame, flag=False: ToggleToRegister(frame, False))
        register.grid(row=1, columnspan=2, pady=20)

        child = tk.Button(frame, text="Add New Child", font=('arial', 18), width=35)
        child.bind('<Button-1>', lambda event, frame=frame: toggle_to_add_child(frame))
        child.grid(row=2, columnspan=2, pady=20)

        images = tk.Button(frame, text="Images", font=('arial', 18), width=35)
        images.bind('<Button-1>', lambda event, frame=frame, flag=False: toggle_to_images(frame))
        images.grid(row=3, columnspan=2, pady=20)

        recommend = tk.Button(frame, text="View Recommendations", font=('arial', 18), width=35)
        recommend.bind('<Button-1>', lambda event, frame=frame: view_rec(frame))
        recommend.grid(row=4, columnspan=2, pady=20)

        holi = tk.Button(frame, text="View Holidays Requests", font=('arial', 18), width=35)
        holi.bind('<Button-1>', lambda event, frame=frame: view_holidays(frame))
        holi.grid(row=5, columnspan=2, pady=20)


    else:
        rec = tk.Button(frame, text="Recommend", font=('arial', 18), width=35)
        rec.grid(row=1, columnspan=2, pady=20)
        rec.bind('<Button-1>', lambda event, frame=frame: toggle_to_rec(frame))

        child_comment = tk.Button(frame, text="Write comment for a child", font=('arial', 18), width=35)
        child_comment.grid(row=2, columnspan=2, pady=20)
        child_comment.bind('<Button-1>', lambda event, frame=frame: toggle_to_child_com(frame))

        child_data = tk.Button(frame, text="Child data", font=('arial', 18), width=35)
        child_data.grid(row=3, columnspan=2, pady=20)
        child_data.bind('<Button-1>', lambda event, frame=frame: toggle_to_child(frame))

        guide = tk.Button(frame, text="User Guide", font=('arial', 18), width=35)
        guide.grid(row=4, columnspan=2, pady=20)
        guide.bind('<Button-1>', lambda event, frame=frame: toggle_to_guide(frame))

        holiday = tk.Button(frame, text="Ask for holiday", font=('arial', 18), width=35)
        holiday.grid(row=5, columnspan=2, pady=20)
        holiday.bind('<Button-1>', lambda event, frame=frame: ask_holiday(frame))
        playBtn = tk.Button(frame, text="Play game", font=('arial', 18), width=35)
        playBtn.grid(row=6, columnspan=2, pady=20)
        playBtn.bind('<Button-1>', lambda event, frame=frame: play(frame))

        contact = tk.Button(frame, text="Contact developer", font=('arial', 18), width=35)
        contact.grid(row=7, columnspan=2, pady=20)
        contact.bind('<Button-1>', lambda event, frame=frame: toggle_to_contact(frame))

        forChild = tk.Button(frame, text="For child", font=('arial', 18), width=35)
        forChild.grid(row=8, columnspan=2, pady=20)
        forChild.bind('<Button-1>', lambda event, frame=frame: child_window())


    log = tk.Button(frame, text="Logout", font=('arial', 18), width=35)
    log.grid(row=9, columnspan=2, pady=20)
    log.bind('<Button-1>', lambda event, frame=frame: logout(frame))



def logout(frame):
    global user
    try:
        open('connected.txt', 'w').close()
    except FileNotFoundError:
        print('a')
    result = tkMessageBox.askquestion('System', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes':
        user = 0
        ToggleToLogin(frame)

def remove_user():
    Requests.RemoveUser(user)
    root.destroy()
    exit()


menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Logout", command=logout)
filemenu.add_command(label="Remove Account", command=remove_user)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)
LoginForm()
root.mainloop()