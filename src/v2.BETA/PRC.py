"""
    @Date                 : 24.05.2025
    @Author               : Stein Lundbeck
    @Name                 : SLT Assets tools
    @Description          : Tool for managing web project resources like Sass, JavaScript, images and distribution of items
    @Version              : 1.0.0.4
    @Latest               : 19.06.2025
"""

import json
import sys
from slt_functions import print_str, up, to_list
from entities import Project
from watcher_repo import WatcherRepo

valid_args = ["menu", "naub", "config"]

def run_menu():
    """Shows a menu for running different features"""
    print("menu")

def run_config():
    """Runs features for editing config"""
    print("config")

def load_config():
    """Loads config values"""
    config = None
    with open("Config.json", encoding="utf-8") as val:
        config = json.load(val)
    i = 0
    projects = {}
    for p in config["projects"]:
        projects[p["name"]] = Project(p, i)
        i = up(i)
    watcher = WatcherRepo(projects)
    watcher.start()

def main():
    """Main entry point for the PRC tool"""
    print_str("SLT Project Resource Compiler v2", True)
    load_config()
    args = sys.argv
    if len(args) > 1:
        arg = args[1].replace("--", "").lower()
        if arg in valid_args:
            match arg:
                case "menu":
                    run_menu()
                case "config":
                    run_config()
        else:
            print_str(f"Error: argument '{arg}' not valid")
            print_str(f"Valid arguments: {to_list(valid_args)}")

if __name__ == "__main__":
    main()
