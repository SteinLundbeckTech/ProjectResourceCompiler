"""
    @Date                 : 24.05.2025
    @Author               : Stein Lundbeck
    @Name                 : SLT Assets tools
    @Description          : Tool for managing web project resources like Sass, JavaScript, images and distribution of items
    @Version              : 1.0.0.2
    @Latest               : 24.05.2025
"""

import json
import sys
from datetime import datetime
from SLtFunctions import *

class Project:
    """Represents a project loaded from config"""
    def __init__(self, project, index):
        self.project = project
        self.index = index
        self.name = project["name"]

def run_menu():
    """Shows a menu for running different features"""
    print("menu")

def run_main():
    """Execs the main module of PRC"""
    load_config()

def run_config():
    """Runs features for editing config"""
    print("config")

def run_backup():
    """Creates a copy of all config files"""
    print("backup")

def run_copy():
    """Copies content of config file to clipboard"""
    print("copy")

def run_install():
    """Installs all features and files"""
    print("install")

def load_config():
    """Loads config values"""
    config = None
    with open("Config.json", encoding="utf-8") as val:
        config = json.load(val)
    i = 0
    projects = {}
    for p in config["projects"]:
        projects[p["name"]] = Project(p, i)
    load_projects(projects)
    projects = {}
    i = 0
    for p in config["projects"]:
        projects[p["name"]] = Project(p, i)
        i = up(i)
    load_projects(projects)

def load_projects(projects):
    """Loads all projects from config"""
    start_time = datetime.now()
    for n, p in projects.items():
        print_str(f"Loading project > {n}")
    run_load_finished(start_time, len(projects))

def run_load_finished(start_time, projects_count):
    """Loading finished"""
    diff = (datetime.now() - start_time).total_seconds()
    if diff <= 60:
        diff = diff / 60
    if projects_count == 1:
        print_str(f"Loaded 1 project in {diff_minute(start_time, datetime.now())} minutes")
    else:
        print_str(f"Loaded {projects_count} projects in {diff_minute(start_time, datetime.now())} minutes")

def load():
    """Loads the basic loading of PRC"""
    cls()
    print_str("SLT Project Resource Compiler v2")
    valid_args = ["menu", "naub", "config", "backup", "copy", "install"]
    args = sys.argv
    if len(args) > 1:
        arg = args[1].replace("--", "").lower()
        if arg in valid_args:
            match arg:
                case "menu":
                    run_menu()
                case "main":
                    run_main()
                case "config":
                    run_config()
                case "backup":
                    run_backup()
                case "copy":
                    run_copy()
                case "install":
                    run_install()
        else:
            print_str(f"Error: argument '{arg}' not valid")
            print_str(f"Valid arguments: {to_list(valid_args)}")
    else:
        run_main()

load()
