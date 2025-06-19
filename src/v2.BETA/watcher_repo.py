"""
@Date                 : 19.06.2025
@Author               : Stein Lundbeck
@Name                 : Watcher Repository
@Description          : Handles watching for changes
@Version              : 1.0.0.1
@Latest               : 19.06.2025
"""

import os
import time
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from slt_functions import print_str, diff_second
from entities import Defaults

class WatcherRepo:
    """Handles watching for changes in projects"""

    def __init__(self, projects):
        self.projects = projects
        self.observer = Observer()
        self.observers = {}

    def start(self):
        """Starts watching all projects"""
        loaded = False
        start_time = datetime.now()
        for project in self.projects.values():
            if os.path.exists(project.path):
                print_str(f"Loading project > {project.name}")
                handler = OnChangeHandler(project)
                self.observer.schedule(handler, project.path, recursive=True)
            else:
                print_str(f"Project path does not exist: {project.path}. Skipping project > {project.name}")
        self.observer.start()
        try:
            while True:
                tmp = "project"
                if len(self.projects) > 1:
                    tmp = "projects"
                if not loaded:
                    loaded = True
                    print_str(f"Loaded {len(self.projects)} {tmp} in {diff_second(start_time)} seconds")
                time.sleep(1)
        finally:
            self.observer.stop()
            self.observer.join()

    def stop(self):
        """Stops watching all projects"""
        self.observer.stop()
        self.observers.clear()

class OnChangeHandler(FileSystemEventHandler):
    """Handles file system events for a project"""

    def __init__(self, project):
        super().__init__()
        self.project = project

    def on_modified(self, event):
        """Called when a file is modified"""
        print(f"File modified: {event.src_path}")

    def on_created(self, event):
        """Called when a file is created"""
        print(f"File created: {event.src_path}")

    def on_deleted(self, event):
        """Called when a file is deleted"""
        print(f"File deleted: {event.src_path}")
