# -*- coding: utf-8 -*-
'''
PING_CMDR
Written by David A Ray

'''

#import libraries
import os
import sys
import datetime as dt
from time import sleep
import subprocess


application = "Ping_CMDR"
version = "0.05.10"
name = application + "  V" + version
email = "David@DREAM-Enterprise.com"

#set start times
currdate = dt.date.today().strftime("%Y%m%d")
currtime = dt.datetime.now().strftime("%H:%M:%S")
start_time = dt.datetime.now().strftime("%H%M%S")

#define varibles
dev_0 = "Internet"
ip_0 = "8.8.8.8"

dev_1 = "Commander"
ip_1 = "192.168.31.11"

dev_2 = "Router"
ip_2 = "192.168.31.31"

dev_3 = "POS 1"
ip_3 = "192.168.31.101"

dev_4 = "POS 2"
ip_4 = "192.168.31.102"

dev_5 = "Pinpad 1"
ip_5 = "192.168.31.126"

dev_6 = "Pinpad 2"
ip_6 = "192.168.31.127"

output_file = "Ping Log - " + currdate + " - " + start_time
output_folder = "Ping Logs"

option_0 = "Exit"
option_1 = "Feature Not Supported"
option_2 = "Feature Not Supported"
option_3 = "Run Ping Tool (BP/Shell Sites Only)"
option_4 = "Run Ping Tool (Non-BP/Shell Sites Only)"
option_5 = "Toggle Log File Function"

#define defaults
ping_0 = 0
ping_1 = 0
ping_2 = 0
ping_3 = 0
ping_4 = 0
ping_5 = 0
ping_6 = 0

var_0 = 0
var_1 = 0
var_2 = 0
var_3 = 0
var_4 = 0
var_5 = 0
var_6 = 0

scan = 31

log_file = 0
diag = 0
loop_count = 0

#define system varibles

wait = 1
splash_wait = 2.5

width = 65
lines = 18
cent_width = int(width)-1
dev_width = 10

#define cosole size and color
os.system("mode con: cols=" + str(width) + " lines=" + str(lines))
os.system("color F")
os.system("cls")
os.system("echo off")

#define commands
def logo():
    os.system("cls")
    os.system("echo off")
    print ()
    print ("   .______    __  .__   __.   _______      ".center(cent_width))
    print ("   |   _  \  |  | |  \ |  |  /  _____|     ".center(cent_width))
    print ("   |  |_)  | |  | |   \|  | |  |  __       ".center(cent_width))
    print ("   |   ___/  |  | |  . `  | |  | |_ |      ".center(cent_width))
    print ("   |  |      |  | |  |\   | |  |__| |      ".center(cent_width))
    print ("   | _|      |__| |__| \__|  \______|      ".center(cent_width))
    print ("  ______ .___  ___.  _______  .______      ".center(cent_width))
    print (" /      ||   \/   | |       \ |   _  \     ".center(cent_width))
    print ("|  ,----'|  \  /  | |  .--.  ||  |_)  |    ".center(cent_width))
    print ("|  |     |  |\/|  | |  |  |  ||      /     ".center(cent_width))
    print ("|  `----.|  |  |  | |  '--'  ||  |\  \----.".center(cent_width))
    print (" \______||__|  |__| |_______/ | _| `._____|".center(cent_width))
    print ()
    print (name.center(cent_width))
    print ("David A Ray".center(cent_width))
    print ()
    print (("Contact: " + email).center(cent_width))

    
    sleep(splash_wait)
    
def main_menu():
    global log_file, ui, diag
    os.system("cls")
    print ()
    print ()
    print (name.center(cent_width))
    print ()
    if log_file == (0):
        print ("Logging Function Disabled".center(cent_width))
    else:
        print ("Logging Function  Enabled".center(cent_width))
    if diag == (1):
        print ("Diagnostics Mode Enabled".center(cent_width))
    print ()
    print ("  0 - " + option_0)
    print ("  1 - " + option_1)
    print ("  2 - " + option_2)
    print ("  3 - " + option_3)
    print ("  4 - " + option_4)
    print ("  5 - " + option_5)
    print ()
    option = input("  Enter Your Selection: [0/1/2/3/4/5] ")
    if option == ("0"):
        end()
    elif option == ("1"):
        funct_not_supp()
    elif option == ("2"):
        funct_not_supp()
    elif option == ("3"):
        ui = 1
    elif option == ("4"):
        ui = 2
    elif option == ("5"):
        if log_file == 0:
            log_file = 1
            main_menu()
        else:
            log_file = 0
            main_menu()
    elif option.lower() == ("diag"):
        if diag == 0:
            diag = 1
            main_menu()
        else:
            diag = 0
    else:
        main_menu()
    
