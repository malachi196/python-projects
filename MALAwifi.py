from tkinter import *
from tkinter import messagebox
import platform
import time
import sys
import os
import subprocess
import threading


class colors:
    green = '\033[32m'
    red = '\033[31m'
    blue = '\033[34m'
    yellow = '\033[33m'
    gray = 'gray'
    magenta = '\033[35m'
    darkgrey = 'darkslategrey'
    end = '\033[0m'
    

device = platform.platform()
DVEce = colors.green + device + colors.end
infodict = {"devices": DVEce,"debugging":True,"directory":os.getcwd()}

def close():
    global infodict
    print("closing...")
    time.sleep(2.4)
    infodict["debugging"] = False
    print("closed succesfully")
    time.sleep(0.5)

commands = {"close":close}
compatibility = {"compatibility":""}

#=====intro=====

def platformAVAILABILITY():
    global compatibility
    try:
        if platform.platform() >= "Windows-10-10.0.19045-SP0":
            compatibility["compatibility"] = "supports all functions used in the shell"
        else:
            compatibility["compatibility"] = "might have some limited abilities"
    except:
        print(colors.red + "ERROR RETREIVING BUILD INFORMATION" + colors.end)

platformAVAILABILITY()

print(colors.magenta
      + "this project is made by @malachi196 on github\n"
      + colors.blue
      + "Welcome to MALAwifi SHELL\n"
      + "the shell for all network information\n"
      + colors.end
      + f"\nyou are running {infodict['devices']}, which {compatibility['compatibility']}"
      + colors.end)

time.sleep(1)
print("type "
      + colors.green
      + "help" 
      + colors.end
      + " for a list of commands")

#=====commands=====

def help():
    print("\ncommands:\n"
          + "\tclose -- closes shell\n"
          + "\tcredits -- people who helped to create this project\n"
          +"\tterminal -- opens powershell commands in shell\n"
          +"\t\tclose -- exits terminal\n"
          +"\t\tnetsh -- opens NETSH commands\n"
          +"\t\t\twlan -- wireless lan(TYPE 'exit' TO EXIT)\n"
          + colors.red
          + "\t\t(NETSH wlan is still under construction until further notice)\n"
          + colors.blue
          +"bug fixes soon to come"
          + colors.end)
commands['help'] = help

def credits():
    print(colors.magenta
          + "this project was mainly built by @malachi196 on github, but with ideas from @mas6y6"
          + colors.end)
commands['credits'] = credits

def SELF_DESTRUCT():
    print(colors.red
        + f"@{infodict['directory']}---ABORTING NETSH---\n"
        + "AUTOMATIC SELF DESTRUCT EXECUTING IN 5\n")
    time.sleep(1)
    print("4\n")
    time.sleep(1)
    print("3\n")
    time.sleep(1)
    print("2\n")
    time.sleep(1)
    print("1\n"
    + colors.end)
    print("executing...")
    time.sleep(1)
    exit()
    
#=====thread netsh=====
def netsh():
    subprocess.run('netsh')
    
threadofnetsh =  threading.Thread(target=netsh)

def tsnetshTHREADSTART():
    threadofnetsh.daemon = True
    threadofnetsh.start()

class gettsnetshTHREAD:
    def __init__(self) -> None:
        self.__init__ = tsnetshTHREADSTART.__get__()

#=====terminal=====
def terminal():
    global infodict, threadofnetsh
    print("opening terminal...")
    time.sleep(1)
    while True:
        target = input(f"${infodict['directory']}> ")
        if target == "close":
            print('exiting terminal...')
            time.sleep(1)
            commands.pop('netsh')
            break
        elif target == 'netsh':
            global gettsnetshTHREAD
            root = Tk()
            def ABORTALLPROCESSES():
                root.destroy()
                threadofnetsh.join()
                SELF_DESTRUCT()       
            lbl1 = Label(root,text="type exit to exit netsh,\n then click this button")
            lbl1.pack(side=TOP)
            btn1 = Button(root,text="kill program",command=ABORTALLPROCESSES)
            btn1.pack(side=TOP)
            tsnetshTHREADSTART()
            while True:
                root.mainloop()
                commands['netsh'] = netsh
                try:
                    if target == 'close':
                        subprocess.TimeoutExpired()
                        break
                    if gettsnetshTHREAD == 'close':
                        subprocess.TimeoutExpired()
                        commands.pop('netsh')
                        break
                except:
                    SELF_DESTRUCT()
                try:
                    if netsh == 'close':
                        break
                    else:
                        pass
                except:
                    SELF_DESTRUCT()
        else:
            SUB = subprocess.Popen(target,stdout=subprocess.PIPE, shell=True)
            print(SUB.stdout.decode('utf8'))
commands['terminal'] = terminal


#=====final running program=====
while infodict["debugging"] == True:
    if infodict["debugging"] == True:
        inputWdir = input(f"@{infodict['directory']}> ")
        output = inputWdir.split(' ')
        cmd = output[0]
        output.pop(0)
        try:
            if output == []:
                commands[cmd]()
            else:
                commands[cmd](output)
        except KeyError:
            print(colors.red
                  + f"#{infodict['directory']}--ERROR: the term '{cmd}' is not recognized as an operatable function"
                  + colors.end)
        except Exception:
            print(colors.red
                  + f"#{infodict['directory']}--ERROR: error occured while trying to run '{cmd}'"
                  + colors.end)    