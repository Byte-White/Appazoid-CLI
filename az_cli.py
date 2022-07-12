import sys
import os
import typer
import pyfiglet
from datetime import datetime

########  PRINTING  ###################
def __prt_clr_help(str,color):
    white = "\033[39m"
    print(color,str,white)
    return
def color_print(str, color):
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    white = "\033[39m"
    if(color == "red"):
        __prt_clr_help(str,red)
    elif(color == "green"):
        __prt_clr_help(str,green)
    elif(color == "yellow"):
        __prt_clr_help(str,yellow)
    elif(color == "blue"):
        __prt_clr_help(str,blue)
    elif(color == "white"):
        __prt_clr_help(str,white)
    return
########################################


az_title_art = pyfiglet.figlet_format("APPAZOID      CLI")
az_project_wizard_art = pyfiglet.figlet_format("PROJ    WIZARD")
#should_close = False
app = typer.Typer()

@app.command()
def new_project(project_name:str, project_path:str):
    if(os.path.isdir(project_path+'\\'+project_name)):
        if(os.listdir(project_path+'\\'+project_name) != 0):
            color_print("WARNING: directory is not empty.","yellow")
            return
    color_print(f"Creating '{project_name}' at '{project_path}'","green")
    os.system(f"git clone --recursive https://github.com/Byte-White/Appazoid-Project-Template {project_path}/{project_name}")
        

#@app.command()
#def exit():
#    global should_close
#    should_close = True

@app.command()
def project_wizard():
    print(az_project_wizard_art)
    print("Todo: add inquirer")


if(__name__ == "__main__"):
    if(sys.argv.__len__()==1 or sys.argv.__len__()==2):
        print(az_title_art)    
    app()
    
#if(__name__ == "__main__"):
#    if(sys.argv.__len__() == 1):
#        print(az_title_art)
#    
#    if(sys.argv.__len__()>1):
#        app()
#    while(not should_close):
#        current_time = datetime.now().strftime("%H:%M:%S")
#        cli_input=input(f"[{current_time}]appazoid cli$ ")
#    print("exiting cli...")
