import json
from pprint import pprint
import sys
import os
from wsgiref import validate
import typer
import pyfiglet
from datetime import date
import inquirer

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
az_project_wizart_ascii = """
                             /\\
                            /  \\
                           |    |
                         --:'''':--
                           :'_' :
                           _:"":\___
            ' '      ____.' :::     '._
           . *=====<<=)           \    :
            .  '      '-'-'\_      /'._.'
                             \====:_ ""
                            .'     \\
                           :       :
                          /   :    \\
                         :   .      '.
         ,. _        snd :  : :      :
      '-'    ).          :__:-:__.;--'
    (        '  )        '-'   '-'
 ( -   .00.   - _
(    .'  _ )     )
'-  ()_.\,\,   -
"""
#should_close = False
app = typer.Typer()

def change_project_json(path:str,project_name:str, render_api = "AZ_RENDER_API_OPENGL",cmake_version = "3.6"):
    json_path = os.path.join(path,"project.json")
    json_path = json_path.replace("\\\\","/")
    json_path = json_path.replace("\\","/")
    json_file = open(json_path,"r")
    data = json.load(json_file)
    data["project"]["name"] = project_name
    data["project"]["render_api"] = render_api
    data["project"]["cmake_minimum_version"] = float(cmake_version)
    json_formatted_str = json.dumps(data, indent=2)
    json_file.close()
    json_file = open(json_path,"w")
    json_file.write(json_formatted_str)
    return

def clone_repo(project_name:str, project_path:str,vcpkg:bool = False):
    project_whole_path = os.path.join(project_path,project_name)
    if(os.path.isdir(project_whole_path)):
        if(os.listdir(project_whole_path) != 0):
            color_print("WARNING: directory is not empty.","yellow")
            return False
    color_print(f"Creating '{project_name}' at '{project_path}'","green")
    if(vcpkg):
        os.system(f"git clone --depth 1 --recursive https://github.com/Byte-White/Appazoid-Project-Template-VCPKG \"{project_whole_path}\"")        
    else:
        os.system(f"git clone --depth 1 --recursive https://github.com/Byte-White/Appazoid-Project-Template \"{project_whole_path}\"")
    return True

@app.command()
def new_project(project_name:str, project_path:str):
    project_whole_path = os.path.join(project_path,project_name)
    if(clone_repo(project_name,project_path)):
        change_project_json(project_whole_path,project_name)
        

#@app.command()
#def exit():
#    global should_close
#    should_close = True
todays_date = date.today()

def validate_project_name(answers, proj_name):
    if(proj_name == ""):
        print("Can't think of a name? Well think harder.")
        return False
    proj_path = os.path.join(answers["path"],proj_name)
    proj_path = proj_path.replace("\\\\","/")
    proj_path = proj_path.replace("\\","/")
    if(os.path.isdir(proj_path)):
        if(os.listdir(proj_path).__len__() != 0):
            color_print("Warning: Directory is not empty! Please change the name of the project.")
            return False
    return True

questions = [
    inquirer.Path(
        "path",
        message = "select a path ",
        
    ),

    inquirer.Text(
        "name",
        message = "what is your project's name?",  
        validate= validate_project_name
    ),

    inquirer.Text(
        
        "cmake_version",
        message = "what is the minimum cmake version?",
        default="3.6"
    ),
    
    inquirer.List(
        
        "render_api",
        message = "what rendering api do you want to use?",
        choices=["OpenGL","Vulkan"],
        default="OpenGL"
    ),
    inquirer.Checkbox(
        "vcpkg",
        message= "would you like to use vcpkg template? (X=True ; o=False)",
        choices=["vcpkg"],
    ),
]

@app.command()
def project_wizard():
    print(az_project_wizard_art)
    print(az_project_wizart_ascii)
    global questions
    answers = inquirer.prompt(questions)
    if(clone_repo(answers["name"],answers["path"])):
        change_project_json(os.path.join(answers["path"],answers["name"]),answers["name"],answers["render_api"],answers["cmake_version"])
    
    


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