def end():
    os.system("cls")
    print ()
    print ()
    print (name.center(cent_width))
    print ()
    print ()
    print ("...Program Ending...".center(cent_width))
    print ()
    print ()
    print ()
    sleep(splash_wait)
    sys.exit()
    
def funct_not_supp():
    os.system("cls")
    print ()
    print ()
    print (name.center(cent_width))
    print ()
    print ()
    print ("FUNCTION NOT SUPPORTED".center(cent_width))
    print ()
    print ()
    print ()
    sleep(splash_wait)
    main_menu()
  
#create folder for logs
def mk_output_folder():
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    
#creates and opens log file
def open_file(file_name):
    global f
    #with open(file_name + ".txt", 'w') as f:
    f = open(output_folder + "\\" + file_name + ".txt","w")
    f.write(application + " V" + version + "\n")
    f.write("Starting Date - " + currdate + "\n")
    f.write("Starting Time - " + currtime + "\n")
    f.write("\n")
    f.flush()
        
#set initial starting times
def init_time():
    global currtime
    global uptime_0
    global uptime_1
    global uptime_2
    global uptime_3
    global uptime_4
    global uptime_5
    global uptime_6
    currtime = dt.datetime.now().strftime("%H:%M:%S")
    uptime_0 = currtime
    uptime_1 = currtime
    uptime_2 = currtime
    uptime_3 = currtime
    uptime_4 = currtime
    uptime_5 = currtime
    uptime_6 = currtime
    
def check_ping():
    global ping_0
    global uptime_0
    global var_0
    global ping_1
    global uptime_1
    global var_1
    global ping_2
    global uptime_2
    global var_2
    global ping_3
    global uptime_3
    global var_3
    global ping_4
    global uptime_4
    global var_4
    global ping_5
    global uptime_5
    global var_5
    global ping_6
    global uptime_6
    global var_6
   
    var_0 = ping_0    
    host = ip_0
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in str(ping)) or ('timed' in str(ping)) or ('failure' in str(ping)):
        ping_0 = 0
    else:
        ping_0 = 1    

    var_1 = ping_1    
    host = ip_1
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in str(ping)) or ('timed' in str(ping)) or ('failure' in str(ping)):
        ping_1 = 0
    else:
        ping_1 = 1

    var_2 = ping_2
    host = ip_2
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in str(ping)) or ('timed' in str(ping)) or ('failure' in str(ping)):
        ping_2 = 0
    else:
        ping_2 = 1    
        
    var_3 = ping_3
    host = ip_3
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in str(ping)) or ('timed' in str(ping)) or ('failure' in str(ping)):
        ping_3 = 0
    else:
        ping_3 = 1   
        
    var_4 = ping_4
    host = ip_4
    ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
    if ('unreachable' in str(ping)) or ('timed' in str(ping)) or ('failure' in str(ping)):
        ping_4 = 0
    else:
        ping_4 = 1  

#if ui = 2
    if ui == (2):
        var_5 = ping_5
        host = ip_5
        ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
        if ('unreachable' in str(ping)) or ('timed' in str(ping)) or ('failure' in str(ping)):
            ping_5 = 0
        else:
            ping_5 = 1  
    
        var_6 = ping_6
        host = ip_6
        ping = subprocess.Popen(["ping.exe","-n","1","-w","1",host],stdout = subprocess.PIPE).communicate()[0]
        if ('unreachable' in str(ping)) or ('timed' in str(ping)) or ('failure' in str(ping)):
            ping_6 = 0
        else:
            ping_6 = 1  
        
def set_uptime():
    global uptime_0
    global uptime_1
    global uptime_2
    global uptime_3
    global uptime_4
    global uptime_5
    global uptime_6
    global currtime
    currtime = dt.datetime.now().strftime("%H:%M:%S")
    if var_0 != ping_0: 
        uptime_0 = currtime
    if var_1 != ping_1: 
        uptime_1 = currtime
    if var_2 != ping_2: 
        uptime_2 = currtime
    if var_3 != ping_3: 
        uptime_3 = currtime
    if var_4 != ping_4: 
        uptime_4 = currtime
    if var_5 != ping_5: 
        uptime_5 = currtime
    if var_6 != ping_6: 
        uptime_6 = currtime

