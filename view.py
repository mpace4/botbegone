import sys
import model
from tkinter import *
from tkinter import font as tkFont


def twitter_username_input():
    global username
    root = Tk()
    root.title("Botbegone")
    root.resizable(False, False)
    username = None
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    root.geometry("+{}+{}".format(positionRight, positionDown))
    
    bbFont = tkFont.Font(family="times", size=30, weight="bold")
    
    def exitProgram():
        root.destroy()
    
    
    def usernameSubmit():
        global username
        print(f"Checking twitter username: @{usernameEntry.get()}")
        username = usernameEntry.get()
        exitProgram()

    
    def user_help():
        messagebox.showinfo("help", "This is a simple program to check the "
                            "probability if a twitter account is a bot! Just "
                            "type the username of the person you would like "
                            "to check in the box and hit enter, the % chance "
                            "of that account being a bot will then be "
                            "displayed. \nWhen inputting a username, just "
                            "type in the twitter accounts name without the "
                            "“@” where prompted to. ")
    
    def press_enter(event):
        usernameSubmit()
    
    usernameLabel = Label(root, text="Twitter User Name")
    usernameEntry = Entry(root, bd=5, justify="right")
    submitBtn = Button(root, text="submit", command=usernameSubmit)
    helpBtn = Button(root, text="help", command=user_help)
    exitBtn = Button(root, text="exit", command=exitProgram)
    
    usernameLabel.grid(row=0, column=0, columnspan=2, padx = 5, pady=5)
    usernameEntry.grid(row=1, column=0, padx = 5, pady=5)
    submitBtn.grid(row=1, column=1, padx=5, pady=5)
    helpBtn.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    exitBtn.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
    
    root.bind("<Return>", press_enter)
    
    mainloop()
    return username

def display_output(listOutput:list):
    root2 = Tk()
    root2.title("Botbegone")
    root2.resizable(False, False)
    windowWidth = root2.winfo_reqwidth()
    windowHeight = root2.winfo_reqheight()
    positionRight = int(root2.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root2.winfo_screenheight()/2 - windowHeight/2)
    root2.geometry("+{}+{}".format(positionRight, positionDown))
    
    bbFont = tkFont.Font(family="times", size=15, weight="bold")
    bbFont2 = tkFont.Font(family="Helvetica", size=12, weight="normal")
    
    def exitProgram():
        root2.destroy()
        sys.exit()
    
    def goAgain():
        twitter_username_input()
        
        
    outputLabel = Label(root2, text=listOutput[0], font=bbFont2)
    outputLabel2 = Label(root2, text=listOutput[1], font = bbFont2)
    outputLabel3 = Label(root2, text=listOutput[2], font = bbFont2)
    outputLabel4 = Label(root2, text=listOutput[3], font = bbFont2)
    outputLabel5 = Label(root2, text=listOutput[4], font = bbFont2)
    outputLabel6 = Label(root2, text=listOutput[5], font = bbFont)
    exitButton = Button(root2, text="Close", command=exitProgram, font=bbFont)
    goAgainButton = Button(root2, text="Look up another user", command=goAgain, font=bbFont)
    outputLabel.grid(row=0, column=0, )
    outputLabel2.grid(row=1, column=0, )
    outputLabel3.grid(row=2, column=0, )
    outputLabel4.grid(row=3, column=0, )
    outputLabel5.grid(row=4, column=0, )
    outputLabel6.grid(row=5, column=0, )
    exitButton.grid(row=6, column=0)
    goAgainButton.grid(row=7, column = 0)
    
    root2.mainloop()
    
    
    
