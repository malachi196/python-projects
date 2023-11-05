from tkinter import *
from tkinter import messagebox

class colors:
    green = 'green'
    black = 'black'
    grey =  'darkslategrey'
    darkgrey = '#222222'
    white = 'white'


root = Tk()
root.geometry('450x450')
root.title("utf-32 encoder")
root.tk_setPalette(background = colors.grey)


encoder_box = Entry(root,background= colors.green,fg=colors.white)
shell = Listbox(root,width=50,background= colors.green)
blanklabel = Label(root,text="\n")
blanklabel.pack(side=TOP)
encoder_box.pack(side=TOP)
starternumber = 0
changing_value = 1
finalnumber = starternumber + changing_value
shelltext = shell.get(ACTIVE)
log = []
othernull = encoder_box.get()

nullVALUE = [""]
nullVALUE = encoder_box.get()
nullVALUE.encode('utf-32')


def add_1():
    global changing_value,starternumber,finalnumber
    changing_value= changing_value + 1
    finalnumber = starternumber + changing_value

def mainEncoding():
    nullVALUE = encoder_box.get()
    shell.insert(1,str(finalnumber)+ "." + " encoded text: " + str(nullVALUE.encode('utf-32')))
    log.append(str([nullVALUE]))
    log.append(str([nullVALUE.encode('utf-32')]))
    add_1()

def delete():
    shell.delete(ANCHOR)

def write_file():
    global shelltext,log
    try:
        try:
            msBX = messagebox.askyesno("PYencoder", "create file?")
            if msBX == 1:
                with open('encoded' + '.txt',mode='wt',encoding='utf-8') as myfile:
                    myfile.write('\n'.join(log))
                    shell.insert(1,"file created")
                try:
                    open('encoded.txt','r')
                except:
                    print("file failed to open")
                    shell.insert(1,"file couldn't load")
        except:
             print("error with encoding")
    except:
        print("ERROR CREATING FILE")


btn1 = Button(root,text=" encode",bd=2,background=colors.darkgrey,fg= colors.green,
              command=mainEncoding)


btn2 = Button(root,text="delete",bd=2,background=colors.darkgrey,fg= colors.green,
              command=delete)

btn3 = Button(root,text="save results", bd=2,background=colors.darkgrey,fg= colors.green,
              command=write_file)

btn1.pack()
btn1.place(x=200,y=80)
shell.pack(side=BOTTOM)
shell.insert(0,"welcome to shell")
btn3.pack(side=BOTTOM)
btn2.pack(side=BOTTOM)


root.mainloop()