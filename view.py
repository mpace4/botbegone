import sys
import controller
from tkinter import Label, Button, Tk, messagebox, Entry, mainloop
from tkinter import font as tkFont

bgColor = "floral white"
btnColor = "PaleTurquoise1"


# gui to ask for twitter username
def twitter_username_input() -> str:
    global username
    root = Tk()
    root.title("Botbegone")
    root.resizable(False, False)
   # root.iconbitmap("D:/Chrome DLs/botbegone/botbegone-master/tweet.ico")
    root.configure(bg=bgColor)

    username = None
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    root.geometry("+{}+{}".format(positionRight, positionDown))

    bbFont = tkFont.Font(family="helvetica", size=15, weight="bold")

    def exitProgram():
        root.destroy()
        sys.exit(0)

    def usernameSubmit():
        global username
        print(f"Checking twitter username: @{usernameEntry.get()}")
        username = usernameEntry.get()
        root.destroy()

    def user_help():
        messagebox.showinfo("help", "This is a simple program to check the "
                            "probability if a twitter account is a bot! Just "
                            "type the username of the person you would like "
                            "to check in the box and hit enter, the number of "
                            "bot points will then be displayed. The higher "
                            "the bot points the more likely it is for that "
                            "account to be a bot \nWhen inputting a username,"
                            "just type in the twitter accounts name without "
                            "the “@” where prompted to. ")

    def press_enter(event):
        usernameSubmit()

    usernameLabel = Label(root, text="Input Twitter User Name",
                          font=bbFont, bg=bgColor, bd=5)
    usernameEntry = Entry(root, bd=10, justify="right", font=bbFont)
    submitBtn = Button(root, text="submit", command=usernameSubmit, bd=5,
                       font=bbFont)
    helpBtn = Button(root, text="help", command=user_help, bd=5,
                     font=bbFont)
    exitBtn = Button(root, text="exit", command=exitProgram, bd=5,
                     font=bbFont)

    usernameLabel.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    usernameEntry.grid(row=1, column=0, padx=(10, 0))
    submitBtn.grid(row=1, column=1, padx=5, pady=10)
    helpBtn.grid(row=2, column=0, columnspan=1, padx=10, pady=(0, 10),
                 ipadx=85)
    exitBtn.grid(row=2, column=1, columnspan=1, padx=10, pady=(0, 10),
                 ipadx=13)

    submitBtn.configure(bg=btnColor)
    exitBtn.configure(bg=btnColor)
    helpBtn.configure(bg=btnColor)

    root.bind("<Return>", press_enter)

    mainloop()
    return username


# gui to display output
def display_output(listOutput: list) -> None:
    root2 = Tk()
    root2.title("Botbegone")
    root2.resizable(False, False)
    #root2.iconbitmap("D:/Chrome DLs/botbegone/botbegone-master/tweet.ico")
    windowWidth = root2.winfo_reqwidth()
    windowHeight = root2.winfo_reqheight()
    positionRight = int(root2.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root2.winfo_screenheight()/2 - windowHeight/2)
    root2.geometry("+{}+{}".format(positionRight, positionDown))
    root2.configure(bg=bgColor)

    bbFont = tkFont.Font(family="times", size=18, weight="bold")
    bbFont2 = tkFont.Font(family="Helvetica", size=12, weight="normal")

    def exitProgram():
        root2.destroy()
        sys.exit()

    def goAgain():
        root2.destroy()
        controller.main()

    outputLabel = Label(root2, text=listOutput[0], font=bbFont2)
    outputLabel2 = Label(root2, text=listOutput[1], font=bbFont2)
    outputLabel3 = Label(root2, text=listOutput[2], font=bbFont2)
    outputLabel4 = Label(root2, text=listOutput[3], font=bbFont2)
    outputLabel5 = Label(root2, text=listOutput[4], font=bbFont2)
    outputLabel6 = Label(root2, text=listOutput[5], font=bbFont2)
    outputlabel7 = Label(root2, text=listOutput[6], font=bbFont)
    exitButton = Button(root2, text="Close", command=exitProgram, font=bbFont,
                        bd=5)
    goAgainButton = Button(root2, text="Look up another user", bd=5,
                           command=goAgain, font=bbFont)

    outputLabel.grid(row=0, column=0)
    outputLabel2.grid(row=1, column=0)
    outputLabel3.grid(row=2, column=0)
    outputLabel4.grid(row=3, column=0)
    outputLabel5.grid(row=4, column=0)
    outputLabel6.grid(row=5, column=0)
    outputlabel7.grid(row=6, column=0)
    goAgainButton.grid(row=7, column=0, padx=5, pady=5)
    exitButton.grid(row=8, column=0, ipadx=82, padx=5, pady=5)

    outputLabel.configure(bg=bgColor)
    outputLabel2.configure(bg=bgColor)
    outputLabel3.configure(bg=bgColor)
    outputLabel4.configure(bg=bgColor)
    outputLabel5.configure(bg=bgColor)
    outputLabel6.configure(bg=bgColor)
    exitButton.configure(bg=btnColor)
    goAgainButton.configure(bg=btnColor)

    root2.mainloop()