def scan_count():
    global scan
    scan += 1
    if scan == 32:
        scan = 0
        
def write_file(file_name):
    
    if diag == 1:
        math = loop_count % 50
        if math == 0:
            f.write("***  Periodic Loop Count " + str(loop_count) + "\n")
    
    if var_0 != ping_0: 
        if ping_0 == 1:
            f.write(dev_0.ljust(dev_width) + " is UP   - " + uptime_0 + " - " + currdate + "\n")
            if diag == (1):
                f.write("Loop Count - " + str(loop_count) + "\n")
        else:
            f.write(dev_0.ljust(dev_width) + " is Down - " + uptime_0 +  " - " + currdate + "\n")
            if diag == (1):
                f.write("Loop Count - " + str(loop_count) + "\n")
       
    if var_1 != ping_1:
        if ping_1 == 1:
            f.write(dev_1.ljust(dev_width) + " is UP   - " + uptime_1 + " - " + currdate +  "\n")        
            if diag == (1):
                f.write("Loop Count - " + str(loop_count) + "\n")
        else:
            f.write(dev_1.ljust(dev_width) + " is DOWN - " + uptime_1 + " - " + currdate +  "\n")
            if diag == (1):
                f.write("Loop Count - " + str(loop_count) + "\n")
   
    if var_2 != ping_2:
        if ping_2 == 1:
            f.write(dev_2.ljust(dev_width) + " is UP   - " + uptime_2 + " - " + currdate +  "\n")        
            if diag == (1):
                f.write("Loop Count - " + str(loop_count) + "\n")
        else:
            f.write(dev_2.ljust(dev_width) + " is DOWN - " + uptime_2 + " - " + currdate +  "\n")
            if diag == (1):
                f.write("Loop Count - " + str(loop_count) + "\n")
   
    if var_3 != ping_3:
        if ping_3 == 1:
            f.write(dev_3.ljust(dev_width) + " is UP   - " + uptime_3 + " - " + currdate +  "\n")        
            if diag == (1):
                f.write("Loop Count - " + str(loop_count) + "\n")
        else:
            f.write(dev_3.ljust(dev_width) + " is DOWN - " + uptime_3 + " - " + currdate +  "\n")
            if diag == (1):
                f.write("Loop Count - " + str(loop_count) + "\n")
   
    if var_4 != ping_4:
        if ping_4 == 1:
            f.write(dev_4.ljust(dev_width) + " is UP   - " + uptime_4 + " - " + currdate +  "\n")        
            if diag == (1):
                f.write("Loop Count - " + str(loop_count) + "\n")
        else:
            f.write(dev_4.ljust(dev_width) + " is DOWN - " + uptime_4 + " - " + currdate +  "\n")
            if diag == (1):
                f.write("Loop Count - " + str(loop_count) + "\n")

    if ui == (2):
        if var_5 != ping_5:
            if ping_5 == 1:
                f.write(dev_5.ljust(dev_width) + " is UP   - " + uptime_5 + " - " + currdate + "\n")        
                if diag == (1):
                    f.write("Loop Count - " + str(loop_count) + "\n")
            else:
                f.write(dev_5.ljust(dev_width) + " is DOWN - " + uptime_5 + " - " + currdate +  "\n")
                if diag == (1):
                    f.write("Loop Count - " + str(loop_count) + "\n")
       
        if var_6 != ping_6:
            if ping_6 == 1:
                f.write(dev_6.ljust(dev_width) + " is UP   - " + uptime_6 + " - " + currdate +  "\n")        
                if diag == (1):
                    f.write("Loop Count - " + str(loop_count) + "\n")
            else:
                f.write(dev_6.ljust(dev_width) + " is DOWN - " + uptime_6 + " - " + currdate +  "\n")
                if diag == (1):
                    f.write("Loop Count - " + str(loop_count) + "\n")
   
    f.flush()

def run_process():
    global loop_count
    check_ping()
    set_uptime()
    if log_file == (1):
        write_file(output_file)
    if diag == (1):
        loop_count +=  1
    ui_screen()
    scan_count()
    sleep(wait)
    
def main():
    logo()
    main_menu()
    init_time()
    if log_file == (1):
        mk_output_folder()
        open_file(output_file)
    while 1 == 1:
        run_process()

#run commands
if __name__ == "__main__":
    main()